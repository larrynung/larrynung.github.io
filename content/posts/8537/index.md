---
title: "[VB.NET]即時座標交叉線條"
date: "2009-05-23 09:36:39"
description: "在小鋪看到個網友發問個問題，希望能夠在滑鼠座標所在點畫上座標交叉線條。大概效果如下： 這效果其實很容易就可以達到，隨手紀錄一下。 範例程式一 範例程式二 相關連結 藍色小鋪-(VB.NET 2003)請問要如何在表單內畫出即時線條?"
tags: [VB.NET]
---

在小鋪看到個網友發問個問題，希望能夠在滑鼠座標所在點畫上座標交叉線條。大概效果如下：

![image3_thumb.png](/images/posts/8537/image3_thumb.png)  ![image12_thumb.png](/images/posts/8537/image12_thumb.png)

這效果其實很容易就可以達到，隨手紀錄一下。

## 範例程式一

```
Public Class Form1
    Private Sub Form1_MouseMove(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles MyBase.MouseMove
        Me.Invalidate()
    End Sub

    Private Sub Form1_Paint(ByVal sender As Object, ByVal e As System.Windows.Forms.PaintEventArgs) Handles Me.Paint
        Dim x As Integer
        Dim y As Integer
        With PointToClient(MousePosition)
            x = .X
            y = .Y
        End With
        With e.Graphics
            .DrawLine(Pens.Black, 0, y, Me.Width, y)
            .DrawLine(Pens.Black, x, 0, x, Me.Height)
        End With
    End Sub
End Class
```

## 範例程式二

```
Public Class Form1
    Dim g As Graphics
    Private Sub Form1_MouseMove(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles MyBase.MouseMove
        Dim point As Point = PointToClient(MousePosition)
        Dim x As Integer = point.X
        Dim y As Integer = point.Y
        g.Clear(Me.BackColor)
        g.DrawLine(Pens.Black, 0, y, Me.Width, y)
        g.DrawLine(Pens.Black, x, 0, x, Me.Height)
    End Sub

    Public Sub New()

        ' 此為 Windows Form 設計工具所需的呼叫。
        InitializeComponent()

        ' 在 InitializeComponent() 呼叫之後加入任何初始設定。

        g = Me.CreateGraphics
    End Sub
End Class
```

## 相關連結

* 藍色小鋪-(VB.NET 2003)請問要如何在表單內畫出即時線條?
