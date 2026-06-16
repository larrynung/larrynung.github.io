---
title: "[Library][C#]USkin 視窗換膚函式庫"
date: "2009-08-28 10:19:24"
description: "Introduction USkin是一個可以讓應用程式換膚用的函式庫。可讓應用程式套用不同的主題，讓介面有別於其它視窗。 Feature 支援 Microsoft Window's Theme 檔 支援通用控制項 支援新控制項 (像是 ToolStrip/MenuStrip) 支援…"
tags: [Library, CSharp]
---

## Introduction

USkin是一個可以讓應用程式換膚用的函式庫。可讓應用程式套用不同的主題，讓介面有別於其它視窗。

## Feature

* 支援 Microsoft Window's Theme 檔
* 支援通用控制項
* 支援新控制項 (像是 ToolStrip/MenuStrip)
* 支援 VC/C#/VB.NET
* 支援系統標準表單，像是檔案對話框、顏色對話框、列印對話框
* 支援客制控制項
* 支援 MDI/SDI/Dialog 類型的應用程式
* 只需增加兩行程式即可支援Skin file
* Skin file僅僅約30Kb的大小

## 使用方法

在使用USkin時我們必需要使用到USkin.dll，並利用PInvoke去叫用USkin.dll內部的函式。因此我們可以把USkin.dll加入專案，並設定屬性讓它在編譯時自動複製到輸出目錄。接著我們可以用DllImport來呼叫使用USkin.dll內的函式。為了方便起見，我們可以直接把官網範例的USkinSDK.cs直接加入來用。

![image1_thumb.png](/images/posts/10301/image1_thumb.png)

程式範例如下:

![image_thumb.png](/images/posts/10301/image_thumb.png)

執行結果
![image_thumb_1.png](/images/posts/10301/image_thumb_1.png)

經過Init設定過Skin後，若想要動態載入變換Skin，則我們可以叫用USkinLoadSkin。

```c
USkin.USkinSDK.USkinLoadSkin(@"Vista.msstyles");
```

若有自行編輯介面的需求，可以使用SkinStudio等編輯工具。若想要抓現成的介面樣版可到[msstyles Skins](http://www.skinbase.org/Application/msstyles/135)下載。

## Link

* [USkin V3.0 version published](http://www.neemedia.com/newsite/index.php?category=5)
* [SkinStudio Free 4.6](http://www.softking.com.tw/soft/clickcount.asp?fid3=10769 "http://www.softking.com.tw/soft/clickcount.asp?fid3=10769")
* [USkin V3.0 - 免費漂亮界面製作(1)](http://www.dotblogs.com.tw/flyup2005/archive/2009/07/22/9636.aspx)
* [USkin V3.0 - 免費漂亮界面製作(2)](http://www.dotblogs.com.tw/flyup2005/archive/2009/07/22/9637.aspx)
* [USkin V3.0 - 免費漂亮界面製作(3)](http://www.dotblogs.com.tw/flyup2005/archive/2009/07/23/9645.aspx)
* [The Code Project-Use the Free USkin Toolkit to Skin your Application](http://www.codeproject.com/KB/library/USkin.aspx?msg=2814769)
* [msstyles Skins](http://www.skinbase.org/Application/msstyles/135)
