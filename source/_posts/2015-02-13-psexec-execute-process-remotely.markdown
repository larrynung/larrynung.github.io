---
layout: post
title: "PsExec - Execute process remotely"
date: 2015-02-13 20:26
comments: true
categories: 
keywords: "PsExec"
description: "PsExec - Execute process remotely"
---

PsExec 是一命令列工具，可讓我們執行遠端電腦的程式。  

<!-- More -->

<br/>


使用前請先至 [PsExec](https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx) 下載。  

{% img /images/posts/PsExec/1.png %}

<br/>


使用方式如下。  

    psexec [\\computer[,computer2[,...] | @file]][-u user [-p psswd][-n s][-r servicename][-h][-l][-s|-e][-x][-i [session]][-c [-f|-v]][-w directory][-d][-<priority>][-a n,n,...] cmd [arguments]


簡單的說，呼叫時要指定欲操作的遠端電腦，依需求帶入命令與參數就可以了。像是要查閱遠端電腦的檔案內容我們就可以像下面這樣叫用：      

    psexec \\TWDT092 cmd /c dir d:

{% img /images/posts/PsExec/2.png %}

<Br/>


要查閱遠端電腦的 IP 設定，可像下面這樣直接在後面加入命令：  

    psexec \\TWDT092 -s ipconfig /all

{% img /images/posts/PsExec/3.png %}

<br/>


要執行遠端電腦的檔案，可像下面這樣直接指定遠端電腦的檔案位置：  

    psexec \\TWDT092 c:\bin\test.exe

<br/>


要將檔案傳到遠端電腦執行，可帶參數 -c 與要執行的檔案： 

    psexec \\TWDT092 -c test.exe

<br/>


要做身分驗證的話，用參數 -u 帶入 帳號，參數 -p 帶入密碼：  

    psexec \\TWDT092 ipconfig /all -u larrynung -p 123456

<br/>


像上面這樣叫用每次遠端電腦都會帶起 psexecsvc 服務，讓 psexec 進行連線後運行命令。若有很多命令要處理，且無法寫成批次的話，我們也可以像下面這樣建立連線後互動處理：  

    psexec \\TWDT092 cmd

{% img /images/posts/PsExec/4.png %}

<br/>


下完命令後會連到遠端電腦的命令提示字元，可以像在本地般叫用命令，直到我們輸入 exit 退出。  

{% img /images/posts/PsExec/5.png %}

<br/>


Link
----
* [PsExec](https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx)
* [PsTools 之 PsExec 的用法 @ 暉獲無度的步烙閣 :: 隨意窩 Xuite日誌](http://blog.xuite.net/jyoutw/xtech/24607577-PsTools+%E4%B9%8B+PsExec+%E7%9A%84%E7%94%A8%E6%B3%95)
* [動態網頁好好玩: PsExec簡介](http://andyshyu.blogspot.tw/2009/07/psexec.html)
* [PsExec - Execute process remotely | Windows CMD | SS64.com](http://ss64.com/nt/psexec.html)
* [PSexec Tutorial - YouTube](https://www.youtube.com/watch?v=MaAL3C-DuHQ)
