---
title: "C++/CLI Managed解構子"
date: "2009-09-17 09:03:44"
description: "C++/CLI Managed解構子"
tags: [C++]
---

<p>
	在傳統C++中，解構子的寫法是"~類別名()"。而在C++/CLI中雖然也有這種寫法，但效果卻截然不同。</p>
<p>
	在C++/CLI Managed類別中，"~類別名()"其實相當於.NET程式的Dispose。在其它語言參考使用時，寫有"~類別名()"的類別，我們可以透過Dispose來釋放資源。</p>
<p>
	而要撰寫C++/CLI Managed類別的解構子，我們可以用"!類別名()"。</p>
<p>
	 </p>
<p>
	簡單的範例如下：</p>
<div class="wlWriterEditableSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:18b4b218-553d-4329-956a-7aa45e004ddb" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c:nocontrols" name="code">
ref class TestObj
{
public:
	//Dispose
	~TestObj() 
	{
		//Release resource
		...
	}

	//Deconstructer
	!TestObj() 
	{
		~TestObj();
	}
};</pre>
</div>
