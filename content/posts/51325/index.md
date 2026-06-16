---
title: "[Visual Studio]強制Visual Studio執行垃圾回收"
date: "2011-11-03 09:58:50"
description: "Visual Studio是一個很大的程式，絕大部分採用Managed Code，由很多不同的部門所共同開發，允許整合許多好用的外掛，有時候會吃掉很多的資源，這時我們可以透過Visual Studio內建的功能強制執行垃圾回收。"
tags: [Visual Studio]
---

Visual Studio是一個很大的程式，絕大部分採用Managed Code，由很多不同的部門所共同開發，允許整合許多好用的外掛，有時候會吃掉很多的資源，這時我們可以透過Visual Studio內建的功能強制執行垃圾回收。可以將已經不用的記憶體回收，讓Visual Studio可在更多的記憶體下運行，像是在做效能量測時可能就可以運行這樣的功能清一下被吃掉的資源，減少會影響量測數據的潛在因素。

要使用時按下快速鍵[Ctrl + Shift + Alt + F12]兩次，或是建立個工具列按鈕讓它執行ToolsForceGC的Command就可以了。

![image_thumb.png](/images/posts/51325/image_thumb.png)

這邊筆者實際測試一下，使用Visual Studio開啟一個幾乎是空的WPF專案，光專案開起來記憶體就佔用了145,732K，實體記憶體也總共用了65%。

![image_thumb_1.png](/images/posts/51325/image_thumb_1.png)

將專案關閉，可以看到記憶體的耗費仍是不變。

![image_thumb_2.png](/images/posts/51325/image_thumb_2.png)

強制Visual Studio進行垃圾回收後，記憶體佔用變為121,836K，實體記憶體總佔用量降為63%。

![image_thumb_3.png](/images/posts/51325/image_thumb_3.png)

## Link

* [VS.NET consumes too much memory? Force a GC!](http://dotneteers.net/blogs/petersm/archive/2010/12/16/vs-net-consumes-too-much-memory-force-a-gc.aspx)
* [Force VS to garbage collect](http://blogs.msdn.com/b/camerons/archive/2010/12/15/force-vs-to-garbage-collect.aspx)
* [Force VS to garbage collect](http://jasper-net.blogspot.com/2010/12/force-vs-to-garbage-collect.html)
