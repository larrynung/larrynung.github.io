---
title: "[C#][VB.NET]自定義例外對話框"
date: "2013-11-06 12:00:00"
description: "[C#][VB.NET]自定義例外對話框"
tags: [CSharp]
---

<p>之前在『例外處理使用時機</a>』這篇有提到我目前很少會寫例外處理。除了在那篇提到的原因之外，還有個因素就是我會弄個自定義的例外處理視窗，讓使用者在例外發生時，可以匯出例外訊息並提供給開發人員。有了匯出的例外訊息，我們就可以很快的把未處理完的例外(指給程式員看的例外)給修正。</p>  <p>要做到自定義的例外對話框，我們需要利用Application.ThreadException事件。</p>  <p>先讓我們看一下MSDN的說明：</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/0904/f597175ff4e3_132CC/image_2.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\dcd63262-c2ae-4a33-9034-9c062fdf234a\image_thumb.png" width="384" height="146" /></a></p>  <p> </p>  <p>從MSDN的說明可以很清楚的看到，當執行緒發生例外，且該例外未被處理，則該事件即會觸發。</p>  <p> </p>  <p>接著就讓我們來看看如何才能利用該事件做出自定義的例外對話框。首先，我們需要設計自定義的例外對話框。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/0904/f597175ff4e3_132CC/image_4.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\dcd63262-c2ae-4a33-9034-9c062fdf234a\image_thumb_1.png" width="497" height="320" /></p>  <p> </p>  <p>接著撰寫繫上事件用的副程式。</p>  <p>VB.NET</p>  <div class="csharpcode">   <pre class="alt">    <span class="kwrd">Public</span> <span class="kwrd">Shared</span> <span class="kwrd">Sub</span> ShowBugWindowOnError()</pre>

  <pre>        <span class="kwrd">AddHandler</span> Application.ThreadException, <span class="kwrd">AddressOf</span> OnErrorOccur</pre>

  <pre class="alt">    <span class="kwrd">End</span> Sub</pre>
</div>

<p> </p>


<p>C#</p>

<div class="csharpcode">
  <pre class="alt">    <span class="kwrd">public</span> <span class="kwrd">static</span> <span class="kwrd">void</span> ShowBugWindowOnError()</pre>

  <pre>    {</pre>

  <pre class="alt">        Application.ThreadException += <span class="kwrd">new</span> System.Threading.ThreadExceptionEventHandler(OnErrorOccur);</pre>

  <pre>    }   </pre>
</div>

<p> </p>


<p> </p>

<p>最後寫上事件觸發時要執行的事件處理函式。</p>

<p>VB.NET</p>

<div class="csharpcode">
  <pre class="alt">    <span class="kwrd">Protected</span> <span class="kwrd">Shared</span> <span class="kwrd">Sub</span> OnErrorOccur(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> <span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> ThreadExceptionEventArgs)</pre>

  <pre>        <span class="kwrd">Dim</span> errorDlg <span class="kwrd">As</span> <span class="kwrd">New</span> ExceptionDialog</pre>

  <pre class="alt">        errorDlg.DetailErrorMsg_TextBox.Text = GetDetailErrorMsg(e.Exception)</pre>

  <pre>        errorDlg.ShowDialog()</pre>

  <pre class="alt">    <span class="kwrd">End</span> Sub</pre>
</div>

<p> </p>



<p>C#</p>

<div class="csharpcode">
  <pre class="alt">    <span class="kwrd">protected</span> <span class="kwrd">static</span> <span class="kwrd">void</span> OnErrorOccur(<span class="kwrd">object</span> sender, System.Threading.ThreadExceptionEventArgs e)</pre>

  <pre>    {</pre>

  <pre class="alt">        ExceptionDlg errorDlg = <span class="kwrd">new</span> ExceptionDlg();</pre>

  <pre>        errorDlg.DetailErrorMsg_TextBox.Text = GetDetailErrorMsg(e.Exception);</pre>

  <pre class="alt">        errorDlg.ShowDialog();</pre>

  <pre>    }</pre>
</div>

<p> </p>



<p> </p>

<p>到此一個簡單的自定義例外對話框就完成了。使用上，我們只需呼叫剛寫的繫上事件用副程式即可。</p>

