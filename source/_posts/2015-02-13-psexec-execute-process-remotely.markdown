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

<br/>


常用的參數有 -c、-i、-l、-w、-s、-u、-p，更多細節可直接輸入 psexec 命令查閱。  

{% img /images/posts/PsExec/2.png %}

<br/>


簡單的說，呼叫時要指定欲操作的遠端電腦，依需求帶入命令與參數就可以了。   

<br/>


像是要單純的讓遠端電腦執行命令，我們就可以直接在後面 psexec 後面加上指定的電腦與欲執行的命令。像是若要查閱遠端電腦的檔案內容我們就可以像下面這樣叫用：      

    psexec \\TWDT092 cmd /c dir d:

{% img /images/posts/PsExec/3.png %}

<Br/>


要查閱遠端電腦的 IP 設定的話：  

    psexec \\TWDT092 -s ipconfig /all

{% img /images/posts/PsExec/4.png %}

<br/>


要執行遠端電腦指定位置的檔案的話：  

    psexec \\TWDT092 c:\bin\test.exe

<br/>


若檔案不存在於遠端電腦，我們也可直接用 psexec 戴上參數 -c 與要執行的檔案，讓 psexec 將指定的檔案傳到遠端電腦執行： 

    psexec \\TWDT092 -c test.exe

<br/>


若需要身分驗證的話，可以在後面用參數 -u 帶入 帳號、參數 -p 帶入密碼：  

    psexec \\TWDT092 ipconfig /all -u larrynung -p 123456

<br/>


像上面介紹的方式都是一次性的叫用，每次叫用遠端電腦都會帶起 psexecsvc 服務，讓 psexec 得以進行連線並運行命令。若有很多命令要處理，且無法寫成批次的話，我們也可以像下面這樣建立連線後互動處理：  

    psexec \\TWDT092 cmd

{% img /images/posts/PsExec/5.png %}

<br/>


下完命令後 psexec 會連到遠端電腦的命令提示字元，使用上就像是在本地叫用命令一般，直到我們輸入 exit 退出。  

{% img /images/posts/PsExec/6.png %}

<br/>


最後我們可以看個 YouTube 的教學體驗一下 PsExec 的使用。  

<iframe width="640" height="480" src="https://www.youtube.com/embed/MaAL3C-DuHQ" frameborder="0" allowfullscreen></iframe>

<br/>


Link
----
* [PsExec](https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx)
* [PsTools 之 PsExec 的用法 @ 暉獲無度的步烙閣 :: 隨意窩 Xuite日誌](http://blog.xuite.net/jyoutw/xtech/24607577-PsTools+%E4%B9%8B+PsExec+%E7%9A%84%E7%94%A8%E6%B3%95)
* [動態網頁好好玩: PsExec簡介](http://andyshyu.blogspot.tw/2009/07/psexec.html)
* [PsExec - Execute process remotely | Windows CMD | SS64.com](http://ss64.com/nt/psexec.html)
* [PSexec Tutorial - YouTube](https://www.youtube.com/watch?v=MaAL3C-DuHQ)
