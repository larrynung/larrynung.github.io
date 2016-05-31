---
layout: post
title: "ProcDump - A powerful command line dump utility"
date: 2014-01-20 23:11:00
comments: true
tags: 
keywords: "Dump, ProcDump, Utility"
description: "ProcDump - A powerful command line dump utility"
---

ProcDump 是ㄧ命令列 Dump 工具。能監控 Process 狀態，在滿足特定的條件時自動產生 Dump 文件。  

<!-- More -->

<br/>

像是我們常常會要在 CPU 飆高時或是應用程式無回應做些分析，若用工作管理員去手動產生 Dump 文件，我們可能會無法準確的抓到要 Dump 的時機。而若用一些分析工具，多半要額外安裝，又會 Dump 出太多不相關的資訊。

<br/>

在這種清況下， ProcDump 就特別好用。程式小巧可攜，又可彈性的設定 Dump 的條件，準確的 Dump 出我們想要的資訊。  

<br/>

程式主檔可至 [ProcDump - TechNet - Microsoft](http://technet.microsoft.com/zh-tw/sysinternals/dd996900.aspx) 這邊下載  

{% img /images/posts/ProcDump/1.png %}

<br/>

下載完後可直接呼叫命令查閱使用方式以及使用參數  

    ProcDump v6.00 - Writes process dump files
    Copyright (C) 2009-2013 Mark Russinovich
    Sysinternals - www.sysinternals.com
    With contributions from Andrew Richards

    Monitors a process and writes a dump file when the process exceeds the
    specified criteria or has an exception.

    usage: procdump [-64] [[-c|-cl CPU usage] [-u] [-s seconds]] [-n exceeds] [-e [1 [-b] [-f <filter,...>] [-g]]] [-h] [-l] [-m|-ml commit usage] [-ma | -mp] [-o] [-p|-pl counter threshold] [-r] [-t] [-d <callback DLL>] <[-w] <process name or service name or PID> [dump file] | -i <dump file> | -x <dump file> <image file> [arguments] >

       -64     By default ProcDump will capture a 32-bit dump of a 32-bit process
               when running on 64-bit Windows. This option overrides to create a
               64-bit dump.
       -b      Treat debug breakpoints as exceptions (otherwise ignore them).
       -c      CPU threshold above which to create a dump of the process.
       -cl     CPU threshold below which to create a dump of the process.
       -d      Invoke the minidump callback routine named MiniDumpCallbackRoutine
               of the specified DLL.
       -e      Write a dump when the process encounters an unhandled exception.
               Include the 1 to create dump on first chance exceptions.
       -f      Filter the first chance exceptions. Wildcards (*) are supported.
           To just display the names without dumping, use a blank ("") filter.
       -g      Only capture native exceptions in a managed process (no interop).
       -h      Write dump if process has a hung window (does not respond to
               window messages for at least 5 seconds).
       -i      Install ProcDump as the AeDebug postmortem debugger.
               Only -ma, -mp and -d are supported as options.
       -l      Display the debug string logging of the process.
       -m      Memory commit threshold in MB at which to create a dump of the
               process.
       -ml     Trigger when memory commit drops below specified MB value.
       -ma     Write a dump file with all process memory. The default
               dump format only includes thread and handle information.
       -mp     Write a dump file with thread and handle information, and all
               read/write process memory. To minimize dump size, memory areas
               larger than 512MB are searched for, and if found, the largest
               area is excluded. A memory area is the collection of same
               sized memory allocation areas. The removal of this (cache)
               memory reduces Exchange and SQL Server dumps by over 90%.
       -n      Number of dumps to write before exiting.
       -o      Overwrite an existing dump file.
       -p      Trigger on the specified performance counter when the threshold
               is exceeded. Note: to specify a process counter when there are
               multiple instances of the process running, use the process ID
               with the following syntax: "\Process(<name>_<pid>)\counter"
       -pl     Trigger wehen performance counter falls below the specified value.
       -r      Reflect (clone) the process for the dump to minimize the time
               the process is suspended (Windows 7 and higher only).
       -s      Consecutive seconds before dump is written (default is 10).
       -t      Write a dump when the process terminates.
       -u      Treat CPU usage relative to a single core.
       -w      Wait for the specified process to launch if it's not running.
       -x      Launch the specified image with optional arguments.
               If it is a Modern Application or Package, ProcDump will start
               on the next activation (only).

    Use the -accepteula command line option to automatically accept the
    Sysinternals license agreement.

    Use -? -e to see example command lines.

    If you omit the dump file name, it defaults to <processname>_<datetime>.dmp.


其中比較常用的參數有  

    -b 將除錯的中斷點視為例外
    -c CPU 使用率到達時生成 Dump 文件
    -cl 在CPU使用率低於這個閥值的時候,生成dump文件.
    -d 當產生Dump文件時呼叫指定DLL內的Callback方法
    -e 指定當未處理的例外發生時產生 Dump 文件。後面帶 1 則當 first chance exception 發生時產生 Dump 文件
    -f 過濾 first chance exceptions ，帶""表示只顯示不Dump
    -g 只攔截原生的例外
    -h 當視窗無回應時產生 Dump 文件 (視窗無法回應視窗訊息至少 5 秒)
    -l 顯示處理序的除錯訊息
    -m 記憶體用到指定的 MB 時產生Dump文件
    -ma Full Dump Process 。預設只 Dump 包括線程和句柄資訊.
    -ml 記憶體掉到特定 MB 時產生 Dump 文件
    -n 退出前要抓取多少 Dump 文件
    -o 覆寫指定 Dump 文件
    -p 指定特定的效能監視器到達指定值時產生 Dump 文件
    -pl 指定特定的效能監視器低於指定值時產生 Dump 文件
    -s 持續幾秒才抓取 Dump 文件(預設值為 10)
    -t 處理序退出時產生 Dump 文件
    -u 將 CPU 使用率視為單核心電腦來看
    -w 等待特定的處理序運行


使用上只要依需求帶上參數與設定值，接著帶入要 Dump 的 Process Name 或是 ID，若有需要再帶上 Dump 出來的檔案位置就可以了。  

<br/>

最後這邊直接來看幾個例子熟悉一下...  

<br/>

假設今天要 Dump 記事本的資料，我們可以簡單的叫用 procdump ，並帶入 Process Name 。  

    procdump notepad


要 Full Dump Process ID 為 4572 的 Process ，可以叫用 procdump ，並帶入 Process ID 以及 -ma 參數。  

    procdump -ma 4572


要 Dump 記事本 3 次，每次 5 秒鐘  

    procdump -s 5 -n 3 notepad


要在 CPU 使用率到達 20% 時，Dump 記事本 3 次，每次 5 秒鐘  

    procdump -c 20 -s 5 -n 3 notepad


當 hang.exe 程式 hang 住時，Dump 資料到 hungwindow.dmp  

    procdump -h hang.exe hungwindow.dmp


Dump outlook 當效能監視器 "\Processor(_Total)\%Processor Time"的值到達 20  

    procdump outlook -p "\Processor(_Total)\%Processor Time" 20


顯示 IIS 的 first chance exception  

    procdump -e 1 -f "" w3wp.exe


Link
----
* [ProcDump - TechNet - Microsoft](http://technet.microsoft.com/zh-tw/sysinternals/dd996900.aspx)
