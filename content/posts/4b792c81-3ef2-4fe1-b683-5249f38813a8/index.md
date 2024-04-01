---
title: "[C#]BigInteger"
date: "2013-11-06 12:00:00"
description: "[C#]BigInteger"
---

<p>
	今天看書才知道原本.NET 3.5中偷藏了一個BinInteger類型，可用來顯示很長的整數。該類型在.NET Framework 3.5 Beta1中就已被加入,但是Release版中該類型被改為Internal類型，導致無法直接使用。根據網路上的資料顯示，據說是微軟認為該類型還有很多問題，因此暫不開放。但我們仍可透過.NET反射機制去使用它。</p>
<p>
	 </p>
<p>
	簡易範例如下：</p>
<div style="overflow: auto; width: 844px; height: 311px">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">using</span> System;</pre>
		<pre>
		<span class="kwrd">using</span> System.Collections.Generic;</pre>
		<pre class="alt">
		<span class="kwrd">using</span> System.Linq;</pre>
		<pre>
		<span class="kwrd">using</span> System.Text;</pre>
		<pre class="alt">
		<span class="kwrd">using</span> System.Reflection;</pre>
		<pre>
		 </pre>
		<pre class="alt">
		<span class="kwrd">namespace</span> ConsoleApplication5</pre>
		<pre>
		{</pre>
		<pre class="alt">
		<span class="kwrd">class</span> Program</pre>
		<pre>
		{</pre>
		<pre class="alt">
		<span class="kwrd">static</span> <span class="kwrd">void</span> Main(<span class="kwrd">string</span>[] args)</pre>
		<pre>
		{            </pre>
		<pre class="alt">
		Type type = Assembly.LoadWithPartialName(<span class="str">"System.Core"</span>).GetType(<span class="str">"System.Numeric.BigInteger"</span>);</pre>
		<pre>
		Object o1 = Activator.CreateInstance(type, <span class="kwrd">double</span>.MaxValue);</pre>
		<pre class="alt">
		Object o2 = Activator.CreateInstance(type, <span class="kwrd">double</span>.MaxValue);</pre>
		<pre>
		MethodInfo m = type.GetMethod(<span class="str">"Add"</span>, BindingFlags.Public | BindingFlags.Static);</pre>
		<pre class="alt">
		Console.WriteLine(m.Invoke (<span class="kwrd">null</span>,<span class="kwrd">new</span> <span class="kwrd">object</span> []{o1,o2}));    </pre>
		<pre>
		}</pre>
		<pre class="alt">
		}</pre>
		<pre>
		}</pre>
	</div>
</div>
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
	執行結果如下：</p>
<p>
	<img alt="image" border="0" height="442" src="\images\posts\4b792c81-3ef2-4fe1-b683-5249f38813a8\image_thumb.png" style="border-right: 0px; border-top: 0px; border-left: 0px; border-bottom: 0px" width="673" /></p>
<p>
	 </p>
<h2>
	Conclusion</h2>
<p>
	上網搜了一下，好像直接這樣使用的人並不多。多半是使用自己寫的類別來達到此需求。像是Code Project上這篇。</p>
<p>
	 </p>
<h2>
	相關連結</h2>
<ul>
	<li>
		Code Project-C# BigInteger Class</li>
</ul>
