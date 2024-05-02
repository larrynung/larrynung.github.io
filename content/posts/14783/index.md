---
title: "[VB.NET]密碼框顯示程式探討與其簡易的保護之道"
date: "2010-04-24 12:17:10"
description: "[VB.NET]密碼框顯示程式探討與其簡易的保護之道"
tags: [VB.NET]
---

<p>相信大家都看過甚至用過密碼顯示工具，其原理Rico大[C#][WinForm]擺脫密碼透視小工具這篇已經把概念給帶出來了，主要是要過濾WM_GETTEXT與WM_SETTEXT兩個訊息(WM_SETTEXT過濾的原因不詳，這邊直接沿用)，但除了取得密碼外，也有的工具是可以讓密碼直接顯示的，那要怎摸做呢？很簡單，其實密碼框是透過設定EM_SETPASSWORDCHAR屬性來達到用星號隱藏密碼的效果，因此我們只要利用PostMessage把密碼框的EM_SETPASSWORDCHAR屬性給取消即可，簡易的程式如下。</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:89594e39-3a0e-4282-965d-0128e5a25a84" class="wlWriterEditableSmartContent"><pre name="code" class="vb">    &lt;DllImport("user32.dll")&gt; _
    Private Shared Function WindowFromPoint(ByVal Point As Point) As IntPtr
    End Function

    &lt;DllImport("user32.dll", SetLastError:=True, CharSet:=CharSet.Auto)&gt; _
Private Shared Function PostMessage(ByVal hWnd As IntPtr, ByVal Msg As UInteger, ByVal wParam As IntPtr, ByVal lParam As IntPtr) As Boolean
    End Function

    Const EM_SETPASSWORDCHAR = &amp;HCC

    Private Sub TargetSelectedControl1_TargetSelected(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TargetSelectedControl1.TargetSelected
        Dim hWnd As IntPtr = WindowFromPoint(MousePosition)
        PostMessage(hWnd, EM_SETPASSWORDCHAR, 0, 0)
    End Sub</pre></div>

<p> </p>

<p>這支測試程式我在介面上放了三個密碼框，依序為內建的TextBox、有過濾WM_GETTEXT與WM_SETTEXT的密碼框、與增加過濾EM_SETPASSWORDCHAR的密碼框，在上面分別打入測試用的字串"abc"。</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\14783\image_thumb.png" width="268" height="158" /></p>

<p> </p>

<p>分別拖曳箭靶至三個密碼框，用以觸發把EM_SETPASSWORDCHAR屬性給取消的程式碼。</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\14783\image_thumb_1.png" width="268" height="158" /> </p>

<p> </p>

<p>實驗後發現，前兩個密碼框變回一般的文字輸入框，而最後一個密碼框仍舊完好。</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\14783\image_thumb_2.png" width="268" height="158" /> </p>

<p> </p>

<p>由以上的實驗，除了可以了解密碼框顯示的概念外，也可以了解簡單的防止密碼顯示起碼要過濾WM_GETTEXT、WM_SETTEXT、與EM_SETPASSWORDCHAR，就像如下的程式一般：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:74821b60-646a-4139-8b15-7d43c73290bd" class="wlWriterEditableSmartContent"><pre name="code" class="vb">Public Class MyPassWordBox
    Inherits TextBox

    Const WM_SETTEXT As Integer = &amp;HC
    Const WM_GETTEXT As Integer = &amp;HD
    Const EM_SETPASSWORDCHAR = &amp;HCC

    Sub New()
        With Me
            .Multiline = False
            .UseSystemPasswordChar = True
        End With
    End Sub

    Protected Overrides Sub WndProc(ByRef m As System.Windows.Forms.Message)
        If m.Msg = WM_SETTEXT OrElse m.Msg = WM_GETTEXT OrElse m.Msg = EM_SETPASSWORDCHAR Then
            Return
        End If
        MyBase.WndProc(m)
    End Sub

End Class
</pre></div>

<p> </p>

<p>除此之外，若能再把密碼加密儲存就更保險了，但這不是這篇紀錄的重點，有興趣的自行研究。</p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>[C#][WinForm]擺脫密碼透視小工具 </li>
</ul>
