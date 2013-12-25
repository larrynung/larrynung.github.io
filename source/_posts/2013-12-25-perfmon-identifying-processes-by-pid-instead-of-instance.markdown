---
layout: post
title: "Perfmon - Identifying processes by PID instead of instance"
date: 2013-12-25 15:52
comments: true
categories: 
keywords: 
description: "Perfmon - Identifying processes by PID instead of instance"
---

在使用效能監視器時，當程式多開，各自有不同的 Process 時，效能監視器會在 Process 後面加上 #n 為後綴 (n 為流水號)。  

<!--More-->

{% img /images/posts/PerfmonWithPID/1.png %}


這樣在使用效能監視器，我們就很難區別哪個才是我們想要關注的 Process。  

此時，我們可以開啟登錄檔，找到 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PerfProc\Performance` ，然後加入一個 DWORD 值 ProcessNameFormat ,並設定其值為 2(要關閉的話將其值設為1)。  

{% img /images/posts/PerfmonWithPID/2.png %}

{% img /images/posts/PerfmonWithPID/3.png %}

{% img /images/posts/PerfmonWithPID/4.png %}


重啟效能監視器，可看到本來看到的後綴會變成 Process ID，使用效能監視器時會比較好區別監看的 Process。  

{% img /images/posts/PerfmonWithPID/5.png %}


Link
----
* [Perfmon: Identifying processes by PID instead of instance](http://blogs.technet.com/b/askperf/archive/2010/03/30/perfmon-identifying-processes-by-pid-instead-of-instance.aspx)
