---
title: "[VB.NET].NET多語系程式(二)"
date: "2009-04-24 11:57:31"
description: "[VB.NET].NET多語系程式(二)"
tags: [VB.NET]
---

<h2><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="558" height="176" src="\images\posts\8169\image_thumb_8.png" /></a></h2><h2>Introduction</h2><p>本篇將介紹.NET多語系程式的寫法 ，下面會利用資料庫來達到多語系的功能。</p><p> </p><h2>學習目標</h2><ul><li>.NET多語程式撰寫 </li><li>MyDatabase類別庫基本使用</li><li>用資料庫實現多語功能</li></ul><p> </p><h2>操作步驟</h2><p><strong>Step1.首先準備個資料庫，內含所有語系的資料</strong></p><p><a href="http://files.dotblogs.com.tw/larrynung/0904/005c03e830cc.NET_11B68/image_6.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="530" height="349" src="\images\posts\8169\image_thumb_2.png" /></a></p><p><a href="http://files.dotblogs.com.tw/larrynung/0904/005c03e830cc.NET_11B68/image_4.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="427" height="287" src="\images\posts\8169\image_thumb_1.png" /></p><p> </p><p><strong>Step2.切換語系時，從資料庫中抓取對應的顯示字串</strong></p><div style="width: 651px; height: 378px; overflow: auto"><div class="csharpcode"><pre class="alt">
    <span class="kwrd">Dim</span> db <span class="kwrd">As</span> MyDatabase.UseDB.AccessDB</pre><pre>
    <span class="kwrd">Dim</span> dt <span class="kwrd">As</span> DataTable</pre><pre class="alt">
 </pre><pre>
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Form1_Load(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> <span class="kwrd">MyBase</span>.Load</pre><pre class="alt">
        db = <span class="kwrd">New</span> MyDatabase.UseDB.AccessDB(<span class="str">"Language.mdb"</span>)</pre><pre>
        dt = db.GetDataTable(<span class="str">"Select * from lan"</span>)</pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre>
 </pre><pre class="alt">
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Button1_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Button1.Click</pre><pre>
        <span class="kwrd">Me</span>.Text = dt.<span class="kwrd">Select</span>(<span class="str">"Key='Title_TW'"</span>)(0).Item(<span class="str">"Value"</span>)</pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre>
 </pre><pre class="alt">
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Button2_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Button2.Click</pre><pre>
        <span class="kwrd">Me</span>.Text = dt.<span class="kwrd">Select</span>(<span class="str">"Key='Title_CH'"</span>)(0).Item(<span class="str">"Value"</span>)</pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre>
 </pre><pre class="alt">
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Button3_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Button3.Click</pre><pre>
        <span class="kwrd">Me</span>.Text = dt.<span class="kwrd">Select</span>(<span class="str">"Key='Title_EN'"</span>)(0).Item(<span class="str">"Value"</span>)</pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre>
 </pre><pre class="alt">
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Button4_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Button4.Click</pre><pre>
        <span class="kwrd">Me</span>.Text = dt.<span class="kwrd">Select</span>(<span class="str">"Key='Title_JP'"</span>)(0).Item(<span class="str">"Value"</span>)</pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre>
 </pre><pre class="alt">
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Button5_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Button5.Click</pre><pre>
        <span class="kwrd">Me</span>.Text = dt.<span class="kwrd">Select</span>(<span class="str">"Key='Title_K'"</span>)(0).Item(<span class="str">"Value"</span>)</pre><pre class="alt">
    <span class="kwrd">End</span> Sub</pre></div></div><p /><style type="text/css"><![CDATA[

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
.csharpcode .lnum { color: #606060; }]]></style><p> </p><p>到此一個多語程式就完成了，執行效果如下：</p><p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="304" height="304" src="\images\posts\8169\image_thumb_3.png" /></a> <a href="http://files.dotblogs.com.tw/larrynung/0904/005c03e830cc.NET_11B68/image_10.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="304" height="304" src="\images\posts\8169\image_thumb_4.png" /></a></p><p><a href="http://files.dotblogs.com.tw/larrynung/0904/005c03e830cc.NET_11B68/image_12.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="304" height="304" src="\images\posts\8169\image_thumb_5.png" /></a> <a href="http://files.dotblogs.com.tw/larrynung/0904/005c03e830cc.NET_11B68/image_14.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="304" height="304" src="\images\posts\8169\image_thumb_6.png" /></a></p><p><a href="http://files.dotblogs.com.tw/larrynung/0904/005c03e830cc.NET_11B68/image_16.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="304" height="304" src="\images\posts\8169\image_thumb_7.png" /></a> </p><p><a href="http://files.dotblogs.com.tw/larrynung/0904/005c03e830cc.NET_11B68/image_22.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="592" height="327" src="\images\posts\8169\image_thumb.png" /></p>
