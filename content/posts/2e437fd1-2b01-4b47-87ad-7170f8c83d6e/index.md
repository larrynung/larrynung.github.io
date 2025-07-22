---
title: "使用滑鼠右鍵快速產生XML序列化組件"
date: "2013-11-06 12:00:00"
description: "使用滑鼠右鍵快速產生XML序列化組件"
---

之前記錄過一篇使用XML序列化程式產生器工具加速XML序列化，裡面有提到使用建置事件來產生XML序列化組件的方法。但若只想更新XML序列化組件，不想要開啟專案重新建置時，這樣的方法就顯得有點麻煩。此時我們可以透過本篇紀錄的方法用滑鼠右建快速產生XML序列化組件。

只要把下面的內容修改一下放至文字檔中，儲存成附檔名為reg的檔案，用滑鼠點選兩下登陸至註冊檔，滑鼠右鍵中即會出現產生序列化組件的選單。

Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\exefile\shell\Sgen]
@="產生序列化組件"

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\exefile\shell\Sgen