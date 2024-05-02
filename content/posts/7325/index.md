---
title: "[C#][VB.NET]使用AxWindowsMediaPlayer撥放多媒體"
date: "2009-03-01 02:09:40"
description: "[C#][VB.NET]使用AxWindowsMediaPlayer撥放多媒體"
tags: [VB.NET,CSharp]
---

<h2>
	加入工具箱</h2>
<p>
	<strong>Step1.</strong>工具箱=&gt;滑鼠右鍵=&gt;選擇項目</p>
<p>
	<img alt="image" border="0" height="460" src="\images\posts\7325\image_thumb_1.png" width="214" /></p>
<p>
	 </p>
<p>
	<strong>Step2.</strong>切換至『COM 元件』頁籤=&gt;勾選Windows Media Player=&gt;確定</p>
<p>
	<img alt="image" border="0" height="380" src="\images\posts\7325\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="575" /></p>
<p>
	 </p>
<p>
	<strong>Step3.</strong>會發現工具箱多了個Windows Media Player的控制項</p>
<p>
	<img alt="image" border="0" height="46" src="\images\posts\7325\image_thumb_1.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="185" /></p>
<p>
	 </p>
<h2>
	使用AxWindowsMediaPlayer撥放多媒體</h2>
<p>
	<strong>Step1.</strong>加入Windows Media Player控制項到設計表單，可看到如下的畫面。</p>
<p>
	<img alt="image" border="0" height="347" src="\images\posts\7325\image_thumb_2.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="330" /></p>
<p>
	 </p>
<p>
	<strong>Step2.</strong>依序加入控制項使介面如下圖所示。</p>
<p>
	<img alt="image" border="0" height="466" src="\images\posts\7325\image_thumb_3.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="334" /></p>
<p>
	 </p>
<p>
	<strong>Step3.</strong>撰寫控制項初始設定程式碼</p>
<p>
	此處是設定控制項的初始值，像是音量的最大值、最小值、目前的音量、與啟動Timer(用來偵測檔案總長度用)，值得注意的是AxWindowsMediaPlayer控制項的音量大小介於0~100之間，另外若不設定AutoStart = False則開啟檔案完程式就會自動撥放開啟的多媒體檔。</p>
<p>
	VB.NET</p>
<div style="width: 768px; height: 157px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> Form1_Load(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> <span class="kwrd">MyBase</span>.Load</pre>
		<pre>
		<span class="kwrd">Me</span>.AxWindowsMediaPlayer1.settings.autoStart = <span class="kwrd">False</span>                     <span class="rem">'設定不自動撥放</span></pre>
		<pre class="alt">
		<span class="kwrd">Me</span>.tbarVolume.Minimum = 0                                               <span class="rem">'設定音量調整Bar最小值為最小音量值(0)</span></pre>
		<pre>
		<span class="kwrd">Me</span>.tbarVolume.Maximum = 100                                             <span class="rem">'設定音量調整Bar最大值為最大音量值(100)</span></pre>
		<pre class="alt">
		<span class="kwrd">Me</span>.tbarVolume.Value = <span class="kwrd">Me</span>.AxWindowsMediaPlayer1.settings.volume          <span class="rem">'設定音量調整Bar目前值為目前音量值</span></pre>
		<pre>
		<span class="kwrd">Me</span>.Timer1.Enabled = <span class="kwrd">True</span></pre>
		<pre class="alt">
		<span class="kwrd">End</span> Sub</pre>
	</div>
</div>
<p>
	 </p>
<p>
	C#</p>
