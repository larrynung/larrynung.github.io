---
title: "WinDBG - Check memory leak with dumpheap"
date: "2016-03-19 22:51:00"
description: "WinDBG - Check memory leak with dumpheap"
tags: [WinDBG]
---

要檢查程式的 Memory leak，我們可以在程式物件應該被釋放時抓取 Dump 檔案，像是程式運行後隔一陣子，理論上 GC 應該已經將物件回收時抓取，抓取後就可以用 WinDBG 進一步的分析。

分析時將 WinDBG 開啟，點選 [File | Symbol File Path…] 。

![1.png](/images/posts/CheckMemoryLeakWithWinDBG/1.png)

將 Symbol Server 的位置加入(SRV*c:\symbols*http://msdl.microsoft.com/download/symbols) 。

![2.png](/images/posts/CheckMemoryLeakWithWinDBG/2.png)

接著點選 [File | Open Crash Dump…] 載入 Dump File ( 直接將 Dump 檔拖曳至 WinDBG 也可 )。

![3.png](/images/posts/CheckMemoryLeakWithWinDBG/3.png)

![4.png](/images/posts/CheckMemoryLeakWithWinDBG/4.png)

接著輸入命令 .loadby sos clr，將 SOS 偵錯擴充功能載入。

![5.png](/images/posts/CheckMemoryLeakWithWinDBG/5.png)

再輸入命令 !dumpheap –stat 將 heap state dump 出來。

![6.png](/images/posts/CheckMemoryLeakWithWinDBG/6.png)

我們就可以看到 heap 內有哪些物件、物件數有多少、佔多少空間。

![7.png](/images/posts/CheckMemoryLeakWithWinDBG/7.png)

像是這邊以筆者的程式來說，程式運行後已經放置一陣子，且不該有強引用參考到，理論上 OracleConnection 應該已經釋放且被 GC 回收，但卻還有 790 個物件實體，這部分就是有問題的地方。 

![8.png](/images/posts/CheckMemoryLeakWithWinDBG/8.png)