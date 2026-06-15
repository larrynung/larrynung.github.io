---
title: "[WPF]Windows Form程式使用WPF控制項"
date: "2009-04-08 12:34:45"
description: "[WPF]Windows Form程式使用WPF控制項"
tags: [WPF]
---

![image_thumb_9.png](/images/posts/7916/image_thumb_9.png)

在Windows Form程式中若欲使用WPF，我們可以很簡單的透過ElementHost控制項來達成。

## 步驟

操作步驟如下：

**Step1.加入WPF控制項到方案**

![image_thumb.png](/images/posts/7916/image_thumb.png)

**Step2.加入ElementHost控制項到表單**

![image_thumb_1.png](/images/posts/7916/image_thumb_1.png)

![image_thumb_2.png](/images/posts/7916/image_thumb_2.png)

**Step3.建置專案**

**Step4.設定ElementHost控制項的裝載內容為Step1中加的WPF控制項**

可以直接透過控制項的智慧標籤來設定。

![image_thumb_4.png](/images/posts/7916/image_thumb_4.png)

或是透過ElementHost控制項的Child屬性設定。

![image_thumb_5.png](/images/posts/7916/image_thumb_5.png)

設定完後即可看到效果。

![image_thumb_6.png](/images/posts/7916/image_thumb_6.png)

![image_thumb_3.png](/images/posts/7916/image_thumb_3.png)
