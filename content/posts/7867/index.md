---
title: "[.NET Concept][VB.NET]MDI子視窗放大時的注意事項"
date: "2009-04-04 11:51:10"
description: "[.NET Concept][VB.NET]MDI子視窗放大時的注意事項"
tags: [.NET Concept,VB.NET]
---

<p>開發MDI程式時，若需要一開始就放大子視窗，有些地方需特別留意。</p><p>這問題是同事在寫VC++.NET時發現的，本來以為是VC++.NET才會發生。剛試了一下，其它語言像是VB.NET也會有此現象。</p><p>讓我們跟著下面步驟來看一下：</p><p><strong>Step1.把MDI主表單設計成大概如下圖這樣</strong></p><p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="348" height="347" src="\images\posts\7867\image_thumb.png" /></a></p><p> </p><p><strong>Step2.方案總管加入子視窗表單</strong></p><p><a href="http://files.dotblogs.com.tw/larrynung/0904/MDI_15DF/image_4.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="140" height="58" src="\images\posts\7867\image_thumb_1.png" /></a></p><p> </p><p><strong>Step3.子視窗表單的WindwoState屬性設為Maximized</strong></p><p><a href="http://files.dotblogs.com.tw/larrynung/0904/MDI_15DF/image_6.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="280" height="451" src="\images\posts\7867\image_thumb_2.png" /></p><p> </p><p><strong>Step4.在MDI主表單工具列上的按鈕點兩下，並在處理函式內加入下列的Code</strong></p><div class="csharpcode"><pre class="alt"><span class="kwrd">Dim</span> f <span class="kwrd">As</span> <span class="kwrd">New</span> Form2</pre><pre>
f.MdiParent = <span class="kwrd">Me</span></pre><pre class="alt">
f.Show()</pre></div><p /><style type="text/css"><![CDATA[
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
.csharpcode .lnum { color: #606060; }]]></style><p> </p><p><strong>Step5.執行</strong></p><p>點選工具列上按鈕兩下，會看到有怪現象發生。可以從下圖看到表單介面已有最大化的跡象，但是子視窗卻無最大化的效果。</p><p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="596" height="405" src="\images\posts\7867\image_thumb_3.png" /></p><p> </p><h2>如何避免</h2><p>要避免該現象的發生，在子表單中不要設定WindowState屬性，而改用程式碼在Show之前設定。</p><div class="csharpcode"><pre class="alt"><span class="kwrd">Dim</span> f <span class="kwrd">As</span> <span class="kwrd">New</span> Form2</pre><pre>
f.MdiParent = <span class="kwrd">Me</span></pre><pre class="alt">
f.WindowState = FormWindowState.Maximized</pre><pre>
f.Show()</pre></div><p /><style type="text/css"><![CDATA[
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
