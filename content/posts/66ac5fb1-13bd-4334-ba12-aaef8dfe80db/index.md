---
title: "[VB.NET]使用Make single instance application實現單一程式執行個體時所發生的怪現象"
date: "2013-11-06 12:00:00"
tags: [VB.NET]
description: "前陣子筆者在回應論壇上程式縮至常駐列，程式重複開啟時視窗無法還原這篇發問，因為這篇發問還滿有趣的，所以稍稍紀錄一下。發問者主要是想要嘗試實現單一程式執行個體，但是卻沒有打算一開始就到位，因此只是很簡單的勾選VB.NET屬性頁中的Make single instance application設定。"
---

前陣子筆者在回應論壇上程式縮至常駐列，程式重複開啟時視窗無法還原這篇發問，因為這篇發問還滿有趣的，所以稍稍紀錄一下。發問者主要是想要嘗試實現單一程式執行個體，但是卻沒有打算一開始就到位，因此只是很簡單的勾選VB.NET屬性頁中的Make single instance application設定。

![image_thumb.png](/images/posts/66ac5fb1-13bd-4334-ba12-aaef8dfe80db/image_thumb.png)

而發問者的程式也只是很簡單的當是窗縮到最小時隱藏到系統列，以及雙擊系統列圖示後將視窗恢復，像是下面這樣：

```vb
Public Class Form1

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
End Class
```

程式運行起來，在縮放到系統列跟還原上都沒有什麼問題，運作良好。單一程式執行個體的功能也已套上，程式無法被開啟多個執行個體。但是若是將程式縮小到系統列，然後點選程式嘗試開啟其他執行個體，再試圖將程式還原，這樣的操作循環個幾次就會發現程式的視窗不見了。

筆者嘗試追了一下這樣的情形，看到這樣的現象發生時仍是本來的Process ID，代表著程式還是本來的執行個體。接著筆者將Visual Studio附加到運行的Process上去進行除錯。

![image_thumb_1.png](/images/posts/66ac5fb1-13bd-4334-ba12-aaef8dfe80db/image_thumb_1.png)

發現視窗的位置變到了(-32000,-32000)，所以我們在桌面範圍內看不到本來視窗的蹤影。

![image_thumb_2.png](/images/posts/66ac5fb1-13bd-4334-ba12-aaef8dfe80db/image_thumb_2.png)

看到了嗎？這問題還滿奇特的，奇特的地方在於使用Make single instance application實現單一程式執行個體時，嘗試開啟其它的執行個體，雖然新的執行個體無法啟動，但是卻有機會會影響到本來的執行個體的位置。這邊筆者不太能理解為何本來的執行個體會受新的執行個體影響,若是改用Mutex來做類似的效果，整個運作就正常許多。

```vb
Imports System.Threading

Public Class Form1

    <STAThread> _
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
End Class
```

# Link

* 程式縮至常駐列，程式重複開啟時視窗無法還原
