---
title: Visual Studio 2017 - Live unit testing
date: 2017-03-01 23:05:15
tags: [Visual Studio]
---

要啟動 Visual Studio 2017 Live Unit Testing 功能，可點選 [Test | Live Unit Testing | Start] 主選單選項。  

<!-- More -->

{% asset_img 1.png %}

<br/>


啟動後單元測試會持續在背景運行。  

{% asset_img 2.png %}

<br/>


可在開發程式時即時看到測試的狀況與覆蓋情形。  

{% asset_img 3.png %}

<br/>


需注意的是這功能需要 MSTest V2 才能啟用，舊測試專案需要移除 `Microsoft.VisualStudio.QualityTools.UnitTestFramework` 的參考。  

{% asset_img 4.png %}

<br/>


加入 MSTest.TestFramework 套件。  

{% asset_img 5.png %}

<br/>


加入 TestAdapter 套件。  

{% asset_img 6.png %}

<br/>


最後調整命名空間即可。  

{% asset_img 7.png %}

<br/>

