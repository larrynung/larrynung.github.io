---
title: "[WPF]Using Windows Forms Controls in WPF"
slug: "wpf-using-windows-forms-controls-in-wpf"
aliases: ["/posts/7929/"]
date: "2009-04-09 12:29:05"
description: "欲在WPF中使用Windows Form控制項，我們可以使用WindowsFormsHost控制項來達成此需求。 Step1.放入WindowsFormsHost控制項 放入控制項後可看到如下畫面： Step2.加入System.Windows.Forms參考…"
tags: [WPF]
---

欲在WPF中使用Windows Form控制項，我們可以使用WindowsFormsHost控制項來達成此需求。

**Step1.放入WindowsFormsHost控制項**

![image_thumb.png](/images/posts/7929/image_thumb.png)

放入控制項後可看到如下畫面：

![image_thumb_1.png](/images/posts/7929/image_thumb_1.png)

**Step2.加入System.Windows.Forms參考**

![image_thumb_2.png](/images/posts/7929/image_thumb_2.png)

**Step3.在XAML文件中加入命名空間**

![image_thumb_3.png](/images/posts/7929/image_thumb_3.png)

**Step4.在XAML文件中加入Windows Forms控制項**

![image_thumb_4.png](/images/posts/7929/image_thumb_4.png)

![image_thumb_5.png](/images/posts/7929/image_thumb_5.png)
