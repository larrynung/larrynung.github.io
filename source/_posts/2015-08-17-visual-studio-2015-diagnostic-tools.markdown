---
layout: post
title: "Visual Studio 2015 - Diagnostic Tools"
date: 2015-08-17 21:54
comments: true
categories: [Visual Studio]
keywords: "Visual Studio"
description: "Visual Studio 2015 - Diagnostic Tools"
---

Diagnostic Tools 是 Visual Studio 2015 的新功能，能幫助開發人員快速的找出效能上的問題。  

<!-- More -->

<br/>


該功能預設除錯時會自動帶出，畫面會像下面這樣。  


{% img /images/posts/DiagnosticTools/1.png %}

<br/>



一邊運行，一邊就會將 CPU、記憶體、與 Event 的狀態帶出。有效能問題開發人員可以即早發現。像這邊的記憶體曲線看起來雖然是平的，但是可以看到有很多次的 GC 出現，這就是需要進行調整的。    

{% img /images/posts/DiagnosticTools/2.png %}

<br/>


記憶體這邊的診斷上我們可以用快照比對分析。只要簡單的進行快照，Diagnostic Tools 就會將兩個快照間的差異清楚的呈現。像是這邊就可以看到物件數跟 Heap 大小有上升的趨勢。進一步點擊，我們可以查看是被哪些物件佔用的，增加的又是哪些物件。   

{% img /images/posts/DiagnosticTools/3.png %}

<br/>

Link
----
* [Performance and Diagnostic Tools in Visual Studio 2015 - Microsoft Application Lifecycle Management - Site Home - MSDN Blogs](http://blogs.msdn.com/b/visualstudioalm/archive/2015/07/20/performance-and-diagnostic-tools-in-visual-studio-2015.aspx)
* [Visual Studio 2015 Diagnostics Investments - The Visual Studio Blog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/visualstudio/archive/2015/07/23/visual-studio-2015-diagnostics-investments.aspx)
