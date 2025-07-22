---
title: "[VB.NET]Change MDI Parent BackColor"
date: "2010-01-23 12:27:55"
description: "[VB.NET]Change MDI Parent BackColor"
tags: [VB.NET]
---

最近在調整MDI背景顏色時，發現MDI的背景顏色不能直接設定。直接設定的話會像下圖一樣，會看不到預期的結果。

其實這是因為WinForm在設定了IsMdiContainer屬性後，WinForm上面會自動添加一個MdiClient控制項在上面。這個控制項是MDI子表單的容器，能放置MDI子表單。而WinForm的BackColor在改變時並未跟著調整MdiClient.BackColor才會有這樣的現象。

有興趣的可以試著拖曳一下Visual Studio內部的視窗，會有機會在更新表單時看到一會表單的背景顏色。

要解決這樣的問題，我們可以把WinForm表單內的MdiClient的背景顏色跟著WinForm.BackColor調整。

  像是可以用迴圈找尋MdiClient後調整      
     Public Class Form1
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        SetMdiBackColor()
    End Sub

    Private Sub SetMdiBackColor()
        For Each c As Control In Me.Controls
            If TypeOf c Is MdiClient Then
                c.BackColor = Me.BackColor
                Exit For
            End If
        Next
    End Sub
End Class

也可以直接跟改最後一個控制項的背景顏色(這是因為MdiClient會是第一個被加進去的控制項的原因) 

  Public Class Form1
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        SetMdiBackColor()
    End Sub

    Private Sub SetMdiBackColor()
        Me.Controls(Me.Controls.Count - 1).BackColor = Me.BackColor
    End Sub
End Class

當然，最好可以把表單的BackColor與MdiClient的BackColor給繫在一起。

Controls(Controls.Count - 1).DataBindings.Add("BackColor", Me, "BackColor")

## Link

  MdiClient 類別 

  如何變更在 Visual Basic.NET 或 Visual Basic 2005 中的 MDI 父表單的背景色彩 

  MDI Container BackColor 

  MDI Form BackColor (Client Area)