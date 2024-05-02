---
title: "Visual Studio 2017 - Live unit testing"
date: "2017-03-01 23:05:15"
tags: [Visual Studio, Visual Studio 2017]
---


要啟動 Visual Studio 2017 Live Unit Testing 功能，可點選 [Test | Live Unit Testing | Start] 主選單選項。  

<!-- More -->

![1.png](1.png)

<br/>


啟動後單元測試會持續在背景運行。  

![2.png](2.png)

<br/>


可在開發程式時即時看到測試的狀況與覆蓋情形。  

![3.png](3.png)

<br/>


需注意的是這功能需要 MSTest V2 才能啟用，舊測試專案需要移除 `Microsoft.VisualStudio.QualityTools.UnitTestFramework` 的參考。  

![4.png](4.png)

<br/>


加入 MSTest.TestFramework 套件。  

![5.png](5.png)

<br/>


加入 TestAdapter 套件。  

![6.png](6.png)

<br/>


最後調整命名空間即可。  

![7.png](7.png)

<br/>
