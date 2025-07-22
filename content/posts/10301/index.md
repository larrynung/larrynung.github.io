---
title: "[Library][C#]USkin 視窗換膚函式庫"
date: "2009-08-28 10:19:24"
description: "[Library][C#]USkin 視窗換膚函式庫"
tags: [Library, CSharp]
---

## Introduction

USkin是一個可以讓應用程式換膚用的函式庫。可讓應用程式套用不同的主題，讓介面有別於其它視窗。

## Feature
支援 Microsoft Window's Theme 檔支援通用控制項支援新控制項 (像是 ToolStrip/MenuStrip)支援 VC/C#/VB.NET支援系統標準表單，像是檔案對話框、顏色對話框、列印對話框支援客制控制項支援 MDI/SDI/Dialog 類型的應用程式只需增加兩行程式即可支援Skin fileSkin file僅僅約30Kb的大小

## 使用方法

在使用USkin時我們必需要使用到USkin.dll，並利用PInvoke去叫用USkin.dll內部的函式。因此我們可以把USkin.dll加入專案，並設定屬性讓它在編譯時自動複製到輸出目錄。接著我們可以用DllImport來呼叫使用USkin.dll內的函式。為了方便起見，我們可以直接把官網範例的USkinSDK.cs直接加入來用。

程式範例如下:

執行結果   

經過Init設定過Skin後，若想要動態載入變換Skin，則我們可以叫用USkinLoadSkin。

USkin.USkinSDK.USkinLoadSkin(@"Vista.msstyles");

若有自行編輯介面的需求，可以使用SkinStudio等編輯工具。若想要抓現成的介面樣版可到msstyles Skins下載。

## Link
USkin V3.0 version publishedSkinStudio Free 4.6USkin V3.0 - 免費漂亮界面製作(1)USkin V3.0 - 免費漂亮界面製作(2)USkin V3.0 - 免費漂亮界面製作(3) The Code Project-Use the Free USkin Toolkit to Skin your Applicationmsstyles Skins