---
title: "[C#][VB.NET]GC.Collect()造成的怪現象"
slug: "[CSharp][VB.NET]GC.Collect()造成的怪現象"
date: "2009-01-30 10:48:06"
description: "[C#][VB.NET]GC.Collect()造成的怪現象"
tags: [CSharp,VB.NET]
---

<h2>Abstract</h2><ul><li>Introduction</li><li>Example</li><li>Conclusion</li><li>Download</li></ul><p> </p><h2>Introduction</h2><p>前一陣子在用同事程式時，總覺得速度有點慢，但卻不知道問題出在哪個同事的Code，因此針對底層同事的程式做了效率上面的測試。測試的結果是，當拿同事的類別來用時，若只建立並使用一次，則其效能不差。但若用迴圈去建立並使用多次時，其效能就變的十分的低落。</p><p>當我把我測出的情況告知同事後，同事也用相同的方法測了一遍，但是在他的電腦上卻看不到效能變差的跡象。相同的程式，不同的電腦，跑出不同的結果，然而其中的差異又不像是電腦速度差異所造成的。研究了老半天，才發現此差異是出在我拿正在開發的產品專案來測試，介面較為複雜，控制項使用的較多。而同事則是開他的測試用專案，沒有啥麼介面。</p><p>雖然發現了造成差異的點，但是若自己寫的類別會因介面上控制項的多寡而造成效能上的影響亦是一件怪事，最後才發現原來一切都是因為GC.Collect()造成的，同事的程式寫了很多GC.Collect()想要回收記憶體。卻意外的造成此怪現象的產生。</p><p>此現象應是由於GC回收資源時會針對目前使用到的物件下去回收，所以記憶體中使用的物件越多執行速度就越慢。而由於程式內部有許多地方有呼叫到GC.Collect()，因此程式的執行速度連帶也會受到GC回收速度影響。</p><p> </p><h2>Example</h2><p>舉個例子來說，假設今天有個Data的類別寫法如下：</p><p>VB.NET</p><div class="csharpcode"><pre class="alt"><span class="kwrd">Public</span> <span class="kwrd">Class</span> Data</pre><pre>
...</pre><pre class="alt">
    <span class="kwrd">Public</span> <span class="kwrd">Sub</span> SetValue(<span class="kwrd">ByVal</span> val <span class="kwrd">As</span> <span class="kwrd">Object</span>)</pre><pre>
        _val = val</pre><pre class="alt">
        GC.Collect()</pre><pre>
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre class="alt">
...</pre><pre><span class="kwrd">End</span> <span class="kwrd">Class</span></pre></div><p> </p><p> </p><p /><style type="text/css"><![CDATA[
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
.csharpcode .lnum { color: #606060; }]]></style><p>C#</p><pre class="csharpcode"><span class="kwrd">class</span> Data
{
...
<span class="kwrd">public</span> <span class="kwrd">void</span> SetValue(Object val)
{
    _val = val;
    GC.Collect();
}
...
}</pre><p> </p><p> </p><p /><style type="text/css"><![CDATA[
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
.csharpcode .lnum { color: #606060; }]]></style><p>則下列這段Code的執行結果，將會依據介面上控制項的多寡而定。</p><p>VB.NET</p><div class="csharpcode"><pre class="alt">
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Button1_Click_1(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Button1.Click</pre><pre>
        <span class="kwrd">Me</span>.Button1.Enabled = <span class="kwrd">False</span></pre><pre class="alt">
        <span class="kwrd">Dim</span> sw <span class="kwrd">As</span> Stopwatch = Stopwatch.StartNew</pre><pre>
        <span class="kwrd">For</span> i <span class="kwrd">As</span> <span class="kwrd">Integer</span> = 1 <span class="kwrd">To</span> 1000</pre><pre class="alt">
            <span class="kwrd">Dim</span> d <span class="kwrd">As</span> <span class="kwrd">New</span> Data</pre><pre>
            d.SetValue(<span class="str">"test"</span>)</pre><pre class="alt">
        <span class="kwrd">Next</span></pre><pre>
        <span class="kwrd">Me</span>.TextBox1.Text = <span class="kwrd">String</span>.Format(<span class="str">"花費時間: {0} ms"</span>, sw.ElapsedMilliseconds.ToString)</pre><pre class="alt">
        <span class="kwrd">Me</span>.Button1.Enabled = <span class="kwrd">True</span></pre><pre>
    <span class="kwrd">End</span> Sub </pre></div><p> </p><p> </p><p /><style type="text/css"><![CDATA[
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
.csharpcode .lnum { color: #606060; }]]></style><p>C#</p><pre class="csharpcode"><span class="kwrd">private</span> <span class="kwrd">void</span> Button1_Click(<span class="kwrd">object</span> sender, EventArgs e)
{
    <span class="kwrd">this</span>.Button1.Enabled = <span class="kwrd">false</span>;
    Stopwatch  sw = Stopwatch.StartNew();
    <span class="kwrd">for</span> (<span class="kwrd">int</span> i = 1; i &lt;= 1000; i++)
    {
        Data d = <span class="kwrd">new</span> Data();
        d.SetValue(<span class="str">"test"</span>);
    }
    <span class="kwrd">this</span>.TextBox1.Text = String.Format(<span class="str">"花費時間: {0} ms"</span>, sw.ElapsedMilliseconds.ToString());
    <span class="kwrd">this</span>.Button1.Enabled = <span class="kwrd">true</span>;
}</pre><p> </p><p> </p><p /><style type="text/css"><![CDATA[
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
.csharpcode .lnum { color: #606060; }]]></style><p>執行結果如下:</p><p> </p><p /><style type="text/css"><![CDATA[
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
.csharpcode .lnum { color: #606060; }]]></style><p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="558" height="304" src="\images\posts\6985\image_thumb.png" /></a></p><p><a href="http://files.dotblogs.com.tw/larrynung/0901/GC.Collect_13B0D/image_4.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="558" height="304" src="\images\posts\6985\image_thumb_1.png" /></a></p><p><a href="http://files.dotblogs.com.tw/larrynung/0901/GC.Collect_13B0D/image_6.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="558" height="304" src="\images\posts\6985\image_thumb_2.png" /></a></p><p> </p><h2>Conclusion</h2><p>一般說來，若非必要普遍都不建議程式設計師下GC.Collect，但畢竟是開出來的函式，仍是不能避免有人會使用GC.Collect，因此我們必須要了解使用GC.Collect可能會產生的現象與濫用的徵兆(執行效能會因控制項或是記憶體中的物件量而變化)，碰到這類問題時才能發現問題的所在。</p><p> </p><h2>Download</h2><p><a href="http://Files.Dotblogs.com.tw/larrynung/0901/2009130225417553.zip">TestGC.zip</p>
