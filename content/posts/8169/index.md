---
title: "[VB.NET].NET多語系程式(二)"
date: "2009-04-24 11:57:31"
description: "[VB.NET].NET多語系程式(二)"
tags: [VB.NET]
---

## ![image_thumb_8.png](/images/posts/8169/image_thumb_8.png)

## Introduction

本篇將介紹.NET多語系程式的寫法 ，下面會利用資料庫來達到多語系的功能。

## 學習目標

* .NET多語程式撰寫
* MyDatabase類別庫基本使用
* 用資料庫實現多語功能

## 操作步驟

**Step1.首先準備個資料庫，內含所有語系的資料**

![image_thumb_2.png](/images/posts/8169/image_thumb_2.png)

![image_thumb_1.png](/images/posts/8169/image_thumb_1.png)

**Step2.切換語系時，從資料庫中抓取對應的顯示字串**

```
Dim db As MyDatabase.UseDB.AccessDB
Dim dt As DataTable

Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
    db = New MyDatabase.UseDB.AccessDB("Language.mdb")
    dt = db.GetDataTable("Select * from lan")
End Sub

Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
    Me.Text = dt.Select("Key='Title_TW'")(0).Item("Value")
End Sub

Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
    Me.Text = dt.Select("Key='Title_CH'")(0).Item("Value")
End Sub

Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
    Me.Text = dt.Select("Key='Title_EN'")(0).Item("Value")
End Sub

Private Sub Button4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button4.Click
    Me.Text = dt.Select("Key='Title_JP'")(0).Item("Value")
End Sub

Private Sub Button5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button5.Click
    Me.Text = dt.Select("Key='Title_K'")(0).Item("Value")
End Sub
```

到此一個多語程式就完成了，執行效果如下：

![image_thumb_3.png](/images/posts/8169/image_thumb_3.png) ![image_thumb_4.png](/images/posts/8169/image_thumb_4.png)

![image_thumb_5.png](/images/posts/8169/image_thumb_5.png) ![image_thumb_6.png](/images/posts/8169/image_thumb_6.png)

![image_thumb_7.png](/images/posts/8169/image_thumb_7.png)

![image_thumb.png](/images/posts/8169/image_thumb.png)
