---
title: "XMind出現_JVM terminated. Exit code 1_異常訊息的修復方法"
date: "2013-11-06 12:00:00"
description: "XMind出現_JVM terminated. Exit code 1_異常訊息的修復方法"
---

這一兩天我的Xmind每次開啟就會出現"JVM terminated. Exit code 1"的異常訊息，畫面如下方所示：

這樣的錯誤會讓整個程式無法開啟，重灌後仍然是異常的，最後找到網路上的解法才得以修復，解決方法是將Xmind安裝目錄下的XMind.ini文件(預設路徑為C:\Program Files\XMind\xmind.ini)開啟。

開啟後將下面這三行自XMind.ini中刪除。

-Xms128m  

-Xmx512m  

-XX:MaxPermSize=256m

儲存後關閉問題就會修復了。

## Link


安裝後無法執行程式: JVM terminated. Exit code =-1