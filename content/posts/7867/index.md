---
title: "[.NET Concept][VB.NET]MDI子視窗放大時的注意事項"
date: "2009-04-04 11:51:10"
description: "[.NET Concept][VB.NET]MDI子視窗放大時的注意事項"
tags: [.NET Concept,VB.NET]
---

開發MDI程式時，若需要一開始就放大子視窗，有些地方需特別留意。

這問題是同事在寫VC++.NET時發現的，本來以為是VC++.NET才會發生。剛試了一下，其它語言像是VB.NET也會有此現象。

讓我們跟著下面步驟來看一下：

**Step1.把MDI主表單設計成大概如下圖這樣**

![image_thumb.png](/images/posts/7867/image_thumb.png)

**Step2.方案總管加入子視窗表單**

![image_thumb_1.png](/images/posts/7867/image_thumb_1.png)

**Step3.子視窗表單的WindwoState屬性設為Maximized**

![image_thumb_2.png](/images/posts/7867/image_thumb_2.png)

**Step4.在MDI主表單工具列上的按鈕點兩下，並在處理函式內加入下列的Code**

```
Dim f As New Form2
f.MdiParent = Me
f.Show()
```

**Step5.執行**

點選工具列上按鈕兩下，會看到有怪現象發生。可以從下圖看到表單介面已有最大化的跡象，但是子視窗卻無最大化的效果。

![image_thumb_3.png](/images/posts/7867/image_thumb_3.png)

## 如何避免

要避免該現象的發生，在子表單中不要設定WindowState屬性，而改用程式碼在Show之前設定。

```
Dim f As New Form2
f.MdiParent = Me
f.WindowState = FormWindowState.Maximized
f.Show()
```
