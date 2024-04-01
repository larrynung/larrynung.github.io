---
title: "[WPF]WrapPanel"
date: "2009-05-08 12:32:01"
description: "[WPF]WrapPanel"
tags: [WPF]
---

<h2>Introduction</h2>  <p />  <p>WrapPanel容器跟StackPanel一樣可由上而下或由左而右排列容器內的控制項。不同的是，當超過容器邊緣WrapPanel會自動換行或換列。</p>  <p> </p>  <h2>命名空間 </h2>  <p />  <p>System.Windows.Controls</p>  <p> </p>  <h2>XMLNS</h2>  <p />  <p>http://schemas.microsoft.com/winfx/xaml/presentation </p>  <p> </p>  <h2>Assemble</h2>  <p />  <p />  <p>PresentationFramework (在 PresentationFramework.dll)</p>  <p> </p>  <h2>功能</h2>  <p>將子項目由左至右依序放置，在包含方塊的邊緣將內容換行。依據 Orientation 屬性的值，後續的排列方式會由上至下或由右至左依序進行。</p>  <p> </p>  <h2>範例一</h2>  <div class="csharpcode">   <pre class="alt">&lt;Window x:Class=<span class="str">"Window1"</span></pre>

  <pre>    xmlns=<span class="str">"http://schemas.microsoft.com/winfx/2006/xaml/presentation"</span></pre>

  <pre class="alt">    xmlns:x=<span class="str">"http://schemas.microsoft.com/winfx/2006/xaml"</span></pre>

  <pre>    Title=<span class="str">"Window1"</span> Height=<span class="str">"300"</span> Width=<span class="str">"300"</span>&gt;</pre>

  <pre class="alt">    &lt;WrapPanel Orientation=<span class="str">"Horizontal"</span> ItemHeight=<span class="str">"50"</span> ItemWidth=<span class="str">"70"</span>&gt;</pre>

  <pre>        &lt;Button&gt;按鈕一&lt;/Button&gt;</pre>

  <pre class="alt">        &lt;Button&gt;按鈕二&lt;/Button&gt;</pre>

  <pre>        &lt;Button&gt;按鈕三&lt;/Button&gt;</pre>

  <pre class="alt">        &lt;Button&gt;按鈕四&lt;/Button&gt;</pre>

  <pre>        &lt;Button&gt;按鈕五&lt;/Button&gt;</pre>

  <pre class="alt">    &lt;/WrapPanel&gt;</pre>

  <pre>&lt;/Window&gt;</pre>
</div>

<p> </p>

<p>執行結果</p>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\8353\image_thumb.png" width="304" height="304" /> </p><style type="text/css"><![CDATA[

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

<p> </p>

<h2>範例二</h2>

<div class="csharpcode">
  <pre class="alt"><span class="kwrd">&lt;</span><span class="html">Window</span> <span class="attr">x:Class</span><span class="kwrd">="Window1"</span></pre>

  <pre>    <span class="attr">xmlns</span><span class="kwrd">="http://schemas.microsoft.com/winfx/2006/xaml/presentation"</span></pre>

  <pre class="alt">    <span class="attr">xmlns:x</span><span class="kwrd">="http://schemas.microsoft.com/winfx/2006/xaml"</span></pre>

  <pre>    <span class="attr">Title</span><span class="kwrd">="Window1"</span> <span class="attr">Height</span><span class="kwrd">="300"</span> <span class="attr">Width</span><span class="kwrd">="300"</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt">    <span class="kwrd">&lt;</span><span class="html">WrapPanel</span> <span class="attr">Orientation</span><span class="kwrd">="Vertical"</span>  <span class="attr">ItemHeight</span><span class="kwrd">="50"</span> <span class="attr">ItemWidth</span><span class="kwrd">="70"</span><span class="kwrd">&gt;</span></pre>

  <pre>        <span class="kwrd">&lt;</span><span class="html">Button</span><span class="kwrd">&gt;</span>按鈕一<span class="kwrd">&lt;/</span><span class="html">Button</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt">        <span class="kwrd">&lt;</span><span class="html">Button</span><span class="kwrd">&gt;</span>按鈕二<span class="kwrd">&lt;/</span><span class="html">Button</span><span class="kwrd">&gt;</span></pre>

  <pre>        <span class="kwrd">&lt;</span><span class="html">Button</span><span class="kwrd">&gt;</span>按鈕三<span class="kwrd">&lt;/</span><span class="html">Button</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt">        <span class="kwrd">&lt;</span><span class="html">Button</span><span class="kwrd">&gt;</span>按鈕四<span class="kwrd">&lt;/</span><span class="html">Button</span><span class="kwrd">&gt;</span></pre>

  <pre>        <span class="kwrd">&lt;</span><span class="html">Button</span><span class="kwrd">&gt;</span>按鈕五<span class="kwrd">&lt;/</span><span class="html">Button</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt">    <span class="kwrd">&lt;/</span><span class="html">WrapPanel</span><span class="kwrd">&gt;</span></pre>

  <pre><span class="kwrd">&lt;/</span><span class="html">Window</span><span class="kwrd">&gt;</span></pre>
