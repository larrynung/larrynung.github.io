---
title: "[C#][VB.NET]彩色圖片轉為黑白圖片"
slug: "[CSharp][VB.NET]彩色圖片轉為黑白圖片"
date: "2009-06-03 09:01:40"
description: "[C#][VB.NET]彩色圖片轉為黑白圖片"
tags: [CSharp,VB.NET]
---

<h2>Introduction</h2><p>本篇的主旨在於介紹如何把圖片轉為黑白照片。欲把彩色圖片轉為黑白圖片，我們可以把圖片上的每個像素都設為灰階值。灰階值的取得可套用下面公式。</p><p><strong>灰階值 = (R+G+B)/3</strong></p><p> </p><h2>範例程式</h2><p>VB.NET</p><div style="width: 613px; height: 337px; overflow: auto"><div class="csharpcode"><pre class="alt"><span class="rem">'|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||</span></pre><pre><span class="rem">'Author: Larry Nung</span></pre><pre class="alt"><span class="rem">'Date: 2009/6/2</span></pre><pre><span class="rem">'File: </span></pre><pre class="alt"><span class="rem">'Memo: </span></pre><pre><span class="rem">'|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||</span></pre><pre class="alt"><span class="rem">''' &lt;summary&gt;</span></pre><pre><span class="rem">''' </span></pre><pre class="alt"><span class="rem">''' &lt;/summary&gt;</span></pre><pre><span class="rem">''' &lt;remarks&gt;&lt;/remarks&gt;</span></pre><pre class="alt"><span class="kwrd">Public</span> <span class="kwrd">Class</span> Form1</pre><pre>
 </pre><pre class="alt">
 </pre><pre>
    <span class="rem">'***************************************************************************</span></pre><pre class="alt">
    <span class="rem">'Author: Larry Nung</span></pre><pre>
    <span class="rem">'Date: 2009/6/2</span></pre><pre class="alt">
    <span class="rem">'Purpose: </span></pre><pre>
    <span class="rem">'Memo: </span></pre><pre class="alt">
    <span class="rem">'***************************************************************************</span></pre><pre>
    <span class="rem">''' &lt;summary&gt;</span></pre><pre class="alt">
    <span class="rem">''' Handles the Click event of the Button1 control.</span></pre><pre>
    <span class="rem">''' &lt;/summary&gt;</span></pre><pre class="alt">
    <span class="rem">''' &lt;param name="sender"&gt;The source of the event.&lt;/param&gt;</span></pre><pre>
    <span class="rem">''' &lt;param name="e"&gt;The &lt;see cref="System.EventArgs" /&gt; instance containing the event data.&lt;/param&gt;</span></pre><pre class="alt">
    <span class="rem">''' &lt;remarks&gt;&lt;/remarks&gt;</span></pre><pre>
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Button1_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Button1.Click</pre><pre class="alt">
        <span class="kwrd">If</span> OpenFileDialog1.ShowDialog = Windows.Forms.DialogResult.OK <span class="kwrd">Then</span></pre><pre>
            <span class="kwrd">Me</span>.PictureBox1.Image = GetGrayBitmap(OpenFileDialog1.FileName)</pre><pre class="alt">
        <span class="kwrd">End</span> <span class="kwrd">If</span></pre><pre>
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre class="alt">
 </pre><pre>
 </pre><pre class="alt">
    <span class="rem">'***************************************************************************</span></pre><pre>
    <span class="rem">'Author: Larry Nung</span></pre><pre class="alt">
    <span class="rem">'Date: 2009/6/2</span></pre><pre>
    <span class="rem">'Purpose: </span></pre><pre class="alt">
    <span class="rem">'Memo: </span></pre><pre>
    <span class="rem">'***************************************************************************</span></pre><pre class="alt">
    <span class="rem">''' &lt;summary&gt;</span></pre><pre>
    <span class="rem">''' Gets the gray image.</span></pre><pre class="alt">
    <span class="rem">''' &lt;/summary&gt;</span></pre><pre>
    <span class="rem">''' &lt;param name="file"&gt;The file.&lt;/param&gt;</span></pre><pre class="alt">
    <span class="rem">''' &lt;returns&gt;&lt;/returns&gt;</span></pre><pre>
    <span class="rem">''' &lt;remarks&gt;&lt;/remarks&gt;</span></pre><pre class="alt">
    <span class="kwrd">Private</span> <span class="kwrd">Function</span> GetGrayBitmap(<span class="kwrd">ByVal</span> file <span class="kwrd">As</span> <span class="kwrd">String</span>) <span class="kwrd">As</span> Bitmap</pre><pre>
        <span class="kwrd">Dim</span> bmp <span class="kwrd">As</span> Bitmap = <span class="kwrd">New</span> Bitmap(file)</pre><pre class="alt">
        <span class="kwrd">For</span> x <span class="kwrd">As</span> <span class="kwrd">Integer</span> = 0 <span class="kwrd">To</span> bmp.Width - 1</pre><pre>
            <span class="kwrd">For</span> y <span class="kwrd">As</span> <span class="kwrd">Integer</span> = 0 <span class="kwrd">To</span> bmp.Height - 1</pre><pre class="alt">
                <span class="kwrd">Dim</span> color <span class="kwrd">As</span> Color = bmp.GetPixel(x, y)</pre><pre>
                <span class="kwrd">Dim</span> gray <span class="kwrd">As</span> <span class="kwrd">Integer</span> = (<span class="kwrd">CInt</span>(color.R) + <span class="kwrd">CInt</span>(color.G) + <span class="kwrd">CInt</span>(color.B)) \ 3</pre><pre class="alt">
                bmp.SetPixel(x, y, color.FromArgb(gray, gray, gray))</pre><pre>
            <span class="kwrd">Next</span></pre><pre class="alt">
        <span class="kwrd">Next</span></pre><pre>
        <span class="kwrd">Return</span> bmp</pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Function</span></pre><pre>
 </pre><pre class="alt"><span class="kwrd">End</span> <span class="kwrd">Class</span></pre></div></div><p /><style type="text/css"><![CDATA[


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
.csharpcode .lnum { color: #606060; }]]></style><p> </p><p>C#</p><div style="width: 613px; height: 313px; overflow: auto"><div class="csharpcode"><pre class="alt"><span class="kwrd">using</span> System;</pre><pre><span class="kwrd">using</span> System.Collections.Generic;</pre><pre class="alt"><span class="kwrd">using</span> System.ComponentModel;</pre><pre><span class="kwrd">using</span> System.Data;</pre><pre class="alt"><span class="kwrd">using</span> System.Drawing;</pre><pre><span class="kwrd">using</span> System.Linq;</pre><pre class="alt"><span class="kwrd">using</span> System.Text;</pre><pre><span class="kwrd">using</span> System.Windows.Forms;</pre><pre class="alt">
 </pre><pre><span class="kwrd">namespace</span> WindowsFormsApplication1</pre><pre class="alt">
{</pre><pre>
 </pre><pre class="alt">
 </pre><pre>
    <span class="rem">//|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||</span></pre><pre class="alt">
    <span class="rem">//Author: Larry Nung</span></pre><pre>
    <span class="rem">//Date: 2009/6/2</span></pre><pre class="alt">
    <span class="rem">//File: </span></pre><pre>
    <span class="rem">//Memo: </span></pre><pre class="alt">
    <span class="rem">//|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||</span></pre><pre>
    <span class="rem">/// &lt;summary&gt;</span></pre><pre class="alt">
    <span class="rem">/// </span></pre><pre>
    <span class="rem">/// &lt;/summary&gt;</span></pre><pre class="alt">
    <span class="kwrd">public</span> <span class="kwrd">partial</span> <span class="kwrd">class</span> Form1 : Form</pre><pre>
    {</pre><pre class="alt">
        <span class="kwrd">public</span> Form1()</pre><pre>
        {</pre><pre class="alt">
            InitializeComponent();</pre><pre>
        }</pre><pre class="alt">
 </pre><pre>
 </pre><pre class="alt">
        <span class="rem">//***************************************************************************</span></pre><pre>
        <span class="rem">//Author: Larry Nung</span></pre><pre class="alt">
        <span class="rem">//Date: 2009/6/2</span></pre><pre>
        <span class="rem">//Purpose: </span></pre><pre class="alt">
        <span class="rem">//Memo: </span></pre><pre>
        <span class="rem">//***************************************************************************</span></pre><pre class="alt">
        <span class="rem">/// &lt;summary&gt;</span></pre><pre>
        <span class="rem">/// Handles the Click event of the button1 control.</span></pre><pre class="alt">
        <span class="rem">/// &lt;/summary&gt;</span></pre><pre>
        <span class="rem">/// &lt;param name="sender"&gt;The source of the event.&lt;/param&gt;</span></pre><pre class="alt">
        <span class="rem">/// &lt;param name="e"&gt;The &lt;see cref="System.EventArgs"/&gt; instance containing the event data.&lt;/param&gt;</span></pre><pre>
        <span class="kwrd">private</span> <span class="kwrd">void</span> button1_Click(<span class="kwrd">object</span> sender, EventArgs e)</pre><pre class="alt">
        {</pre><pre>
            <span class="kwrd">if</span> (openFileDialog1.ShowDialog() == DialogResult.OK)</pre><pre class="alt">
            {</pre><pre>
                pictureBox1.Image = GetGrayBitmap(openFileDialog1.FileName);</pre><pre class="alt">
            }</pre><pre>
        }</pre><pre class="alt">
 </pre><pre>
 </pre><pre class="alt">
        <span class="rem">//***************************************************************************</span></pre><pre>
        <span class="rem">//Author: Larry Nung</span></pre><pre class="alt">
        <span class="rem">//Date: 2009/6/2</span></pre><pre>
        <span class="rem">//Purpose: </span></pre><pre class="alt">
        <span class="rem">//Memo: </span></pre><pre>
        <span class="rem">//***************************************************************************</span></pre><pre class="alt">
        <span class="rem">/// &lt;summary&gt;</span></pre><pre>
        <span class="rem">/// Gets the gray bitmap.</span></pre><pre class="alt">
        <span class="rem">/// &lt;/summary&gt;</span></pre><pre>
        <span class="rem">/// &lt;param name="file"&gt;The file.&lt;/param&gt;</span></pre><pre class="alt">
        <span class="rem">/// &lt;returns&gt;&lt;/returns&gt;</span></pre><pre>
        <span class="kwrd">private</span> Bitmap GetGrayBitmap(<span class="kwrd">string</span> file)</pre><pre class="alt">
        {</pre><pre>
            Bitmap bmp = <span class="kwrd">new</span> Bitmap(file);</pre><pre class="alt">
            <span class="kwrd">for</span> (<span class="kwrd">int</span> x=0; x &lt; bmp.Width; x++)</pre><pre>
            {</pre><pre class="alt">
                <span class="kwrd">for</span> (<span class="kwrd">int</span> y=0; y &lt; bmp.Height; y++)</pre><pre>
                {</pre><pre class="alt">
                    Color color = bmp.GetPixel(x, y);</pre><pre>
                    <span class="kwrd">int</span> gray = (color.R + color.G + color.B) / 3;</pre><pre class="alt">
                    bmp.SetPixel(x, y, Color.FromArgb(gray, gray, gray));</pre><pre>
                }</pre><pre class="alt">
            }</pre><pre>
            <span class="kwrd">return</span> bmp;</pre><pre class="alt">
        }</pre><pre>
    }</pre><pre class="alt">
}</pre></div></div><p /><style type="text/css"><![CDATA[


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
.csharpcode .lnum { color: #606060; }]]></style><p> </p><p>執行結果：</p><p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="304" height="304" src="\images\posts\8651\image_thumb.png" /></p>
