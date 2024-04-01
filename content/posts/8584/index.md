---
title: "[VB.NET]突破Disable按鈕的封鎖與限制"
date: "2009-05-28 01:28:08"
description: "[VB.NET]突破Disable按鈕的封鎖與限制"
tags: [VB.NET]
---

<h2>Introduction</h2><p>一般來說，當我們程式中有部份功能欲不讓使用者使用時。通常我們會把按鈕給Disable掉，讓使用者無法執行特定的功能。但這樣做真的就安全嗎？答案是否定的。其實光是把按鈕給Disable掉是很容易破解的，在對岸就已有許多破解工具 (e.x. 按鈕突破大師)，因此在編碼上最好還是要在程式中自行加上判斷，讓按鈕就算被突破也無法執行。</p><p> </p><h2>突破Disable按鈕的封鎖與限制</h2><p>欲突破Disable按鈕的封鎖與限制，其實很簡單。只要透過Win32 API即可達成。</p><p>需要使用的API有：</p><ul><li>ChildWindowFromPoint</li><li>GetForegroundWindow</li><li>IsWindowEnabled</li><li>EnableWindow</li><li>GetCursorPos</li><li>ScreenToClient</li></ul><p> </p><p>程式流程如下：</p><p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="274" height="534" src="\images\posts\8584\image_thumb.png" /></p><p> </p><p>程式範例如下：</p><p>MFC</p><div style="width: 622px; height: 271px; overflow: auto"><div class="csharpcode"><pre class="alt"><span class="kwrd">void</span> CBtnEnableDlg::OnButton1() </pre><pre>
{</pre><pre class="alt">
  SetTimer(1,100,NULL);</pre><pre>
}</pre><pre class="alt">
 </pre><pre><span class="kwrd">void</span> CBtnEnableDlg::OnTimer(UINT nIDEvent) </pre><pre class="alt">
{</pre><pre>
 HWND hWnd,hWndChild;</pre><pre class="alt">
  POINT point;</pre><pre>
 </pre><pre class="alt">
    hWnd=::GetForegroundWindow();</pre><pre>
    GetCursorPos(&amp;point);</pre><pre class="alt">
    ::ScreenToClient(hWnd,&amp;point);</pre><pre>
    hWndChild=::ChildWindowFromPoint(hWnd,point);</pre><pre class="alt">
    <span class="kwrd">if</span>(::IsWindowEnabled(hWndChild)==0)</pre><pre>
    {            </pre><pre class="alt">
    ::EnableWindow(hWndChild,1);</pre><pre>
  }             </pre><pre class="alt">
    </pre><pre>
    CDialog::OnTimer(nIDEvent);</pre><pre class="alt">
}</pre></div></div><p> </p><p /><style type="text/css"><![CDATA[



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
.csharpcode .lnum { color: #606060; }]]></style><p> </p><p>VB.NET</p><div style="width: 622px; height: 329px; overflow: auto"><div class="csharpcode"><pre class="alt"><span class="kwrd">Imports</span> System.Runtime.InteropServices</pre><pre>
 </pre><pre class="alt"><span class="kwrd">Public</span> <span class="kwrd">Class</span> Form1</pre><pre>
 </pre><pre class="alt">
    &lt;DllImport(<span class="str">"user32.dll"</span>)&gt; _</pre><pre><span class="kwrd">Private</span> <span class="kwrd">Shared</span> <span class="kwrd">Function</span> ChildWindowFromPoint(<span class="kwrd">ByVal</span> hWndParent <span class="kwrd">As</span> IntPtr, <span class="kwrd">ByVal</span> Point <span class="kwrd">As</span> Point) <span class="kwrd">As</span> IntPtr</pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Function</span></pre><pre>
 </pre><pre class="alt">
    &lt;DllImport(<span class="str">"user32.dll"</span>, SetLastError:=<span class="kwrd">True</span>)&gt; _</pre><pre><span class="kwrd">Private</span> <span class="kwrd">Shared</span> <span class="kwrd">Function</span> GetForegroundWindow() <span class="kwrd">As</span> IntPtr</pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Function</span></pre><pre>
 </pre><pre class="alt">
    &lt;DllImport(<span class="str">"user32.dll"</span>)&gt; _</pre><pre><span class="kwrd">Private</span> <span class="kwrd">Shared</span> <span class="kwrd">Function</span> IsWindowEnabled(<span class="kwrd">ByVal</span> hWnd <span class="kwrd">As</span> IntPtr) <span class="kwrd">As</span> &lt;MarshalAs(UnmanagedType.Bool)&gt; <span class="kwrd">Boolean</span></pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Function</span></pre><pre>
 </pre><pre class="alt">
    <span class="kwrd">Declare</span> <span class="kwrd">Function</span> EnableWindow <span class="kwrd">Lib</span> <span class="str">"user32"</span> (<span class="kwrd">ByVal</span> hwnd <span class="kwrd">As</span> IntPtr, <span class="kwrd">ByVal</span> fEnable <span class="kwrd">As</span> <span class="kwrd">Integer</span>) <span class="kwrd">As</span> <span class="kwrd">Integer</span></pre><pre>
 </pre><pre class="alt">
    &lt;DllImport(<span class="str">"user32.dll"</span>, SetLastError:=<span class="kwrd">True</span>)&gt; _</pre><pre><span class="kwrd">Private</span> <span class="kwrd">Shared</span> <span class="kwrd">Function</span> ScreenToClient(<span class="kwrd">ByVal</span> hWnd <span class="kwrd">As</span> IntPtr, <span class="kwrd">ByRef</span> lpPoint <span class="kwrd">As</span> Point) <span class="kwrd">As</span> <span class="kwrd">Boolean</span></pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Function</span></pre><pre>
 </pre><pre class="alt">
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Timer1_Tick(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Timer1.Tick</pre><pre>
        <span class="kwrd">Dim</span> p <span class="kwrd">As</span> Point = MousePosition</pre><pre class="alt">
        <span class="kwrd">Dim</span> hWnd, hWndChild <span class="kwrd">As</span> IntPtr</pre><pre>
        hWnd = GetForegroundWindow()</pre><pre class="alt">
        ScreenToClient(hWnd, p)</pre><pre>
        hWndChild = ChildWindowFromPoint(hWnd, p)</pre><pre class="alt">
 </pre><pre>
        <span class="kwrd">If</span> <span class="kwrd">Not</span> IsWindowEnabled(hWndChild) <span class="kwrd">Then</span></pre><pre class="alt">
            EnableWindow(hWndChild, 1)</pre><pre>
        <span class="kwrd">End</span> <span class="kwrd">If</span></pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre>
 </pre><pre class="alt">
    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> CheckBox1_CheckedChanged(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> CheckBox1.CheckedChanged</pre><pre>
        Timer1.Enabled = CheckBox1.Checked</pre><pre class="alt">
    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre><pre><span class="kwrd">End</span> <span class="kwrd">Class</span></pre></div></div><p> </p><p /><style type="text/css"><![CDATA[

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
.csharpcode .lnum { color: #606060; }]]></style><style type="text/css"><![CDATA[



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
.csharpcode .lnum { color: #606060; }]]></style><p> </p><p>執行後我們把滑鼠移到Disable的按鈕上，按鈕就會被強制變回Enable狀態了。變回Enable的按鈕也變得可以按下與執行。</p><p> </p><h2>執行步驟</h2><p><strong>Step1.開啟按鈕突破程式</strong></p><p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="170" height="112" src="\images\posts\8584\image_thumb_1.png" /></a></p><p> </p><p><strong>Step2.開啟欲突破的程式</strong></p><p><a href="http://files.dotblogs.com.tw/larrynung/0905/Disable_119C/image_6.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="490" height="336" src="\images\posts\8584\image_thumb_2.png" /></a></p><p> </p><p><strong>Step3.啟動按鈕突破功能</strong></p><p><a href="http://files.dotblogs.com.tw/larrynung/0905/Disable_119C/image_8.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="170" height="112" src="\images\posts\8584\image_thumb_3.png" /></a></p><p> </p><p><strong>Step4.把滑鼠移到欲突破的按鈕上</strong></p><p>當滑鼠移到欲突破的Disable按鈕上，按鈕會被強制設回Enable。</p><p><a href="http://files.dotblogs.com.tw/larrynung/0905/Disable_119C/image_10.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="490" height="336" src="\images\posts\8584\image_thumb_4.png" /></p><p> </p><p>P.S.</p><ul><li>上述範例對.NET程式的按鈕無效，請使用非.NET程式來測試。</li><li>雖範例無法達到突破.NET按鈕，但這不代表.NET程式不需注意這問題。因為能突破.NET按鈕的工具確實存在(e.x. Enable.NET)。</li><li>雖範例只能把Disable按鈕設為Enable，但其實運用同樣的概念也可以把隱藏的元件顯示出來。</li></ul><p> </p><h2>Conclusion</h2><p>此篇的主旨不是要教程式員破解，而是要提醒設計員在程式的設計上不是只要把按鈕給Disable掉就安全了。還是要額外利用Code去判斷是否可以執行才是較為安全的作法，尤其是程式中重要的功能更是要加以防堵。</p>
