---
title: Visual Studio 2017 - Find all references
date: 2017-02-19 23:18:31
tags: [Visual Studio, Visual Studio 2017]
---

Visual Studio 2017 針對 Find all references 視窗做了些強化，在要查詢 Reference 的地方按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中點選 `Find All References` 選單選項，將 Find all references 視窗開啟。  

<!-- More -->

{% asset_img 1.png %}

<br/>


開啟後會看到該視窗跟 Visual Studio 2017 以前有些許不同，上方工具列有些差異，結果也改以群組的方式呈現。  

{% asset_img 2.png %}

<br/>


上方工具列有下拉式選單可供我們選擇是找尋整個方案、開啟的文件、當前專案、當前文件。  

{% asset_img 3.png %}

<br/>


也提供向前巡覽 reference (也可用熱鍵 Shift + F8 觸發)。  

{% asset_img 4.png %}

<br/>


向後巡覽 reference (也可用熱鍵 F8 觸發)。  

{% asset_img 5.png %}

<br/>


也有下拉選單可以改變群組的方式，像是預設的 `Project then Definition` 群組，會先以專案再以程式碼的定義去群組：    

{% asset_img 6.png %}

<br/>


`Definition Only` 會以程式碼的定義去群組：  

{% asset_img 7.png %}

<br/>


`Definition then Project` 會先以程式碼定義再以專案去群組：  

{% asset_img 8.png %}

<br/>


`Definition then Path` 會先以程式碼定義再以專案路徑去群組：  

{% asset_img 9.png %}

<br/>


`Definition, Project then Path` 會先以程式碼定義再以專案最後以專案路徑去群組：  

{% asset_img 10.png %}

<br/>


不同的群組方式適用於不同的使用情境，可視需求調整使用。  

<br/>


若有需要進一步篩選，可利用上方的搜尋框。  

{% asset_img 11.png %}

<br/>


若要保留搜尋結果供後續使用，可按下 `Keep Result` 按鈕。  

{% asset_img 12.png %}

<br/>


這樣再次搜尋 Reference 時就不會重用本來的視窗。  

{% asset_img 13.png %}

<br/>


而會使用新的視窗。  

{% asset_img 14.png %}

<br/>
