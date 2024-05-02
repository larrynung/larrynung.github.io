---
title: "[WPF]DockPanel"
date: "2009-05-08 12:30:45"
description: "[WPF]DockPanel"
tags: [WPF]
---

<h2>Introduction</h2>  <p />  <p>DockPanel容器主要為容器內部的控制項提供停靠的機制。</p>  <p> </p>  <h2>命名空間 </h2>  <p />  <p>System.Windows.Controls</p>  <p> </p>  <h2>XMLNS</h2>  <p />  <p>http://schemas.microsoft.com/winfx/xaml/presentation</p>  <p> </p>  <h2>Assemble</h2>  <p />  <p />  <p>PresentationFramework (在 PresentationFramework.dll)</p>  <p> </p>  <h2>功能</h2>  <p>定義一個區域，讓子項目可以依彼此相對的水平或垂直位置來排列。</p>  <p> </p>  <h2>範例</h2>  <div style="width: 637px; height: 344px; overflow: auto">   <div class="csharpcode">     <pre class="alt"><span class="kwrd">&lt;</span><span class="html">Window</span> <span class="attr">x:Class</span><span class="kwrd">="Window1"</span></pre>

    <pre>    <span class="attr">xmlns</span><span class="kwrd">="http://schemas.microsoft.com/winfx/2006/xaml/presentation"</span></pre>

    <pre class="alt">    <span class="attr">xmlns:x</span><span class="kwrd">="http://schemas.microsoft.com/winfx/2006/xaml"</span></pre>

    <pre>    <span class="attr">Title</span><span class="kwrd">="Window1"</span> <span class="attr">Height</span><span class="kwrd">="300"</span> <span class="attr">Width</span><span class="kwrd">="300"</span><span class="kwrd">&gt;</span></pre>

    <pre class="alt">    <span class="kwrd">&lt;</span><span class="html">DockPanel</span> <span class="attr">Height</span><span class="kwrd">="263"</span> <span class="attr">Name</span><span class="kwrd">="DockPanel1"</span> <span class="attr">Width</span><span class="kwrd">="276"</span><span class="kwrd">&gt;</span></pre>

    <pre>        <span class="kwrd">&lt;</span><span class="html">Menu</span> <span class="attr">DockPanel</span>.<span class="attr">Dock</span><span class="kwrd">="Top"</span> <span class="kwrd">&gt;</span></pre>

    <pre class="alt">            <span class="kwrd">&lt;</span><span class="html">MenuItem</span> <span class="attr">Header</span><span class="kwrd">="File"</span><span class="kwrd">&gt;</span></pre>

    <pre>                <span class="kwrd">&lt;</span><span class="html">MenuItem</span> <span class="attr">Header</span><span class="kwrd">="Open"</span><span class="kwrd">&gt;&lt;/</span><span class="html">MenuItem</span><span class="kwrd">&gt;</span></pre>

    <pre class="alt">            <span class="kwrd">&lt;/</span><span class="html">MenuItem</span><span class="kwrd">&gt;</span></pre>

    <pre>        <span class="kwrd">&lt;/</span><span class="html">Menu</span><span class="kwrd">&gt;</span></pre>

    <pre class="alt">        </pre>

    <pre>        <span class="kwrd">&lt;</span><span class="html">ToolBarPanel</span> <span class="attr">DockPanel</span>.<span class="attr">Dock</span><span class="kwrd">="Top"</span><span class="kwrd">&gt;</span></pre>

    <pre class="alt">            <span class="kwrd">&lt;</span><span class="html">Button</span> <span class="attr">HorizontalAlignment</span><span class="kwrd">="Left"</span> <span class="kwrd">&gt;</span>Tool<span class="kwrd">&lt;/</span><span class="html">Button</span><span class="kwrd">&gt;</span></pre>

    <pre>        <span class="kwrd">&lt;/</span><span class="html">ToolBarPanel</span><span class="kwrd">&gt;</span></pre>

    <pre class="alt">        </pre>

    <pre>        <span class="kwrd">&lt;</span><span class="html">StackPanel</span> <span class="attr">Width</span><span class="kwrd">="150"</span> <span class="attr">Background</span><span class="kwrd">="Yellow"</span>   <span class="attr">DockPanel</span>.<span class="attr">Dock</span><span class="kwrd">="Left"</span><span class="kwrd">&gt;</span></pre>

    <pre class="alt">            <span class="kwrd">&lt;</span><span class="html">TextBlock</span> <span class="attr">Background</span><span class="kwrd">="Gray"</span><span class="kwrd">&gt;</span>Tool1<span class="kwrd">&lt;/</span><span class="html">TextBlock</span><span class="kwrd">&gt;</span></pre>

    <pre>            <span class="kwrd">&lt;</span><span class="html">TextBlock</span> <span class="attr">Background</span><span class="kwrd">="Aqua"</span><span class="kwrd">&gt;</span>Tool2<span class="kwrd">&lt;/</span><span class="html">TextBlock</span><span class="kwrd">&gt;</span></pre>

    <pre class="alt">        <span class="kwrd">&lt;/</span><span class="html">StackPanel</span><span class="kwrd">&gt;</span></pre>

    <pre>        </pre>

    <pre class="alt">        <span class="kwrd">&lt;</span><span class="html">StackPanel</span> <span class="attr">Width</span><span class="kwrd">="150"</span> <span class="attr">DockPanel</span>.<span class="attr">Dock</span><span class="kwrd">="Left"</span><span class="kwrd">&gt;</span></pre>

    <pre>        <span class="kwrd">&lt;/</span><span class="html">StackPanel</span><span class="kwrd">&gt;</span></pre>

    <pre class="alt">        </pre>

    <pre>    <span class="kwrd">&lt;/</span><span class="html">DockPanel</span><span class="kwrd">&gt;</span></pre>

    <pre class="alt"><span class="kwrd">&lt;/</span><span class="html">Window</span><span class="kwrd">&gt;</span></pre>
  </div>
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

<p>執行結果 </p>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\8350\image_thumb.png" width="304" height="304" /></p>
