---
title: "解決Web安裝專案無法在IIS7下安裝的問題"
date: "2013-11-06 12:00:00"
description: "解決Web安裝專案無法在IIS7下安裝的問題"
---

若遇到透過Visual Studio包出的Web安裝程式在XP下運行正常，但卻無法在Vista、Windows Srever 2008、Win7下正常執行，出現下方的錯誤畫面。

此時若在Win7的話，可透過點選[控制台]→[程式集]→[開啟或關閉Windows功能]，開啟Windows功能對話框。

在彈出的Windows功能對話框中，勾選[IIS Metabase及IIS 6設定相容性]，再次運行安裝程式即可正常運行。

  如果作業系統是Win2008的可自行參閱VS2008 Web Setup Project and Win2008。  

## Link
     Troubleshooting Windows Installer Deployment    Making Web Setup projects run on Windows Vista    Visual Studio 2008 and IIS 7    Windows 2008 & Visual Studio Web Setup: The installer was interrupted before ApplicationName could be installed    Managing IIS 6.0 Servers from Windows Vista (and other Management Stuff)    VS2008 Web Setup Project and Win2008