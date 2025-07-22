---
title: "[VB.NET]突破Disable按鈕的封鎖與限制"
date: "2009-05-28 01:28:08"
description: "[VB.NET]突破Disable按鈕的封鎖與限制"
tags: [VB.NET]
---

## Introduction

一般來說，當我們程式中有部份功能欲不讓使用者使用時。通常我們會把按鈕給Disable掉，讓使用者無法執行特定的功能。但這樣做真的就安全嗎？答案是否定的。其實光是把按鈕給Disable掉是很容易破解的，在對岸就已有許多破解工具 (e.x. 按鈕突破大師)，因此在編碼上最好還是要在程式中自行加上判斷，讓按鈕就算被突破也無法執行。

## 突破Disable按鈕的封鎖與限制

欲突破Disable按鈕的封鎖與限制，其實很簡單。只要透過Win32 API即可達成。

需要使用的API有：
ChildWindowFromPointGetForegroundWindowIsWindowEnabledEnableWindowGetCursorPosScreenToClient

程式流程如下：

程式範例如下：

MFC

VB.NET

執行後我們把滑鼠移到Disable的按鈕上，按鈕就會被強制變回Enable狀態了。變回Enable的按鈕也變得可以按下與執行。

## 執行步驟
Step1.開啟按鈕突破程式
 
Step2.開啟欲突破的程式
 
Step3.啟動按鈕突破功能
 
Step4.把滑鼠移到欲突破的按鈕上
當滑鼠移到欲突破的Disable按鈕上，按鈕會被強制設回Enable。

P.S.
上述範例對.NET程式的按鈕無效，請使用非.NET程式來測試。雖範例無法達到突破.NET按鈕，但這不代表.NET程式不需注意這問題。因為能突破.NET按鈕的工具確實存在(e.x. Enable.NET)。雖範例只能把Disable按鈕設為Enable，但其實運用同樣的概念也可以把隱藏的元件顯示出來。

## Conclusion

此篇的主旨不是要教程式員破解，而是要提醒設計員在程式的設計上不是只要把按鈕給Disable掉就安全了。還是要額外利用Code去判斷是否可以執行才是較為安全的作法，尤其是程式中重要的功能更是要加以防堵。