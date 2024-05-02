---
title: "Batch - Run as administrator"
date: "2014-01-01 22:36:00"
description: "Batch - Run as administrator"
tags: [Batch]
---


Windows Vista 後的作業系統開始導入 UAC ，在運行某些操作時必須要提升至管理者權限才能繼續。這在程式中只要加上 MetaData 就可以了，但在批次檔中卻沒有比較直接的做法。

<!-- More -->

好在有好心的網友整理好了下面這樣的程式碼片段

```bat
:: BatchGotAdmin
:-------------------------------------
REM --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32