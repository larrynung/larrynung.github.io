---
title: "[C#]設定WebBrowser Control運行的User Agent版本"
date: "2013-11-06 12:00:00"
description: "[C#]設定WebBrowser Control運行的User Agent版本"
tags: [CSharp]
---

<p>
	今天再弄WebBrowser Control元件的測試，發現IE9無法運行我寫的WebSocket程式，因此稍微測試了一下HTML5的支援程度，發現用IE開起來可以跑出138的分數，但在WebBrowser Control中只能跑出41分。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\430b9055-b166-466e-be27-7c709439c47d\image_thumb_2.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="574" /></p>
<p>
	 </p>
<p>
	經過Aaron大神的開示，發現這其實是因為直接用IE跟使用WebBrowser Control運行的是不同的User Agent。像是這邊筆者的IE跑的是IE9，但是WebBrowser Control跑的是IE7。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\430b9055-b166-466e-be27-7c709439c47d\image_thumb_3.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="598" /></p>
<p>
	 </p>
<p>
	所以我們必須要將WebBrowser Control的User Agent設定調整一下，我們可以透過修改IE的Feature登錄資訊來達到這個效果，機碼位置如下：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:bd19cbdd-8412-497d-904c-48a2b70cef37" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="xml" name="code">
32 bit:
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_BROWSER_EMULATION

64 bit:
HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_BROWSER_EMULATION
</pre>
</div>
<p>
	 </p>
<p>
	在這機碼下新增個跟應用程式同名的Dword Key，設定的值可參閱Internet Feature Controls (B..C)這篇文章，不同的值對應到不同版本的User Agent。</p>
<p>
	<img alt="image" border="0" height="596" src="\images\posts\430b9055-b166-466e-be27-7c709439c47d\image_thumb_7.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="415" /></p>
<p>
	 </p>
<p>
	像是筆者要將名為WindowsFormApplication3.exe的應用程式指定用IE9的User Agent下去運作，就可以像下面這般設定。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\430b9055-b166-466e-be27-7c709439c47d\image_thumb_4.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="584" /></p>
<p>
	 </p>
<p>
	除了手動修改外，我們也可以透過程式去做，像是下面這樣撰寫：</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:cda344d1-39ec-4e72-864b-8492582bfe0c" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
		...
		public Form1()
		{
			var appName = Process.GetCurrentProcess().MainModule.ModuleName;
			Registry.SetValue(@"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_BROWSER_EMULATION", appName, 9999, RegistryValueKind.DWord);
			InitializeComponent();	
		}
		...</pre>
</div>
<p>
	 </p>
<p>
	設定完後運行，可以看到已經使用IE9的User Agent下去運行。</p>
<p>
	<img alt="image" border="0" height="498" src="\images\posts\430b9055-b166-466e-be27-7c709439c47d\image_thumb_5.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="570" /></p>
<p>
	 </p>
<p>
	再次測試HTML5的支援程度，分數已從41分升為137分，跟直接用IE去開是差不多的。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\430b9055-b166-466e-be27-7c709439c47d\image_thumb_6.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="583" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		Web Browser Control – Specifying the IE Version</li>
	<li>
		Internet Feature Controls (B..C)</li>
	<li>
		More IE8 Extensibility Improvements</li>
	<li>
		C# 視窗程式：如何使用新版的瀏覽器控件？</li>
	<li>
		C# Web Browser component is IE7 not IE8? How to change this?</li>
</ul>
