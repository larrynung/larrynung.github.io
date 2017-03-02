---
title: Visual Studio 2017 - Lightweight solution load
date: 2017-02-10 00:28:45
tags: [Visual Studio, Visual Studio 2017]
---

Visual Studio 2017 新增 Lightweight Solution load 功能，能 OnDemand 進行專案的載入，特別適用於大型專案的開發。

<!-- More -->

<br/>


該功能預設是關閉的，要啟用可開啟選項對話框，切到 [Projects and Solutions | General] 頁籤，勾選 `Lightweight Solution load` 選項。  

{% asset_img 1.png %}

<br/>


將專案載入，乍看起來好像沒什麼太大的變化。  

{% asset_img 2.png %}

<br/>


但仔細看方案總管這邊，會發現方案名稱後面多了個 `lightweight` 字樣。  

{% asset_img 3.png %}

<br/>


將方案總管的專案展開，會看到其實專案還沒被載入，展開的同時才開始進行載入。  

{% asset_img 4.png %}

<br/>


稍待一下即可載入完成。  

{% asset_img 5.png %}

<br/>