<p>VB.NET</p>

<div style="width: 693px; height: 82px; overflow: auto">
  <div class="csharpcode">
    <pre class="alt">   <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Form1_Load(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> <span class="kwrd">MyBase</span>.Load</pre>

    <pre>        ExceptionDialog.ShowBugWindowOnError()</pre>

    <pre class="alt">    <span class="kwrd">End</span> Sub</pre>
  </div>
</div>

<p>C#</p>

<div class="csharpcode">
  <pre class="alt">    <span class="kwrd">private</span> <span class="kwrd">void</span> Form1_Load(<span class="kwrd">object</span> sender, EventArgs e)</pre>

  <pre>    {</pre>

  <pre class="alt">        ExceptionDlg.ShowBugWindowOnError();</pre>

  <pre>    }</pre>
</div>

<p> </p>



<p> </p>

<p>完整程式碼：</p>

<p>VB.NET</p>

<div style="width: 696px; height: 375px; overflow: auto">
  <div class="csharpcode">
    <pre class="alt"><span class="kwrd">Imports</span> System.Windows.Forms</pre>

    <pre><span class="kwrd">Imports</span> System.Threading</pre>

    <pre class="alt"><span class="kwrd">Imports</span> System.Text</pre>

    <pre> </pre>

    <pre class="alt"><span class="kwrd">Public</span> <span class="kwrd">Class</span> ExceptionDialog</pre>

    <pre> </pre>

    <pre class="alt"><span class="preproc">#Region</span> <span class="str">"Const"</span></pre>

    <pre>    <span class="kwrd">Const</span> OpenDetailButtonText <span class="kwrd">As</span> <span class="kwrd">String</span> = <span class="str">"v 詳細資料"</span></pre>

    <pre class="alt">    <span class="kwrd">Const</span> CloseDetailButtonText <span class="kwrd">As</span> <span class="kwrd">String</span> = <span class="str">"^ 詳細資料"</span></pre>

    <pre><span class="preproc">#End Region</span></pre>

    <pre class="alt"> </pre>

    <pre> </pre>

    <pre class="alt"> </pre>

    <pre><span class="preproc">#Region</span> <span class="str">"Var"</span></pre>

    <pre class="alt">    <span class="kwrd">Private</span> _isDetailOpened <span class="kwrd">As</span> <span class="kwrd">Boolean</span></pre>

    <pre><span class="preproc">#End Region</span></pre>

    <pre class="alt"> </pre>

    <pre> </pre>

    <pre class="alt"> </pre>

    <pre><span class="preproc">#Region</span> <span class="str">"Public Shared Method"</span></pre>

    <pre class="alt"> </pre>

    <pre>    <span class="rem">'***************************************************************************</span></pre>

    <pre class="alt">    <span class="rem">'Author: Larry Nung</span></pre>

    <pre>    <span class="rem">'Date: 2009/4/9</span></pre>

    <pre class="alt">    <span class="rem">'Purpose: </span></pre>

    <pre>    <span class="rem">'Memo: </span></pre>

    <pre class="alt">    <span class="rem">'***************************************************************************</span></pre>

    <pre>    <span class="rem">''' &lt;summary&gt;</span></pre>

    <pre class="alt">    <span class="rem">''' Shows the bug window on error.</span></pre>

    <pre>    <span class="rem">''' &lt;/summary&gt;</span></pre>

    <pre class="alt">    <span class="rem">''' &lt;remarks&gt;&lt;/remarks&gt;</span></pre>

    <pre>    <span class="kwrd">Public</span> <span class="kwrd">Shared</span> <span class="kwrd">Sub</span> ShowBugWindowOnError()</pre>

    <pre class="alt">        <span class="kwrd">AddHandler</span> Application.ThreadException, <span class="kwrd">AddressOf</span> OnErrorOccur</pre>

    <pre>    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre>

    <pre class="alt"><span class="preproc">#End Region</span></pre>

    <pre> </pre>

    <pre class="alt"> </pre>

    <pre><span class="preproc">#Region</span> <span class="str">"Protected Shared Method"</span></pre>

    <pre class="alt"> </pre>

    <pre>    <span class="rem">'***************************************************************************</span></pre>

    <pre class="alt">    <span class="rem">'Author: Larry Nung</span></pre>

    <pre>    <span class="rem">'Date: 2009/4/9</span></pre>

    <pre class="alt">    <span class="rem">'Purpose: </span></pre>

    <pre>    <span class="rem">'Memo: </span></pre>

    <pre class="alt">    <span class="rem">'***************************************************************************</span></pre>

    <pre>    <span class="rem">''' &lt;summary&gt;</span></pre>

    <pre class="alt">    <span class="rem">''' Called when [error occur].</span></pre>

    <pre>    <span class="rem">''' &lt;/summary&gt;</span></pre>

    <pre class="alt">    <span class="rem">''' &lt;param name="sender"&gt;The sender.&lt;/param&gt;</span></pre>

    <pre>    <span class="rem">''' &lt;param name="e"&gt;The &lt;see cref="System.Threading.ThreadExceptionEventArgs" /&gt; instance containing the event data.&lt;/param&gt;</span></pre>

    <pre class="alt">    <span class="rem">''' &lt;remarks&gt;&lt;/remarks&gt;</span></pre>

    <pre>    <span class="kwrd">Protected</span> <span class="kwrd">Shared</span> <span class="kwrd">Sub</span> OnErrorOccur(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> <span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> ThreadExceptionEventArgs)</pre>

    <pre class="alt">        <span class="kwrd">Dim</span> errorDlg <span class="kwrd">As</span> <span class="kwrd">New</span> ExceptionDialog</pre>

    <pre>        errorDlg.DetailErrorMsg_TextBox.Text = GetDetailErrorMsg(e.Exception)</pre>

    <pre class="alt">        errorDlg.ShowDialog()</pre>

    <pre>    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre>

    <pre class="alt"><span class="preproc">#End Region</span></pre>

    <pre> </pre>

    <pre class="alt"> </pre>

    <pre><span class="preproc">#Region</span> <span class="str">"Private Shared Method"</span></pre>

    <pre class="alt"> </pre>

    <pre>    <span class="rem">'***************************************************************************</span></pre>

    <pre class="alt">    <span class="rem">'Author: Larry Nung</span></pre>

    <pre>    <span class="rem">'Date: 2009/4/9</span></pre>

    <pre class="alt">    <span class="rem">'Purpose: </span></pre>

    <pre>    <span class="rem">'Memo: </span></pre>

    <pre class="alt">    <span class="rem">'***************************************************************************</span></pre>

    <pre>    <span class="rem">''' &lt;summary&gt;</span></pre>

    <pre class="alt">    <span class="rem">''' Gets the detail error MSG.</span></pre>

    <pre>    <span class="rem">''' &lt;/summary&gt;</span></pre>

    <pre class="alt">    <span class="rem">''' &lt;returns&gt;&lt;/returns&gt;</span></pre>

    <pre>    <span class="rem">''' &lt;remarks&gt;&lt;/remarks&gt;</span></pre>

    <pre class="alt">    <span class="kwrd">Private</span> <span class="kwrd">Shared</span> <span class="kwrd">Function</span> GetDetailErrorMsg(<span class="kwrd">ByVal</span> e <span class="kwrd">As</span> Exception) <span class="kwrd">As</span> <span class="kwrd">String</span></pre>

    <pre>        <span class="kwrd">Dim</span> str <span class="kwrd">As</span> <span class="kwrd">New</span> StringBuilder</pre>

    <pre class="alt">        str.AppendLine(<span class="kwrd">String</span>.Format(<span class="str">"Source: {0}"</span>, e.Source))</pre>

    <pre>        str.AppendLine(<span class="kwrd">String</span>.Format(<span class="str">"Message: {0}"</span>, e.Message))</pre>

    <pre class="alt">        str.AppendLine(<span class="kwrd">String</span>.Format(<span class="str">"TargetSite: {0}"</span>, e.TargetSite))</pre>

    <pre>        str.AppendLine(<span class="str">""</span>)</pre>

    <pre class="alt">        str.AppendLine(<span class="str">"StackTrace: "</span>)</pre>

    <pre>        str.AppendLine(e.StackTrace)</pre>

    <pre class="alt">        <span class="kwrd">Return</span> str.ToString</pre>

    <pre>    <span class="kwrd">End</span> <span class="kwrd">Function</span></pre>

    <pre class="alt"><span class="preproc">#End Region</span></pre>

    <pre> </pre>

    <pre class="alt"> </pre>

    <pre> </pre>

    <pre class="alt"> </pre>

    <pre> </pre>

    <pre class="alt"><span class="preproc">#Region</span> <span class="str">"Event Process"</span></pre>

    <pre>    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> OK_Button_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> OK_Button.Click</pre>

    <pre class="alt">        <span class="kwrd">Me</span>.DialogResult = System.Windows.Forms.DialogResult.OK</pre>

    <pre>        <span class="kwrd">Me</span>.Close()</pre>

    <pre class="alt">    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre>

    <pre> </pre>

    <pre class="alt">    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Cancel_Button_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Cancel_Button.Click</pre>

    <pre>        <span class="kwrd">Me</span>.DialogResult = System.Windows.Forms.DialogResult.Cancel</pre>

    <pre class="alt">        Application.<span class="kwrd">Exit</span>()</pre>

    <pre>    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre>

    <pre class="alt"> </pre>

    <pre>    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> Detail_Button_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Detail_Button.Click</pre>

    <pre class="alt">        _isDetailOpened = <span class="kwrd">Not</span> _isDetailOpened</pre>

    <pre>        Detail_Button.Text = <span class="kwrd">If</span>(_isDetailOpened, CloseDetailButtonText, OpenDetailButtonText)</pre>

    <pre class="alt">        <span class="kwrd">Me</span>.Height = <span class="kwrd">If</span>(_isDetailOpened, <span class="kwrd">Me</span>.DetailErrorMsg_TextBox.Bottom, <span class="kwrd">Me</span>.DetailErrorMsg_TextBox.Top) + 32</pre>

    <pre>    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre>

    <pre class="alt"> </pre>

    <pre>    <span class="kwrd">Private</span> <span class="kwrd">Sub</span> ExceptionDialog_Load(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> <span class="kwrd">MyBase</span>.Load</pre>

    <pre class="alt">        <span class="kwrd">Me</span>.Height = <span class="kwrd">Me</span>.DetailErrorMsg_TextBox.Top + 32</pre>

    <pre>        <span class="kwrd">Me</span>.ErrorIcon_Label.Image = SystemIcons.<span class="kwrd">Error</span>.ToBitmap</pre>

    <pre class="alt">    <span class="kwrd">End</span> <span class="kwrd">Sub</span></pre>

    <pre><span class="preproc">#End Region</span></pre>

    <pre class="alt"> </pre>

    <pre><span class="kwrd">End</span> <span class="kwrd">Class</span></pre>
  </div>
</div>

<p>C#</p>

<div style="width: 696px; height: 375px; overflow: auto">
  <div class="csharpcode">
    <pre class="alt"><span class="kwrd">using</span> System;</pre>

    <pre><span class="kwrd">using</span> System.Collections.Generic;</pre>

    <pre class="alt"><span class="kwrd">using</span> System.ComponentModel;</pre>

    <pre><span class="kwrd">using</span> System.Data;</pre>

    <pre class="alt"><span class="kwrd">using</span> System.Drawing;</pre>

    <pre><span class="kwrd">using</span> System.Linq;</pre>

    <pre class="alt"><span class="kwrd">using</span> System.Text;</pre>

    <pre><span class="kwrd">using</span> System.Windows.Forms;</pre>

    <pre class="alt"> </pre>

    <pre> </pre>

    <pre class="alt"><span class="kwrd">namespace</span> ExceptionDlgTest</pre>

    <pre>{</pre>

    <pre class="alt">    <span class="kwrd">public</span> <span class="kwrd">partial</span> <span class="kwrd">class</span> ExceptionDlg : Form</pre>

    <pre>    {</pre>

    <pre class="alt"> </pre>

    <pre>        <span class="preproc">#region</span> Const</pre>

    <pre class="alt">        <span class="kwrd">const</span> <span class="kwrd">string</span> OpenDetailButtonText = <span class="str">"v 詳細資料"</span>;</pre>

    <pre>        <span class="kwrd">const</span> <span class="kwrd">string</span> CloseDetailButtonText = <span class="str">"^ 詳細資料"</span>;</pre>

    <pre class="alt">        <span class="preproc">#endregion</span></pre>

    <pre> </pre>

    <pre class="alt">        <span class="preproc">#region</span> Var</pre>

    <pre>        <span class="kwrd">private</span> Boolean _isDetailOpened;</pre>

    <pre class="alt">        <span class="preproc">#endregion</span></pre>

    <pre> </pre>

    <pre class="alt"> </pre>

    <pre>        <span class="preproc">#region</span> Construction</pre>

    <pre class="alt">        <span class="kwrd">public</span> ExceptionDlg()</pre>

    <pre>        {</pre>

    <pre class="alt">            InitializeComponent();</pre>

    <pre>        }</pre>

    <pre class="alt">        <span class="preproc">#endregion</span></pre>

    <pre> </pre>

    <pre class="alt"> </pre>

    <pre> </pre>

    <pre class="alt">        <span class="preproc">#region</span> Public Shared Method</pre>

    <pre> </pre>

    <pre class="alt">        <span class="rem">//***************************************************************************</span></pre>

    <pre>        <span class="rem">//Author: Larry Nung</span></pre>

    <pre class="alt">        <span class="rem">//Date: 2009/4/9</span></pre>

    <pre>        <span class="rem">//Purpose: </span></pre>

    <pre class="alt">        <span class="rem">//Memo: </span></pre>

    <pre>        <span class="rem">//***************************************************************************</span></pre>

    <pre class="alt">        <span class="rem">/// &lt;summary&gt;</span></pre>

    <pre>        <span class="rem">/// </span></pre>

    <pre class="alt">        <span class="rem">/// &lt;/summary&gt;</span></pre>

    <pre>        <span class="kwrd">public</span> <span class="kwrd">static</span> <span class="kwrd">void</span> ShowBugWindowOnError()</pre>

    <pre class="alt">        {</pre>

    <pre>            Application.ThreadException += <span class="kwrd">new</span> System.Threading.ThreadExceptionEventHandler(OnErrorOccur);</pre>

    <pre class="alt">        }     </pre>

    <pre>        <span class="preproc">#endregion</span></pre>

    <pre class="alt"> </pre>

    <pre> </pre>

    <pre class="alt">        <span class="preproc">#region</span> Protected Shared Method</pre>

    <pre>        <span class="kwrd">protected</span> <span class="kwrd">static</span> <span class="kwrd">void</span> OnErrorOccur(<span class="kwrd">object</span> sender, System.Threading.ThreadExceptionEventArgs e)</pre>

    <pre class="alt">        {</pre>

    <pre>            ExceptionDlg errorDlg = <span class="kwrd">new</span> ExceptionDlg();</pre>

    <pre class="alt">            errorDlg.DetailErrorMsg_TextBox.Text = GetDetailErrorMsg(e.Exception);</pre>

    <pre>            errorDlg.ShowDialog();</pre>

    <pre class="alt">        }</pre>

    <pre>        <span class="preproc">#endregion</span></pre>

    <pre class="alt"> </pre>

    <pre> </pre>

    <pre class="alt">        <span class="preproc">#region</span> Private Shared Method</pre>

    <pre>        <span class="kwrd">private</span> <span class="kwrd">static</span> <span class="kwrd">string</span> GetDetailErrorMsg(Exception e)</pre>

    <pre class="alt">        {</pre>

    <pre>            StringBuilder str = <span class="kwrd">new</span> StringBuilder();</pre>

    <pre class="alt">            str.AppendLine(String.Format(<span class="str">"Source: {0}"</span>, e.Source));</pre>

    <pre>            str.AppendLine(String.Format(<span class="str">"Message: {0}"</span>, e.Message));</pre>

    <pre class="alt">            str.AppendLine(String.Format(<span class="str">"TargetSite: {0}"</span>, e.TargetSite));</pre>

    <pre>            str.AppendLine(<span class="str">""</span>);</pre>

    <pre class="alt">            str.AppendLine(<span class="str">"StackTrace: "</span>);</pre>

    <pre>            str.AppendLine(e.StackTrace);</pre>

    <pre class="alt">            <span class="kwrd">return</span> str.ToString();</pre>

    <pre>        }</pre>

    <pre class="alt">        <span class="preproc">#endregion</span></pre>

    <pre> </pre>

    <pre class="alt"> </pre>

    <pre>        <span class="preproc">#region</span> Event Process</pre>

    <pre class="alt">        <span class="kwrd">private</span> <span class="kwrd">void</span> Cancel_Button_Click(<span class="kwrd">object</span> sender, EventArgs e)</pre>

    <pre>        {</pre>

    <pre class="alt">            Application.Exit();</pre>

    <pre>        }</pre>

    <pre class="alt"> </pre>

    <pre>        <span class="kwrd">private</span> <span class="kwrd">void</span> OK_Button_Click(<span class="kwrd">object</span> sender, EventArgs e)</pre>

    <pre class="alt">        {</pre>

    <pre>            <span class="kwrd">this</span>.Close();</pre>

    <pre class="alt">        }</pre>

    <pre> </pre>

    <pre class="alt">        <span class="kwrd">private</span> <span class="kwrd">void</span> Detail_Button_Click(<span class="kwrd">object</span> sender, EventArgs e)</pre>

    <pre>        {</pre>

    <pre class="alt">            _isDetailOpened = !_isDetailOpened;</pre>

    <pre>            Detail_Button.Text = _isDetailOpened ? CloseDetailButtonText : OpenDetailButtonText;</pre>

    <pre class="alt">            <span class="kwrd">this</span>.Height = _isDetailOpened ? <span class="kwrd">this</span>.DetailErrorMsg_TextBox.Bottom : <span class="kwrd">this</span>.DetailErrorMsg_TextBox.Top + 32;</pre>

    <pre>        }</pre>

    <pre class="alt"> </pre>

    <pre>        <span class="kwrd">private</span> <span class="kwrd">void</span> ExceptionDlg_Load(<span class="kwrd">object</span> sender, EventArgs e)</pre>

    <pre class="alt">        {</pre>

    <pre>            <span class="kwrd">this</span>.Height = <span class="kwrd">this</span>.DetailErrorMsg_TextBox.Top + 32;</pre>

    <pre class="alt">            <span class="kwrd">this</span>.ErrorIcon_Label.Image = SystemIcons.Error.ToBitmap();</pre>

    <pre>        }</pre>

    <pre class="alt">        <span class="preproc">#endregion</span></pre>

    <pre> </pre>

    <pre class="alt">     </pre>

    <pre>    }</pre>

    <pre class="alt">}</pre>
  </div>
</div>

<p> </p>



<p> </p>

<p>執行畫面如下：</p>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\dcd63262-c2ae-4a33-9034-9c062fdf234a\image_thumb_2.png" width="469" height="141" /></p>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\dcd63262-c2ae-4a33-9034-9c062fdf234a\image_thumb_3.png" width="469" height="271" /></p>

<p> </p>

<h2>Conclusion</h2>

<p>透過Application.ThreadException事件，我們可以很容易達到該篇的效果。但需注意這樣的作法只對繫上的執行緒有效，非繫上的執行緒若發生例外，將無法截取到。在實際應用上，也可依自己需求加入記錄到事件記錄簿等功能，甚至可以使用.NET預設的例外視窗來顯示，只是多加了一些自己的處理，讓使用者感覺不出差異。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:4dbfe4c7-de20-4538-885f-6e8bdfd47fab" class="wlWriterSmartContent"><pre name="code" class="vb">    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        AddHandler Application.ThreadException, AddressOf Application_ThreadException
        ...
    End Sub

    Private Sub Application_ThreadException(ByVal sender As Object, ByVal e As ThreadExceptionEventArgs)
        ... 
        Dim exceptionDlg As New ThreadExceptionDialog(e.Exception)
        exceptionDlg.ShowDialog()
    End Sub</pre></div>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\dcd63262-c2ae-4a33-9034-9c062fdf234a\image_thumb.png" width="444" height="319" /> </p>

<p> </p>

<p>另外，若有興趣的也可以改繫上AppDomain.UnhandledException試看看。</p>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\dcd63262-c2ae-4a33-9034-9c062fdf234a\image_thumb_4.png" width="347" height="138" /> </p>

<p> </p>

<h2>Download</h2>

<p>ExceptionDlg.zip</p>
