---
title: SonarQube - Quality Profiles
date: 2017-03-22 13:13:45
tags: SonarQube
---

SonarQube 的 Quality Profiles 頁面提供我們查詢可供分析的 Profile。  

<!--More -->

<br/>


Profile 為分析 Rule 的集合，多半會造著語言或是套件下去區分。透過 Quality Profiles 頁面我們可以新增 Profile、查看 Profile 的 Rule 數、查看上次使用的時間...等。  

{% asset_img 1.png %}

<br/>


點選 Profile 的名稱可進一步進入 Profile 管理頁面。在這頁面我們可以看到 Profile 所使用的 Rule、與設定 Profile 的繼承關係。  

{% asset_img 2.png %}

<br/>


在進行程式碼分析之前可先透過該頁面確認 Rule 的啟用狀態，因為有時套件安裝的 Profile 其 Rule 預設是未啟用的狀態，或是某些想要分析的 Rule 並未被啟用，這時可以按下 `Active More` 按鈕切到 Rules 頁面，透過 Rules 頁面將之啟用。  