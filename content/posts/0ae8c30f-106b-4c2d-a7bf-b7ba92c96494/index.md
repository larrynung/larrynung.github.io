---
title: "XMind出現_JVM terminated. Exit code 1_異常訊息的修復方法"
date: "2013-11-06 12:00:00"
tags: [XMind]
description: "這一兩天我的Xmind每次開啟就會出現\"JVM terminated. Exit code 1\"的異常訊息，畫面如下方所示： 這樣的錯誤會讓整個程式無法開啟，重灌後仍然是異常的，最後找到網路上的解法才得以修復，"
---

這一兩天我的Xmind每次開啟就會出現"JVM terminated. Exit code 1"的異常訊息，畫面如下方所示：

![image_thumb.png](/images/posts/0ae8c30f-106b-4c2d-a7bf-b7ba92c96494/image_thumb.png)

這樣的錯誤會讓整個程式無法開啟，重灌後仍然是異常的，最後找到網路上的解法才得以修復，解決方法是將Xmind安裝目錄下的XMind.ini文件(預設路徑為C:\Program Files\XMind\xmind.ini)開啟。

![image_thumb_2.png](/images/posts/0ae8c30f-106b-4c2d-a7bf-b7ba92c96494/image_thumb_2.png)

開啟後將下面這三行自XMind.ini中刪除。

-Xms128m
-Xmx512m
-XX:MaxPermSize=256m

![image_thumb_1.png](/images/posts/0ae8c30f-106b-4c2d-a7bf-b7ba92c96494/image_thumb_1.png)

儲存後關閉問題就會修復了。

## Link

* 安裝後無法執行程式: JVM terminated. Exit code =-1
