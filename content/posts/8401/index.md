---
title: "[VB.NET]Lambda運算式"
date: "2009-05-14 08:50:13"
description: "[VB.NET]Lambda運算式"
tags: [VB.NET]
---

<h2>Abstract</h2><ul><li>Introduction</li><li>使用方式</li><li>特色</li><li>呼叫不具回傳值的副程式</li></ul><p> </p><h2>Introduction</h2><p>「Lambda 運算式」(Lambda Expression) 是沒有名稱的函式，會計算並傳回單一值。</p><p> </p><h2>使用方式</h2><p>宣告方式</p><p>Function (參數) 運算式</p><p> </p><p>簡易的宣告範例</p><div class="csharpcode"><pre class="alt"><span class="kwrd">Function</span> (num <span class="kwrd">As</span> <span class="kwrd">Integer</span>) num + 1 </pre></div><p /><style type="text/css"><![CDATA[


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
.csharpcode .lnum { color: #606060; }]]></style><p> </p><p>若要重覆利用呼叫，可以將函式指派為變數名稱。</p><div class="csharpcode"><pre class="alt"><span class="kwrd">Dim</span> add1 = <span class="kwrd">Function</span>(num <span class="kwrd">As</span> <span class="kwrd">Integer</span>) num + 1</pre></div><p> </p><p>要使用時就可以直接叫用。</p><div class="csharpcode"><pre class="alt">
Console.WriteLine(add1(5))</pre></div><p /><style type="text/css"><![CDATA[


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
.csharpcode .lnum { color: #606060; }]]></style><p>或是在宣告時直接叫用。</p><div class="csharpcode"><pre class="alt">
Console.WriteLine((<span class="kwrd">Function</span>(num <span class="kwrd">As</span> <span class="kwrd">Integer</span>) num + 1)(5))</pre></div><p /><style type="text/css"><![CDATA[


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
.csharpcode .lnum { color: #606060; }]]></style><p> </p><h1>特色</h1><ul><li>Lambda 運算式沒有名稱。</li><li><p>Lambda 運算式不能有修飾詞 (Modifier)，例如 Overloads 或 Overrides。</p></li><li><p>Lambda 運算式不會使用 As 子句指定函式的傳回型別。而是從 Lambda 運算式評估之主體的值來推斷型別。例如，如果 Lambda 運算式的主體是 Where cust.City = "London"，其傳回型別為 Boolean。</p></li><li><p>函式的主體必須是運算式，而不是陳述式。主體可以由對函式程序的呼叫組成，但不可由對子程序的呼叫組成。</p></li><li><p>沒有 Return 陳述式。函式傳回的值就是函式主體中運算式的值。</p></li><li><p>沒有 End Function 陳述式。</p></li><li><p>所有參數都必須具有指定的資料型別，不然所有參數就都必須經過推斷。</p></li><li><p>不允許使用 Optional 和 Paramarray 參數。</p></li><li><p>不允許使用泛型參數。</p></li><li><p>只支援單行運算式(C#支援多行運算式)。</p></li><li><p>Lambda 運算式不能直接呼叫不具回傳值的副程式(C#可以)。</p></li></ul><p> </p><h2>呼叫不具回傳值的副程式</h2><p>Lambda 運算式的特點之一就是不能直接呼叫不具回傳值的副程式。其實這也是本篇主要想記載的小技巧。</p><p>我們先來看一下程式碼。</p><p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="408" height="203" src="\images\posts\8401\image_thumb.png" /></a></p><p> </p><p>由上圖可以看出，若在Lambda運算示中欲直接呼叫不具回傳值的副程式，將會產生"運算式沒有產生值"的錯誤。</p><p>那是否就不行叫用不具回傳值的副程式了呢？其實換個想法，若我們可以讓不具回傳值的副程式，透過某些方法，把它變成具有回傳值的函式，那一切不就解決了嗎？</p><p>為此，我們可以透過CallByName函式來達到此需求。</p><p><a href="http://files.dotblogs.com.tw/larrynung/0905/VB.NETLambda_12632/image_4.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="664" height="456" src="\images\posts\8401\image_thumb_1.png" /></p><p> </p><p>完整程式碼如下</p><div style="width: 658px; height: 260px; overflow: auto"><div class="csharpcode"><pre class="alt"><span class="kwrd">Module</span> Module1</pre><pre>
 </pre><pre class="alt">
    <span class="kwrd">Sub</span> Main()</pre><pre>
        <span class="kwrd">Dim</span> obj <span class="kwrd">As</span> <span class="kwrd">New</span> OutputClass</pre><pre class="alt">
        <span class="kwrd">Dim</span> Output = <span class="kwrd">Function</span>(msg <span class="kwrd">As</span> <span class="kwrd">String</span>) CallByName(obj, <span class="str">"WriteLine"</span>, CallType.Method, msg)</pre><pre>
        Output(<span class="str">"Test"</span>)</pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre>
 </pre><pre class="alt"><span class="kwrd">End</span> <span class="kwrd">Module</span></pre><pre>
 </pre><pre class="alt"><span class="kwrd">Class</span> OutputClass</pre><pre>
    <span class="kwrd">public</span> <span class="kwrd">Sub</span> WriteLine(<span class="kwrd">ByVal</span> msg <span class="kwrd">As</span> <span class="kwrd">String</span>)</pre><pre class="alt">
        Console.WriteLine(msg)</pre><pre>
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre class="alt"><span class="kwrd">End</span> Class</pre></div></div><p /><style type="text/css"><![CDATA[


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
.csharpcode .lnum { color: #606060; }]]></style><p> </p><p>執行結果</p><p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="473" height="123" src="\images\posts\8401\image_thumb_2.png" /> </p><p> </p><p>Lambda運算式透過上面的小技巧，已能呼叫不具回傳值的副程式。使用上因此變得更具彈性。如下範例，我們可用Lambda運算式做更多的應用。</p><div style="width: 657px; height: 358px; overflow: auto"><div class="csharpcode"><pre class="alt">
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Button1_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Button1.Click</pre><pre>
        GO()</pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre>
 </pre><pre class="alt">
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> GO()</pre><pre>
        <span class="kwrd">Dim</span> f <span class="kwrd">As</span> <span class="kwrd">New</span> Form</pre><pre class="alt">
        <span class="kwrd">Dim</span> b <span class="kwrd">As</span> <span class="kwrd">New</span> Button</pre><pre>
        <span class="kwrd">Dim</span> lst <span class="kwrd">As</span> <span class="kwrd">New</span> ListBox</pre><pre class="alt">
 </pre><pre>
        <span class="kwrd">With</span> lst</pre><pre class="alt">
            .Items.Add(<span class="str">"Double Click Me"</span>)</pre><pre>
            .Dock = DockStyle.Fill</pre><pre class="alt">
        <span class="kwrd">End</span> <span class="kwrd">With</span></pre><pre>
        <span class="kwrd">AddHandler</span> lst.DoubleClick, <span class="kwrd">Function</span>(sender <span class="kwrd">As</span> <span class="kwrd">Object</span>, e <span class="kwrd">As</span> EventArgs) CallByName(b, <span class="str">"PerformClick"</span>, CallType.Method, <span class="kwrd">Nothing</span>)</pre><pre class="alt">
 </pre><pre>
        <span class="kwrd">With</span> b</pre><pre class="alt">
            .Text = <span class="str">"Ok"</span></pre><pre>
            .DialogResult = Windows.Forms.DialogResult.OK</pre><pre class="alt">
            .Dock = DockStyle.Bottom</pre><pre>
        <span class="kwrd">End</span> <span class="kwrd">With</span></pre><pre class="alt">
        <span class="kwrd">AddHandler</span> b.Click, <span class="kwrd">Function</span>(sender <span class="kwrd">As</span> <span class="kwrd">Object</span>, e <span class="kwrd">As</span> EventArgs) MsgBox(<span class="str">"You Click Me"</span>)</pre><pre>
 </pre><pre class="alt">
        <span class="kwrd">With</span> f</pre><pre>
            .Controls.AddRange(<span class="kwrd">New</span> Control() {lst, b})</pre><pre class="alt">
            .ShowDialog()</pre><pre>
        <span class="kwrd">End</span> <span class="kwrd">With</span></pre><pre class="alt">
    <span class="kwrd">End</span> Sub</pre></div></div><p> </p><p>執行結果</p><p /><style type="text/css"><![CDATA[


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
.csharpcode .lnum { color: #606060; }]]></style><p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="299" height="303" src="\images\posts\8401\image_thumb_3.png" /></p>
