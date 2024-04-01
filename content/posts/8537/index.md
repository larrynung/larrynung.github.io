---
title: "[VB.NET]即時座標交叉線條"
date: "2009-05-23 09:36:39"
description: "[VB.NET]即時座標交叉線條"
tags: [VB.NET]
---

<p>在小鋪看到個網友發問個問題，希望能夠在滑鼠座標所在點畫上座標交叉線條。大概效果如下：</p><p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="304" height="304" src="\images\posts\8537\image3_thumb.png" /></a>  <a href="http://files.dotblogs.com.tw/larrynung/0905/b0c8882562a5_12ECD/image12.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="304" height="304" src="\images\posts\8537\image12_thumb.png" /></p><p> </p><p>這效果其實很容易就可以達到，隨手紀錄一下。</p><p> </p><h2>範例程式一</h2><div style="width: 609px; height: 305px; overflow: auto"><div class="csharpcode"><pre class="alt"><span class="kwrd">Public</span> <span class="kwrd">Class</span> Form1</pre><pre>
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Form1_MouseMove(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.Windows.Forms.MouseEventArgs) <span class="kwrd">Handles</span> <span class="kwrd">MyBase</span>.MouseMove</pre><pre class="alt">
        <span class="kwrd">Me</span>.Invalidate()</pre><pre>
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre class="alt">
 </pre><pre>
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Form1_Paint(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> <span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.Windows.Forms.PaintEventArgs) <span class="kwrd">Handles</span> <span class="kwrd">Me</span>.Paint</pre><pre class="alt">
        <span class="kwrd">Dim</span> x <span class="kwrd">As</span> <span class="kwrd">Integer</span> </pre><pre>
        <span class="kwrd">Dim</span> y <span class="kwrd">As</span> <span class="kwrd">Integer</span></pre><pre class="alt">
        <span class="kwrd">With</span> PointToClient(MousePosition)</pre><pre>
            x = .X</pre><pre class="alt">
            y = .Y</pre><pre>
        <span class="kwrd">End</span> <span class="kwrd">With</span></pre><pre class="alt">
        <span class="kwrd">With</span> e.Graphics</pre><pre>
            .DrawLine(Pens.Black, 0, y, <span class="kwrd">Me</span>.Width, y)</pre><pre class="alt">
            .DrawLine(Pens.Black, x, 0, x, <span class="kwrd">Me</span>.Height)</pre><pre>
        <span class="kwrd">End</span> <span class="kwrd">With</span></pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre><span class="kwrd">End</span> Class</pre></div></div><p> </p><h2>範例程式二</h2><div style="width: 611px; height: 378px; overflow: auto"><div class="csharpcode"><pre class="alt"><span class="kwrd">Public</span> <span class="kwrd">Class</span> Form1</pre><pre>
    <span class="kwrd">Dim</span> g <span class="kwrd">As</span> Graphics</pre><pre class="alt">
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Form1_MouseMove(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.Windows.Forms.MouseEventArgs) <span class="kwrd">Handles</span> <span class="kwrd">MyBase</span>.MouseMove</pre><pre>
        <span class="kwrd">Dim</span> point <span class="kwrd">As</span> Point = PointToClient(MousePosition)</pre><pre class="alt">
        <span class="kwrd">Dim</span> x <span class="kwrd">As</span> <span class="kwrd">Integer</span> = point.X</pre><pre>
        <span class="kwrd">Dim</span> y <span class="kwrd">As</span> <span class="kwrd">Integer</span> = point.Y</pre><pre class="alt">
        g.Clear(<span class="kwrd">Me</span>.BackColor)</pre><pre>
        g.DrawLine(Pens.Black, 0, y, <span class="kwrd">Me</span>.Width, y)</pre><pre class="alt">
        g.DrawLine(Pens.Black, x, 0, x, <span class="kwrd">Me</span>.Height)</pre><pre>
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre class="alt">
 </pre><pre>
    <span class="kwrd">Public</span> <span class="kwrd">Sub</span> <span class="kwrd">New</span>()</pre><pre class="alt">
 </pre><pre>
        <span class="rem">' 此為 Windows Form 設計工具所需的呼叫。 </span></pre><pre class="alt">
        InitializeComponent()</pre><pre>
 </pre><pre class="alt">
        <span class="rem">' 在 InitializeComponent() 呼叫之後加入任何初始設定。 </span></pre><pre>
 </pre><pre class="alt">
        g = <span class="kwrd">Me</span>.CreateGraphics</pre><pre>
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre class="alt"><span class="kwrd">End</span> Class</pre></div></div><p> </p><h2>相關連結</h2><ul><li>藍色小鋪-(VB.NET 2003)請問要如何在表單內畫出即時線條?</li></ul>
