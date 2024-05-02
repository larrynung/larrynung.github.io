---
title: "[VB.NET]使用Make single instance application實現單一程式執行個體時所發生的怪現象"
date: "2013-11-06 12:00:00"
description: "[VB.NET]使用Make single instance application實現單一程式執行個體時所發生的怪現象"
---

<p>前陣子筆者在回應論壇上程式縮至常駐列，程式重複開啟時視窗無法還原</a>這篇發問，因為這篇發問還滿有趣的，所以稍稍紀錄一下。發問者主要是想要嘗試實現單一程式執行個體，但是卻沒有打算一開始就到位，因此只是很簡單的勾選VB.NET屬性頁中的Make single instance application設定。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1303/1037d6749381_AF99/image_2.png"><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\66ac5fb1-13bd-4334-ba12-aaef8dfe80db\image_thumb.png" width="425" height="179" /> </p>  <p> </p>  <p>而發問者的程式也只是很簡單的當是窗縮到最小時隱藏到系統列，以及雙擊系統列圖示後將視窗恢復，像是下面這樣：</p>  <div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:cc291899-eb8f-4ac8-862f-bfb69323a349" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="vb">Public Class Form1

    Private Sub Form1_Resize(sender As Object, e As EventArgs) Handles MyBase.Resize
        If Me.WindowState = FormWindowState.Minimized Then
            NotifyIcon1.Visible = True
            Me.Hide()
        End If
    End Sub

    Private Sub NotifyIcon1_MouseDoubleClick(sender As Object, e As MouseEventArgs) Handles NotifyIcon1.MouseDoubleClick
        Me.Visible = True
        Me.WindowState = 0 '還原
        Me.Activate()
        Me.TopMost = True
        NotifyIcon1.Visible = False
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        NotifyIcon1.Icon = Me.Icon
    End Sub
End Class</pre></div>

<p> </p>

<p>程式運行起來，在縮放到系統列跟還原上都沒有什麼問題，運作良好。單一程式執行個體的功能也已套上，程式無法被開啟多個執行個體。但是若是將程式縮小到系統列，然後點選程式嘗試開啟其他執行個體，再試圖將程式還原，這樣的操作循環個幾次就會發現程式的視窗不見了。</p>

<p> </p>

<p>筆者嘗試追了一下這樣的情形，看到這樣的現象發生時仍是本來的Process ID，代表著程式還是本來的執行個體。接著筆者將Visual Studio附加到運行的Process上去進行除錯。</p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\66ac5fb1-13bd-4334-ba12-aaef8dfe80db\image_thumb_1.png" width="644" height="436" /> </p>

<p> </p>

<p>發現視窗的位置變到了(-32000,-32000)，所以我們在桌面範圍內看不到本來視窗的蹤影。</p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\66ac5fb1-13bd-4334-ba12-aaef8dfe80db\image_thumb_2.png" width="460" height="123" /> </p>

<p> </p>

<p>看到了嗎？這問題還滿奇特的，奇特的地方在於使用Make single instance application實現單一程式執行個體時，嘗試開啟其它的執行個體，雖然新的執行個體無法啟動，但是卻有機會會影響到本來的執行個體的位置。這邊筆者不太能理解為何本來的執行個體會受新的執行個體影響,若是改用Mutex來做類似的效果，整個運作就正常許多。</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:6e8754e4-2efe-49d4-82a8-2963ed849f43" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="vb">Imports System.Threading

Public Class Form1

    &lt;STAThread&gt; _
    Public Shared Sub Main()
        Dim isCreated As Boolean

        Using m As New Mutex(False, "NotifyIconApp", isCreated)
            If Not isCreated Then
                Return
            End If
            Application.Run(New Form1())
        End Using
    End Sub

    Private Sub Form1_Resize(sender As Object, e As EventArgs) Handles MyBase.Resize
        If Me.WindowState = FormWindowState.Minimized Then
            NotifyIcon1.Visible = True
            Me.Hide()
        End If
    End Sub

    Private Sub NotifyIcon1_MouseDoubleClick(sender As Object, e As MouseEventArgs) Handles NotifyIcon1.MouseDoubleClick
        Me.Visible = True
        Me.WindowState = 0 '還原
        Me.Activate()
        Me.TopMost = True
        NotifyIcon1.Visible = False
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        NotifyIcon1.Icon = Me.Icon
    End Sub
End Class</pre></div>

<p> </p>

<h1>Link</h1>

<ul>
  <li>程式縮至常駐列，程式重複開啟時視窗無法還原</li>
</ul>
