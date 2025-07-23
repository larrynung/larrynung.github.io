---
title: "[VB.NET]用ControlCollection.GetChildIndex取得表單元件的Z-Order"
date: "2010-06-08 10:32:59"
description: "[VB.NET]用ControlCollection.GetChildIndex取得表單元件的Z-Order"
tags: [VB.NET]
---

若要取得表單上元件的Z-Order，我們可以透過ControlCollection.GetChildIndex去取得，取得的值越大，代表表單元件在越上面，越小，則代表表單元件在越下面。簡易範例程式如下：
```
Public Class Form1
Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
For Each c As Control In Me.Controls
Dim lablZIndex As New Label
lablZIndex.Text = Me.Controls.GetChildIndex(c)
lablZIndex.AutoSize = True
lablZIndex.ForeColor = Color.White
lablZIndex.BackColor = Color.Blue
c.Controls.Add(lablZIndex)
Next
End Sub
End Class
```
運行後的效果如下：

![](/images/posts/15727/)

## Download

GetZOrder.zip