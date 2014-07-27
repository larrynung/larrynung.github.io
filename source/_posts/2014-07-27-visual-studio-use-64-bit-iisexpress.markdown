---
layout: post
title: "Visual Studio - Use 64 Bit IISExpress"
date: 2014-07-27 23:11
comments: true
categories: [Visual Studio]
keywords: "Visual Studio, 64 bit, iisexpress"
description: "Visual Studio - Use 64 Bit IISExpress"
---

雖然 .Net 程式支援位元適應性，Visual Studio 也允許我們做 64 位元的網站開發，但 Visual Studio 預設啟用的 IISExpress 是 32位元的，所以當在做 64 位元的網站開發時，在本地端測試我們會發現網站會跑不起來，因為 64 位元的網站無法跑在 32 位元的 IISExpress 上。

<!-- More -->

<br/>

這時要馬要改用 IIS 去跑，要馬就是要像像下面這樣輸入命令修改登錄檔，將 Visual Studio 設定為使用 64 位元的 IISExpress：

    reg add HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\11.0\WebProjects /v Use64BitIISExpress /t REG_DWORD /d 1

注意到這邊，登錄檔位置依 Visual Studio 版本不同會有所差異，請自行視個人需求下去調整。

