---
title: "[VB.NET]把.NET視窗嵌入.NET視窗或控制項"
date: "2010-01-13 11:36:59"
description: "前好一陣子看到同事在做抽換表單時，利用到了把視窗嵌入視窗或控制項的功能。這邊隨手記錄一下。 要把視窗嵌入視窗，在表單的宣告上跟平常並無差異，只是多加了把TopLevel屬性設為False，則此表單即可嵌到另一個表單或控制項中。 TopLevel屬性主要是用來指出是否要將表單顯示為最上層視窗。"
tags: [VB.NET]
---

前好一陣子看到同事在做抽換表單時，利用到了把視窗嵌入視窗或控制項的功能。這邊隨手記錄一下。

要把視窗嵌入視窗，在表單的宣告上跟平常並無差異，只是多加了把TopLevel屬性設為False，則此表單即可嵌到另一個表單或控制項中。

TopLevel屬性主要是用來指出是否要將表單顯示為最上層視窗。最上層表單是沒有父表單的視窗，或它的父表單為桌面視窗。最上層視窗通常在應用程式中當做主表單使用。

若未加入把TopLevel屬性設為False，則在表單嵌入時上會發生ArgumentException was unhandled的例外。![image_thumb.png](/images/posts/13004/image_thumb.png)

要把表單嵌入到另一個表單或控制項，主要操作步驟如下：

1. 宣告表單物件
2. 把表單物件的TopLevel屬性設為False
3. 把表單嵌入另一個表單或控制項

![image_thumb_1.png](/images/posts/13004/image_thumb_1.png)

簡單的程式碼範例如下：

```vb
Dim f As New Form
f.TopLevel = False
f.Parent = Me
f.Show()
```

嵌入的表單在使用上仍可以拖曳、縮小、放大、與關閉，操作就跟一般的視窗一樣，不同的只是它的活動範圍被限制在另一個視窗或控制項內。

若要用此方法來做抽換表單，可把視窗的FormBorderStyle設為None，並把它嵌到欲放置的控制項。

## 程式範例

程式範例如下：

```vb
Public Class Form1
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim f As New Form
        f.TopLevel = False
        f.Parent = Me
        f.Show()
    End Sub
End Class
```

執行結果：

![image_thumb_2.png](/images/posts/13004/image_thumb_2.png) ![image_thumb_4.png](/images/posts/13004/image_thumb_4.png)

![image_thumb_7.png](/images/posts/13004/image_thumb_7.png)![image_thumb_6.png](/images/posts/13004/image_thumb_6.png)

## Link

* Form.TopLevel 屬性
