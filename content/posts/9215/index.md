---
title: "[C#]Effective C# 條款一： 使用屬性代替公有欄位"
date: "2009-07-08 12:38:19"
description: "[C#]Effective C# 條款一： 使用屬性代替公有欄位"
tags: [CSharp]
---

<p>
	<img alt="image" border="0" height="181" src="\images\posts\9215\image_thumb.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="741" /></p>
<p>
	為何要用屬性來替代公有欄位主要有下列幾項原因：</p>
<ol>
	<li>
		符合物件導向封裝概念</li>
	<li>
		支援資料繫結</li>
	<li>
		具修改彈性</li>
</ol>
<p>
	 </p>
<h2>
	符合物件導向封裝概念</h2>
<p>
	屬性是對取得/修改內部數據的方法的一種擴展，從表面看來就像是數據成員，但內部卻是以方法實現。</p>
<p>
	在程式編譯後，編譯器在把程式編譯成MSIL時，會自動把屬性中的get區塊與set區塊編譯成兩個分離的方法。所以使用屬性能穫得函式的全部好處。</p>
<p>
	 </p>
<p>
	讓我們來看一下簡單的例子。假設今天有個People的類別，內含一個Name屬性，該屬性可讀可寫。</p>
<p>
	class People<br />
	{<br />
	    string Name { get; set; }<br />
	}</p>
<p>
	 </p>
<p>
	程式編譯後我們透過SDK內建的IL Disassembler工具查看MSIL。</p>
<p>
	<img alt="image" border="0" height="255" src="\images\posts\9215\image_thumb_4.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="245" /></p>
<p>
	 </p>
<p>
	我們可以發現Name屬性在MSIL中已不復可見，取而代之的是MSIL中多了兩個Method，一個是get_name、一個是set_name，這兩個方法分別對應至本來屬性的get與set區塊。</p>
<p>
	<img alt="image" border="0" height="369" src="\images\posts\9215\image_thumb_3.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="319" /></p>
<p>
	 </p>
<p>
	 </p>
<h2>
	支援資料繫結</h2>
<p>
	.NET中的資料繫結只支援屬性，並不支援公有欄位。這是因為資料繫結機制用反射來實作時只尋找類別的屬性。而之所以不支援公有欄位，主要是因為公有欄位把數據成員直接鋪暴露給外界較不符合物件導向的封裝原則。</p>
<p>
	 </p>
<h2>
	具修改彈性</h2>
<p>
	使用屬性在修改上也較一般公有欄位更具彈性。試想當程式中類別的公有欄位被頻繁的使用，則當我們要增加判斷防止公有欄位值為空時，我們勢必需要把散在程式中所有用到的地方都加上判斷才行。同樣的情況對於屬性來說，我們只需在屬性的get區塊增加判斷即可。</p>
<p>
	class People<br />
	{<br />
	    private string _name;<br />
	    public string Name<br />
	    {<br />
	        get<br />
	        {<br />
	            if (_name == null)<br />
	                return string.Empty;<br />
	            return _name;<br />
	        }<br />
	        set<br />
	        {<br />
	            _name = value;<br />
	        }<br />
	    }<br />
	}</p>
<p>
	 </p>
<p>
	 </p>
<p>
	若是日後要改成多執行緒程式，使用屬性也會比使用公有欄位容易來得修改。只要在get與set區塊中加入lock即可。</p>
<p>
	class People<br />
	{<br />
	    private string _name;<br />
	    public string Name<br />
	    {<br />
	        get<br />
	        {<br />
	            lock (this)<br />
	            {<br />
	                if (_name == null)<br />
	                    return string.Empty;<br />
	                return _name;<br />
	            }<br />
	        }<br />
	        set<br />
	        {<br />
	            lock (this)<br />
	            {<br />
	                _name = value;<br />
	            }<br />
	        }<br />
	    }<br />
	}</p>
<p>
	 </p>
<p>
	除此之外，使用屬性對於事件的增加也較為容易。</p>
<p>
	class People<br />
	{<br />
	    public event EventHandler NameChanging;<br />
	    public event EventHandler NameChanged;</p>
<p>
	    private string _name;<br />
	    public string Name<br />
	    {<br />
	        get<br />
	        {<br />
	            if (_name == null)<br />
	                return string.Empty;<br />
	            return _name;<br />
	        }<br />
	        set<br />
	        {<br />
	            if (_name != value)<br />
	            {<br />
	                NameChanging(this, new EventArgs());<br />
	                _name = value;<br />
	                NameChanged(this, new EventArgs());<br />
	            }<br />
	        }<br />
	    }<br />
	}</p>
<p>
	 </p>
<h2>
	注意事項</h2>
<p>
	雖然屬性與公有欄位在使用上看起來是一樣的，但不代表可以先寫成公有欄位以後有需要再改成屬性，因為公有欄位與屬性所編譯出的MSIL是不同的，因此若把公有欄位改為屬性，所有使用到本來公有欄位的程式都必需重新編譯，兩者以二進制的層級來看並非是兼容的。</p>