<div style="width: 767px; height: 156px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">private</span> <span class="kwrd">void</span> Form1_Load(<span class="kwrd">object</span> sender, EventArgs e)</pre>
		<pre>
		{</pre>
		<pre class="alt">
		<span class="kwrd">this</span>.axWindowsMediaPlayer1.settings.autoStart = <span class="kwrd">false</span>;                     <span class="rem">//設定不自動撥放</span></pre>
		<pre>
		<span class="kwrd">this</span>.tbarVolume.Minimum = 0;                                               <span class="rem">//設定音量調整Bar最小值為最小音量值(0)</span></pre>
		<pre class="alt">
		<span class="kwrd">this</span>.tbarVolume.Maximum = 100;                                             <span class="rem">//設定音量調整Bar最大值為最大音量值(100)</span></pre>
		<pre>
		<span class="kwrd">this</span>.tbarVolume.Value = <span class="kwrd">this</span>.axWindowsMediaPlayer1.settings.volume;        <span class="rem">//設定音量調整Bar目前值為目前音量值</span></pre>
		<pre class="alt">
		<span class="kwrd">this</span>.timer1.Enabled = <span class="kwrd">true</span>;</pre>
		<pre>
		}</pre>
	</div>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	 </p>
<p>
	 </p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[

.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	<strong>Step4.</strong>撰寫開啟程式碼</p>
<p>
	AxWindowsMediaPlayer控制項是去設定AxWindowsMediaPlayer.URL屬性值來達到多媒體檔案開啟的功能。</p>
<p>
	VB.NET</p>
<div style="width: 769px; height: 119px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> btnOpen_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> btnOpen.Click</pre>
		<pre>
		<span class="kwrd">If</span> OpenFileDialog1.ShowDialog = Windows.Forms.DialogResult.OK <span class="kwrd">Then</span></pre>
		<pre class="alt">
		<span class="kwrd">Me</span>.AxWindowsMediaPlayer1.URL = OpenFileDialog1.FileName                                     <span class="rem">'開啟檔案</span></pre>
		<pre>
		<span class="kwrd">End</span> <span class="kwrd">If</span></pre>
		<pre class="alt">
		<span class="kwrd">End</span> Sub</pre>
	</div>
</div>
<p>
	 </p>
<p>
	C#</p>
<div style="width: 772px; height: 152px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">private</span> <span class="kwrd">void</span> btnOpen_Click(<span class="kwrd">object</span> sender, EventArgs e)</pre>
		<pre>
		{</pre>
		<pre class="alt">
		<span class="kwrd">if</span> (openFileDialog1.ShowDialog() == DialogResult.OK)</pre>
		<pre>
		{</pre>
		<pre class="alt">
		<span class="kwrd">this</span>.axWindowsMediaPlayer1.URL = openFileDialog1.FileName;             <span class="rem">//開啟檔案</span></pre>
		<pre>
		}</pre>
		<pre class="alt">
		}</pre>
	</div>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	 </p>
<p>
	 </p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[



.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	<strong>Step5.</strong>撰寫撥放程式碼</p>
<p>
	這部份功能程式碼只需呼叫AxWindowsMediaPlayer.Ctlcontrols.play()即可。</p>
<p>
	VB.NET</p>
<div style="width: 767px; height: 83px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> btnPlay_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> btnPlay.Click</pre>
		<pre>
		<span class="kwrd">Me</span>.AxWindowsMediaPlayer1.Ctlcontrols.play()</pre>
		<pre class="alt">
		<span class="kwrd">End</span> Sub</pre>
	</div>
</div>
<p>
	 </p>
<p>
	C#</p>
<div style="width: 766px; height: 81px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">private</span> <span class="kwrd">void</span> btnPlay_Click(<span class="kwrd">object</span> sender, EventArgs e)</pre>
		<pre>
		{</pre>
		<pre class="alt">
		<span class="kwrd">this</span>.axWindowsMediaPlayer1.Ctlcontrols.play();</pre>
		<pre>
		}</pre>
	</div>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	 </p>
<p>
	<strong>Step6.</strong>撰寫停止程式碼</p>
<p>
	這部份功能程式碼只需呼叫AxWindowsMediaPlayer.Ctlcontrols.stop()即可。</p>
<p>
	VB.NET</p>
<div style="width: 766px; height: 88px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> btnStop_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> btnStop.Click</pre>
		<pre>
		<span class="kwrd">Me</span>.AxWindowsMediaPlayer1.Ctlcontrols.<span class="kwrd">stop</span>()         <span class="rem">'停止播放</span></pre>
		<pre class="alt">
		<span class="kwrd">End</span> Sub</pre>
	</div>
</div>
<p>
	 </p>
<p>
	C#</p>
<p>
	 </p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[

.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<div style="width: 764px; height: 85px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">private</span> <span class="kwrd">void</span> btnStop_Click(<span class="kwrd">object</span> sender, EventArgs e)</pre>
		<pre>
		{</pre>
		<pre class="alt">
		<span class="kwrd">this</span>.axWindowsMediaPlayer1.Ctlcontrols.stop();         <span class="rem">//停止播放</span></pre>
		<pre>
		}</pre>
	</div>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	 </p>
<p>
	<strong>Step7.</strong>撰寫暫停撥放程式碼</p>
<p>
	這部份功能程式碼只需呼叫AxWindowsMediaPlayer.Ctlcontrols.pause()即可。</p>
<p>
	VB.NET</p>
<div style="width: 765px; height: 90px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> btnPause_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> btnPause.Click</pre>
		<pre>
		<span class="kwrd">Me</span>.AxWindowsMediaPlayer1.Ctlcontrols.pause()        <span class="rem">'暫停撥放</span></pre>
		<pre class="alt">
		<span class="kwrd">End</span> Sub</pre>
	</div>
</div>
<p>
	 </p>
<p>
	C#</p>
<div style="width: 761px; height: 85px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">private</span> <span class="kwrd">void</span> btnPause_Click(<span class="kwrd">object</span> sender, EventArgs e)</pre>
		<pre>
		{</pre>
		<pre class="alt">
		<span class="kwrd">this</span>.axWindowsMediaPlayer1.Ctlcontrols.pause();        <span class="rem">//暫停撥放</span></pre>
		<pre>
		}</pre>
	</div>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	 </p>
<p>
	 </p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[

.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	<strong>Step8.</strong>撰寫音量控制程式碼</p>
<p>
	這部份功能程式碼只需對AxWindowsMediaPlayer.settings.volume做屬性值的變更即可。</p>
<p>
	VB.NET </p>
<p>
	 </p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[



.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<div style="width: 763px; height: 220px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> tbarVolume_Scroll(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> tbarVolume.Scroll</pre>
		<pre>
		<span class="kwrd">Me</span>.AxWindowsMediaPlayer1.settings.volume = <span class="kwrd">Me</span>.tbarVolume.Value      <span class="rem">'改變音量大小</span></pre>
		<pre class="alt">
		<span class="kwrd">End</span> <span class="kwrd">Sub</span></pre>
		<pre>
		 </pre>
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> btnIncreaseVolume_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> btnIncreaseVolume.Click</pre>
		<pre>
		<span class="kwrd">Me</span>.AxWindowsMediaPlayer1.settings.volume += 1       <span class="rem">'音量大小+1</span></pre>
		<pre class="alt">
		<span class="kwrd">End</span> <span class="kwrd">Sub</span></pre>
		<pre>
		 </pre>
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> btnDecreaseVolume_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> btnDecreaseVolume.Click</pre>
		<pre>
		<span class="kwrd">Me</span>.AxWindowsMediaPlayer1.settings.volume -= 1       <span class="rem">'音量大小-1</span></pre>
		<pre class="alt">
		<span class="kwrd">End</span> Sub</pre>
	</div>
</div>
<p>
	 </p>
<p>
	C#</p>
<div style="width: 767px; height: 253px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">private</span> <span class="kwrd">void</span> tbarVolume_Scroll(<span class="kwrd">object</span> sender, EventArgs e)</pre>
		<pre>
		{</pre>
		<pre class="alt">
		<span class="kwrd">this</span>.axWindowsMediaPlayer1.settings.volume = <span class="kwrd">this</span>.tbarVolume.Value;      <span class="rem">//改變音量大小</span></pre>
		<pre>
		}</pre>
		<pre class="alt">
		 </pre>
		<pre>
		<span class="kwrd">private</span> <span class="kwrd">void</span> btnIncreaseVolume_Click(<span class="kwrd">object</span> sender, EventArgs e)</pre>
		<pre class="alt">
		{</pre>
		<pre>
		<span class="kwrd">this</span>.axWindowsMediaPlayer1.settings.volume += 1;       <span class="rem">//音量大小+1</span></pre>
		<pre class="alt">
		}</pre>
		<pre>
		 </pre>
		<pre class="alt">
		<span class="kwrd">private</span> <span class="kwrd">void</span> btnDecreaseVolume_Click(<span class="kwrd">object</span> sender, EventArgs e)</pre>
		<pre>
		{</pre>
		<pre class="alt">
		<span class="kwrd">this</span>.axWindowsMediaPlayer1.settings.volume -= 1;       <span class="rem">//音量大小-1</span></pre>
		<pre>
		}</pre>
	</div>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	 </p>
<p>
	 </p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[

.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	<strong>Step9.</strong>撰寫撥放位置控制程式碼</p>
<p>
	除需對AxWindowsMediaPlayer.Ctlcontrols.currentPosioion做屬性值的變更外，尚需利用AxWindowsMediaPlayer.currentMedia.duration去設定最大影片長度。</p>
<p>
	VB.NET</p>
<div style="width: 761px; height: 185px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> tbarPlayLoaction_Scroll(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> tbarPlayLoaction.Scroll</pre>
		<pre>
		<span class="kwrd">Me</span>.AxWindowsMediaPlayer1.Ctlcontrols.currentPosition = tbarPlayLoaction.Value          <span class="rem">'改變撥放位置</span></pre>
		<pre class="alt">
		<span class="kwrd">End</span> <span class="kwrd">Sub</span></pre>
		<pre>
		 </pre>
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> Timer1_Tick(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Timer1.Tick</pre>
		<pre>
		<span class="kwrd">If</span> <span class="kwrd">Me</span>.AxWindowsMediaPlayer1.currentMedia <span class="kwrd">Is</span> <span class="kwrd">Nothing</span> <span class="kwrd">Then</span></pre>
		<pre class="alt">
		<span class="kwrd">Return</span></pre>
		<pre>
		<span class="kwrd">End</span> <span class="kwrd">If</span></pre>
		<pre class="alt">
		<span class="kwrd">Me</span>.tbarPlayLoaction.Maximum = <span class="kwrd">CInt</span>(<span class="kwrd">Me</span>.AxWindowsMediaPlayer1.currentMedia.duration)          <span class="rem">'設定撥放位置調整Bar最大值</span></pre>
		<pre>
		<span class="kwrd">End</span> Sub</pre>
	</div>
</div>
<p>
	 </p>
<p>
	C#</p>
<div style="width: 760px; height: 233px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">private</span> <span class="kwrd">void</span> tbarPlayLoaction_Scroll(<span class="kwrd">object</span> sender, EventArgs e)</pre>
		<pre>
		{</pre>
		<pre class="alt">
		<span class="kwrd">this</span>.axWindowsMediaPlayer1.Ctlcontrols.currentPosition = tbarPlayLoaction.Value;          <span class="rem">//改變撥放位置</span></pre>
		<pre>
		}</pre>
		<pre class="alt">
		 </pre>
		<pre>
		<span class="kwrd">private</span> <span class="kwrd">void</span> timer1_Tick(<span class="kwrd">object</span> sender, EventArgs e)</pre>
		<pre class="alt">
		{</pre>
		<pre>
		<span class="kwrd">if</span> (<span class="kwrd">this</span>.axWindowsMediaPlayer1.currentMedia == <span class="kwrd">null</span>)</pre>
		<pre class="alt">
		<span class="kwrd">return</span>;</pre>
		<pre>
		<span class="kwrd">this</span>.tbarPlayLoaction.Maximum = (<span class="kwrd">int</span>)<span class="kwrd">this</span>.axWindowsMediaPlayer1.currentMedia.duration;          <span class="rem">//設定撥放位置調整Bar最大值</span></pre>
		<pre class="alt">
		}</pre>
	</div>
</div>
<p>
	  </p>
<h2>
	Download</h2>
<p>
	使用AxWindowsMediaPlayer撥放多媒體.zip</p>
<p>
	 </p>
<h2>
	參考連結</h2>
<ol>
	<li>
		MSDN Library - AxWindowsMediaPlayer Object (VB and C#)</li>
	<li>
		黑色幽默 - AxWindowsMediaPlayer媒体文件主要方法属性</li>
</ol>
