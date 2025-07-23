---
title: "[VC.NET]VC.NET表單無法開啟表單設計畫面的解決辦法"
date: "2010-06-08 10:27:47"
description: "[VC.NET]VC.NET表單無法開啟表單設計畫面的解決辦法"
tags: [C++]
---

有用過VC.NET的可能都有發現，已經編輯好的表單有時會變成像一般的標頭檔一樣，怎樣都無法切換回表單設計畫面，最後只得用修改程式碼的方式來調整介面。

多半這種問題是因為從別的專案做加入檔案至專案的動作所導致，舉個例子來說，假設今天有個表單Form1。

![image_thumb_1.png](/images/posts/15725/image_thumb_1.png)

我們把他從專案中移除

![image_thumb_2.png](/images/posts/15725/image_thumb_2.png)

在到方案總管上按下滑鼠右鍵，點選[Add]→[Existing Item…]，把檔案加回至專案中。此時本來應該是表單的Form1，就會變得像標頭檔一樣的圖示，且連續點擊或是按下滑鼠右鍵，都無法再次切換製表單設計畫面。

![image_thumb_3.png](/images/posts/15725/image_thumb_3.png)

要解決這樣的問題可在方案總管上選取表單的標頭檔，切到屬性視窗，將File Type屬性從C++ Header File切回至C++ Form就可以了。

![image_thumb_4.png](/images/posts/15725/image_thumb_4.png)
