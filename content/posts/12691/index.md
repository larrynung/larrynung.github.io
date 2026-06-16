---
title: "[Software]The Regular"
date: "2009-12-27 01:24:30"
description: "Introduction The Regular是ㄧ套用來撰寫測試.NET正規表示式的輔助工具。作者是Roy Osherove。該軟體主要提供Match、Replace、Split、Generate Code、Intellisense、Code Snippets、Web Search、Regex…"
tags: [Software]
---

## Introduction

The Regular是ㄧ套用來撰寫測試.NET正規表示式的輔助工具。作者是Roy Osherove。該軟體主要提供Match、Replace、Split、Generate Code、Intellisense、Code Snippets、Web Search、Regex Analyzer…等功能，其與知名網站RegexLib.Com也有做相當的整合。

在使用上主要可以分為下列三個主要區塊。

![image5_thumb.png](/images/posts/12691/image5_thumb.png)

上方區塊主要是用來編寫正規表示式；左下區塊是用來顯示匹配、取代、分割的結果與其處理時間；右下區塊是用來帶入要用來測試正規表示式的資料。

## Match Regex

若要使用The Regular匹配正規表示式，我們可以如下操作：

**Step1.在上方編輯區塊中打入要匹配的正規表示式**

當鍵入正規表示式，程式會彈出Intellisense功能提式輔助使用者編寫正規表示式。這邊強烈建議到[View]→[Options]中把Intellisense功能關閉，因為這套軟體個人在使用上覺得Bug還算滿多的，使用Intellisense常會讓版面亂掉無法復原。

![image_thumb.png](/images/posts/12691/image_thumb.png)

**Step2.在右下編輯區塊輸入要帶入測試的資料**

要帶入測試資料，我們可以直接在編輯區塊內輸入。

![image30_thumb.png](/images/posts/12691/image30_thumb.png)

也可以透過上方的讀檔按鈕或是輸入框、從檔案中載入測試資料。

![image11_thumb.png](/images/posts/12691/image11_thumb.png)

![image17_thumb.png](/images/posts/12691/image17_thumb.png)

**Step3.按下工具列上的[Match]按鈕或是熱鍵F5來做匹配的動作**

匹配完後，匹配的結果會顯示在左下區塊。

![image20_thumb.png](/images/posts/12691/image20_thumb.png)

## Replace Regex

**Step1.在上方編輯區塊中打入要取代的正規表示式**

**Step2.在右下編輯區塊輸入要帶入測試的資料**

**Step3.在右下編輯區塊輸入要帶入要取代的資料**

![image54_thumb.png](/images/posts/12691/image54_thumb.png)

**Step4.按下工具列上的[Replace]按鈕或是熱鍵F6來做取代動作**

![image58_thumb.png](/images/posts/12691/image58_thumb.png)

## Split Regex

**Step1.在上方編輯區塊中打入要取代的正規表示式**

**Step2.在右下編輯區塊輸入要帶入測試的資料**

**Step3.按下工具列上的[Split]按鈕或是熱鍵F7來做分割動作**

![image62_thumb.png](/images/posts/12691/image62_thumb.png)

## Generate Code

當正規表示式編好後，我們可以透過[Tools]→[Generate Code…]或熱鍵Ctrl+K來啟動Generate Code視窗。

![image33_thumb.png](/images/posts/12691/image33_thumb.png)

Generate Code視窗會提供VB.NET與C#兩種語言的程式碼

![image36_thumb.png](/images/posts/12691/image36_thumb.png)

其程式碼會把您所輸入的正規表示式Pattern與工具列上所設定的參數給帶入

![image50_thumb.png](/images/posts/12691/image50_thumb.png)

## Snippets

要使用Snippets，首先我們必須透過[View]→[Snippets]或是熱鍵Ctrl+Shift+S啟動SnippetsControl視窗。

![image42_thumb.png](/images/posts/12691/image42_thumb.png)

使用時只需在想套用的Snippets上，用滑鼠左鍵連點兩下即可。

![image39_thumb.png](/images/posts/12691/image39_thumb.png)

## Shortcuts

![image2_thumb.png](/images/posts/12691/image2_thumb.png)

## Link

* [The Regular Download Page – Sourceforge](http://sourceforge.net/projects/regulator/files/The%20Regulator/Regulator2.0%20Binaries%20Only/Regulator20Bin.zip/download)
* [Learn – Test Regular Expressions With The Regulator](http://www.webresourcesdepot.com/learn-test-regular-expressions-with-the-regulator/)
