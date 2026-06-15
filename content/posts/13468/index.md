---
title: "[Visual Studio]Fixldquo;The application cannot startrdquo;"
date: "2010-02-03 11:56:17"
description: "[Visual Studio]Fix“The application cannot start”"
tags: [Visual Studio]
---

最近在使用Visual Studio 2010 Beta2，開啟時出現"The application cannot start"的錯誤，按下確定後Visual Studio就自動關閉了。

![image_thumb.png](/images/posts/13468/image_thumb.png)

這問題發生後無法直接啟動Visual Studio，卻可以透過連點程式碼來開啟。

經查詢這問題有很多可能會造成，像是：

1. IDE 無法載入 Msxml3.dll。
2. IDE 無法載入 Mso.dll。
3. IDE 無法載入 DTE.olb。
4. 安裝時並未建立 Visual Studio .NET 的授權識別碼。
5. 已開啟指令碼封鎖，無法執行指令碼。
6. Visual Studio .NET 的 .NET Framework 安裝部分，無法為 mscorlib.dll 產生有效的原生影像。
7. 出現 Klez 病毒。

多半都是缺少或是毀損了某些檔案所導致，可自行參考MSDN的[The application cannot start](http://msdn.microsoft.com/en-us/library/ect3fzs0(VS.80).aspx)來修復，或使用procmon來找尋引起問題的原因。

在Visual Studio 2010 Beta2中，又多了兩個原因會導致這樣的問題。

1. 匯入先前Visual Studio的設定檔，其內含non-TrueType字型。
2. 不正確的window profile。像是把視窗調為浮動狀態後縮小Visual Studio關閉。

這兩個問題在Visual Studio 2010 RTM就會被修復，在RTM出來之前，我們可以透過還原設定的方式來修復這個問題。只要在命令提示字元中，鍵入下列命令：

devenv /resetuserdata

若使用的是Express版，可參閱下列命令：

* For Visual Basic Express type, “vbexpress /resetuserdata”
* For Visual C# Express type, “vcsexpress /resetuserdata”
* For Visual C++ Express type, “vcexpress /resetuserdata”
* For Visual Wed Developer Express type, “vwdexpress /resetuserdata”

## Link

* [The application cannot start.](http://msdn.microsoft.com/en-us/library/ect3fzs0(VS.80).aspx)
* [How to Fix “The application cannot start” Error](http://blogs.msdn.com/visualstudio/archive/2009/10/29/how-to-fix-the-application-cannot-start-error.aspx)
* [VS 2010 Beta2: Workaround for Raster Font Settings Issue](http://blogs.msdn.com/visualstudio/archive/2009/10/27/VS-2010-Beta2_3A00_--Workaround-for-Raster-Font-Settings-Issue.aspx)
* [啟動 Visual IDE 後，Visual IDE 並未開啟，或者出現「應用程式無法啟動」錯誤訊息](http://support.microsoft.com/kb/306905)