</div>
<style type="text/css"><![CDATA[

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

<p> </p>

<p>執行結果</p>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\8353\image_thumb_1.png" width="304" height="278" /> </p>

<p> </p>

<h2>範例三</h2>

<div class="csharpcode">
  <pre class="alt"><span class="kwrd">&lt;</span><span class="html">Window</span> <span class="attr">x:Class</span><span class="kwrd">="Window1"</span></pre>

  <pre>    <span class="attr">xmlns</span><span class="kwrd">="http://schemas.microsoft.com/winfx/2006/xaml/presentation"</span></pre>

  <pre class="alt">    <span class="attr">xmlns:x</span><span class="kwrd">="http://schemas.microsoft.com/winfx/2006/xaml"</span></pre>

  <pre>    <span class="attr">Title</span><span class="kwrd">="Window1"</span> <span class="attr">Height</span><span class="kwrd">="300"</span> <span class="attr">Width</span><span class="kwrd">="300"</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt">    <span class="kwrd">&lt;</span><span class="html">WrapPanel</span> <span class="attr">Orientation</span><span class="kwrd">="Vertical"</span> <span class="attr">FlowDirection</span><span class="kwrd">="RightToLeft"</span>  <span class="attr">ItemHeight</span><span class="kwrd">="50"</span> <span class="attr">ItemWidth</span><span class="kwrd">="70"</span><span class="kwrd">&gt;</span></pre>

  <pre>        <span class="kwrd">&lt;</span><span class="html">Button</span><span class="kwrd">&gt;</span>按鈕一<span class="kwrd">&lt;/</span><span class="html">Button</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt">        <span class="kwrd">&lt;</span><span class="html">Button</span><span class="kwrd">&gt;</span>按鈕二<span class="kwrd">&lt;/</span><span class="html">Button</span><span class="kwrd">&gt;</span></pre>

  <pre>        <span class="kwrd">&lt;</span><span class="html">Button</span><span class="kwrd">&gt;</span>按鈕三<span class="kwrd">&lt;/</span><span class="html">Button</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt">        <span class="kwrd">&lt;</span><span class="html">Button</span><span class="kwrd">&gt;</span>按鈕四<span class="kwrd">&lt;/</span><span class="html">Button</span><span class="kwrd">&gt;</span></pre>

  <pre>        <span class="kwrd">&lt;</span><span class="html">Button</span><span class="kwrd">&gt;</span>按鈕五<span class="kwrd">&lt;/</span><span class="html">Button</span><span class="kwrd">&gt;</span></pre>

  <pre class="alt">    <span class="kwrd">&lt;/</span><span class="html">WrapPanel</span><span class="kwrd">&gt;</span></pre>

  <pre><span class="kwrd">&lt;/</span><span class="html">Window</span><span class="kwrd">&gt;</span></pre>
</div>
<style type="text/css"><![CDATA[

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

<p> </p>

<p>執行結果</p>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\8353\image_thumb_2.png" width="304" height="249" /></p>
