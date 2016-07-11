---
title: Visual Studio - Move obj folder
date: 2016-07-12 00:06:15
tags: [Visual Studio]
---

Visual Studio 的專案在建置 .NET 專案時會自動建立 Obj 目錄放置中繼檔案，該目錄位置並無直接的設定方式。  


<!-- More -->

<br/>

如果想要調整該目錄位置，可設定 Project 檔案，在第一個 PropertyGroup 中加入 BaseIntermediateOutputPath 元素去指定位置。  

{% asset_img 1.png %}

<br/>


Link
---
* [c# - Move obj folder in Visual Studio 2012 - Stack Overflow](http://stackoverflow.com/questions/15620224/move-obj-folder-in-visual-studio-2012)
