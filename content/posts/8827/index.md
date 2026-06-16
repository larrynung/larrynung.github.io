---
title: "[VB.NET]自定義ComboBox下拉清單選項"
date: "2009-06-15 11:09:17"
description: "實作步驟 Step1.ComboBox.DrawMode設為OwnerDrawFixed或OwnerDrawVariable Step2.在ComboBox.DrawItem事件中重繪ComboBox下拉清單選項 程式範例 VB.NET 執行畫面"
tags: [VB.NET]
---

## 實作步驟

**Step1.ComboBox.DrawMode設為OwnerDrawFixed或OwnerDrawVariable**

![image_thumb.png](/images/posts/8827/image_thumb.png)

**Step2.在ComboBox.DrawItem事件中重繪ComboBox下拉清單選項**

## 程式範例

VB.NET

```
Public Class Form1

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        ComboBox1.DisplayMember = "Color"
        ComboBox1.Items.Add(Brushes.Cyan)
        ComboBox1.Items.Add(Brushes.Yellow)
    End Sub

    Private Sub ComboBox1_DrawItem(ByVal sender As System.Object, ByVal e As System.Windows.Forms.DrawItemEventArgs) Handles ComboBox1.DrawItem
        Dim cmb As ComboBox = DirectCast(sender, ComboBox)
        Dim brush As SolidBrush = DirectCast(cmb.Items(e.Index), SolidBrush)
        Dim g As Graphics = e.Graphics
        e.DrawBackground()
        e.DrawFocusRectangle()
        Dim rect As Rectangle = e.Bounds
        rect.Offset(2, 2)
        rect.Width = 20
        rect.Height -= 4
        g.DrawRectangle(Pens.Black, rect)

        rect.Offset(1, 1)
        rect.Width -= 1
        rect.Height -= 1
        g.FillRectangle(brush, rect)

        g.DrawString(brush.Color.ToString, Font, Brushes.Black, e.Bounds.X + 30, e.Bounds.Y + 3)
    End Sub
End Class
```

執行畫面

![image_thumb_1.png](/images/posts/8827/image_thumb_1.png)
