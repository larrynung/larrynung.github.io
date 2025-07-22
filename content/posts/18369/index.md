---
title: "[Visual Studio]Visual Studio 2010 從類別圖產生程式碼專案出現 quot;(Class) does not existquot; 錯誤"
date: "2010-10-15 12:54:19"
description: "[Visual Studio]Visual Studio 2010 從類別圖產生程式碼專案出現 &quot;(Class) does not exist&quot; 錯誤"
tags: [Visual Studio]
---

今天在使用Visual Studio 2010想把規劃好的UML類別圖，轉換成對應的程式碼專案時，發現不如我之前使用般順利，按了半天對應的程式碼專案就是不出來，看了一下輸出視窗才發現有"(Class) does not exist"錯誤訊息。

但之前筆電使用都好好的，故再細看一下錯誤，發現%LocalAppData%這個環境變數竟然沒有被系統替換。

  查閱了一下網路上Error during code generation of UML model這篇資料。發現這問題只會出在XP，若使用的是Win7則不會發生此現象。要解決這個問題可自行為系統加上LocalAppData這個環境變數，設定其值為"%USERPROFILE%\Local Settings\Application Data"，重開機後再試應該就可以了。        

## Link
     Error during code generation of UML model