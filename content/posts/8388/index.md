---
title: "[WPF]TextBlock"
date: "2009-05-12 05:44:57"
description: "[WPF]TextBlock"
tags: [WPF]
---

<h2>命名空間 </h2>  <p />  <p>System.Windows.Controls</p>  <p> </p>  <h2>XMLNS</h2>  <p />  <p>http://schemas.microsoft.com/winfx/xaml/presentation </p>  <p> </p>  <h2>Assemble</h2>  <p />  <p />  <p>PresentationFramework (在 PresentationFramework.dll) </p>  <p> </p>  <h2>功能</h2>  <p>提供輕量控制項，以顯示少量的非固定格式內容。</p>  <p> </p>  <h2>範例</h2>  <div class="csharpcode">   <pre class="alt"><span class="kwrd">&lt;</span><span class="html">Window</span> <span class="attr">x:Class</span><span class="kwrd">="Window1"</span></pre>

  <pre>    <span class="attr">xmlns</span><span class="kwrd">="http://schemas.microsoft.com/winfx/2006/xaml/presentation"</span></pre>

  <pre class="alt">    <span class="attr">xmlns:x</span><span class="kwrd">="http://schemas.microsoft.com/winfx/2006/xaml"</span></pre>

  <pre>    <span class="attr">Title</span><span class="kwrd">="Window1"</span> <span class="attr">Height</span><span class="kwrd">="300"</span> <span class="attr">Width</span><span class="kwrd">="300"</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt">    <span class="kwrd">&lt;</span><span class="html">Grid</span><span class="kwrd">&gt;</span></pre>

  <pre>        <span class="kwrd">&lt;</span><span class="html">TextBlock</span> <span class="attr">TextWrapping</span><span class="kwrd">="Wrap"</span> <span class="attr">Height</span><span class="kwrd">="262"</span> <span class="attr">VerticalAlignment</span><span class="kwrd">="top"</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt">            <span class="kwrd">&lt;</span><span class="html">Button</span><span class="kwrd">&gt;</span>Button<span class="kwrd">&lt;/</span><span class="html">Button</span><span class="kwrd">&gt;</span></pre>

  <pre>            Normal</pre>

  <pre class="alt">            <span class="kwrd">&lt;</span><span class="html">Bold</span><span class="kwrd">&gt;</span>Bold<span class="kwrd">&lt;/</span><span class="html">Bold</span><span class="kwrd">&gt;</span> </pre>

  <pre>            <span class="kwrd">&lt;</span><span class="html">Hyperlink</span><span class="kwrd">&gt;</span>Hyperlink<span class="kwrd">&lt;/</span><span class="html">Hyperlink</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt">            <span class="kwrd">&lt;</span><span class="html">Italic</span><span class="kwrd">&gt;</span>Italic<span class="kwrd">&lt;/</span><span class="html">Italic</span><span class="kwrd">&gt;</span></pre>

  <pre>            <span class="kwrd">&lt;</span><span class="html">Underline</span><span class="kwrd">&gt;</span>Underline<span class="kwrd">&lt;/</span><span class="html">Underline</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt">        <span class="kwrd">&lt;/</span><span class="html">TextBlock</span><span class="kwrd">&gt;</span></pre>

  <pre>    <span class="kwrd">&lt;/</span><span class="html">Grid</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt"><span class="kwrd">&lt;/</span><span class="html">Window</span><span class="kwrd">&gt;</span></pre>
</div>

<p /><style type="text/css"><![CDATA[

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

<p>執行結果</p>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\8388\image_thumb.png" width="304" height="304" /></p>
