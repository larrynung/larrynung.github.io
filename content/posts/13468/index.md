---
title: "[Visual Studio]Fixldquo;The application cannot startrdquo;"
date: "2010-02-03 11:56:17"
description: "[Visual Studio]Fix&ldquo;The application cannot start&rdquo;"
tags: [Visual Studio]
---

最近在使用Visual Studio 2010 Beta2，開啟時出現"The application cannot start"的錯誤，按下確定後Visual Studio就自動關閉了。

這問題發生後無法直接啟動Visual Studio，卻可以透過連點程式碼來開啟。

經查詢這問題有很多可能會造成，像是：
     IDE 無法載入 Msxml3.dll。    IDE 無法載入 Mso.dll。    IDE 無法載入 DTE.olb。     安裝時並未建立 Visual Studio .NET 的授權識別碼。     已開啟指令碼封鎖，無法執行指令碼。     Visual Studio .NET 的 .NET Framework 安裝部分，無法為 mscorlib.dll 產生有效的原生影像。     出現 Klez 病毒。   
 
  多半都是缺少或是毀損了某些檔案所導致，可自行參考MSDN的The application cannot start來修復，或使用procmon來找尋引起問題的原因。  

在Visual Studio 2010 Beta2中，又多了兩個原因會導致這樣的問題。
     匯入先前Visual Studio的設定檔，其內含non-TrueType字型。    不正確的window profile。像是把視窗調為浮動狀態後縮小Visual Studio關閉。   

這兩個問題在Visual Studio 2010 RTM就會被修復，在RTM出來之前，我們可以透過還原設定的方式來修復這個問題。只要在命令提示字元中，鍵入下列命令：
  
devenv /resetuserdata

若使用的是Express版，可參閱下列命令：
  For Visual Basic Express type, “vbexpress /resetuserdata”   For Visual C# Express type, “vcsexpress /resetuserdata”   For Visual C++ Express type, “vcexpress /resetuserdata”   For Visual Wed Developer Express type, “vwdexpress /resetuserdata”   

## Link
     The application cannot start.     How to Fix “The application cannot start” Error     VS 2010 Beta2: Workaround for Raster Font Settings Issue    啟動 Visual IDE 後，Visual IDE 並未開啟，或者出現「應用程式無法啟動」錯誤訊息