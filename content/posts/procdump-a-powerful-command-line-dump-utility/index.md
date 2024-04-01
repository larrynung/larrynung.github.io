---
title: "ProcDump - A powerful command line dump utility"
date: "2014-01-20 23:11:00"
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
               with the following syntax: "\Process(<name>_<pid>)