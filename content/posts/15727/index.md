---
title: "[VB.NET]Get a Control's Z-Order with ControlCollection.GetChildIndex"
slug: "vbnet-get-a-control-s-z-order-with-controlcollection-getchildindex"
aliases: ["/posts/15727/"]
date: "2010-06-08 10:32:59"
description: "若要取得表單上元件的Z-Order，我們可以透過ControlCollection.GetChildIndex去取得，取得的值越大，代表表單元件在越上面，越小，則代表表單元件在越下面。簡易範例程式如下： 運行後的效果如下： Download GetZOrder.zip"
tags: [VB.NET]
---

若要取得表單上元件的Z-Order，我們可以透過ControlCollection.GetChildIndex去取得，取得的值越大，代表表單元件在越上面，越小，則代表表單元件在越下面。簡易範例程式如下：

```vb
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

![image_thumb_1.png](/images/posts/15727/image_thumb_1.png)

## Download

[GetZOrder.zip](http://Files.Dotblogs.com.tw/larrynung/1006/20106810355411.zip)
