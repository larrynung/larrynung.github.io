---
title: "[VB.NET]從登錄檔中讀取CPU資訊"
date: "2009-07-03 12:00:52"
description: "[VB.NET]從登錄檔中讀取CPU資訊"
tags: [VB.NET]
---

要由登錄檔中讀取CPU資訊。首先，我們必需要了解CPU資訊是存放在登錄檔的何處。讓我們看一下下圖：

由圖中可知，CPU資訊是存放在[HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System\CentralProcessor]中，其中~MHZ是指CPU的時脈、ProcessorNameStrin是CPU詳細描述文字、VendorIdentifier是指製造廠商。

了解了CPU資訊在登錄檔中存放的位置後，我們只要能透過程式到對應的位置讀取出值來，一個簡單的CPU資訊獲取程式就完成了。

完整範例如下：

執行結果：