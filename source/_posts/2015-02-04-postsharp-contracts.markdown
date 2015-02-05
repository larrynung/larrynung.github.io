---
layout: post
title: "PostSharp - Contracts"
date: 2015-02-04 23:56
comments: true
categories: [PostSharp]
keywords: "PostSharp, Contract"
description: "PostSharp - Contracts"
---

以往我們在寫函式的時候，若要作參數的檢查，我們可能會自行去檢查參數是否 Null 或是 Empty，若是 Null 或 Empty 則丟出 ArgumentNullException。這樣的參數動作會混在程式邏輯的前面，PostSharp 的 Contract 功能就有點像是 Code Contract 一樣，能讓我們做前置條件的檢查，並將檢查抽離程式核心。   

<!-- More -->

<br/>


使用上只要在要加入檢查的參數上面按下滑鼠右鍵，然後在彈出的滑鼠右鍵快顯選單中，選取 `Require a non-null and non whitespace value` 這個選單選項。

{% img /images/posts/PostSharpContracts/1.png %}

<br/>


接著 PostSharp 擴充套件會帶出精靈視窗，第一頁是 Summary 頁面，這邊只是告訴我們繼續下去會做什麼事，不外乎就是加入套件引用與加上對應的 RequiredAttribute，這邊直接 Next。

{% img /images/posts/PostSharpContracts/2.png %}

<br/>


如 Summary 頁面所提，要處理的東西有點多，進度要稍微跑一下。  

{% img /images/posts/PostSharpContracts/3.png %}

<br/>


進度跑完後按下 Finish 按鈕結束精靈視窗即可。  

<br/>


可以看到專案已套上對應的修改，已將該引用的套件引用、RequiredAttribute 也已正確的加上。

{% img /images/posts/PostSharpContracts/4.png %}

<br/>


滑鼠移上去再次確認，沒意外的話就會看到確實已經套用完成(若沒有這畫面可能是因為資料還未更新完成，可嘗試重建專案看看)。  

{% img /images/posts/PostSharpContracts/5.png %}

<br/>

{% img /images/posts/PostSharpContracts/6.png %}

<br/>


運行後可看到帶入空值時確實會做參數的檢查，得到了預期的 ArgunemtNullException。  

{% img /images/posts/PostSharpContracts/7.png %}

<br/>


除了 RequiredAttribute 外，PostSharp 也內建了許多其它常用的 Contract。若要套用可在要加入的參數上按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中，選取 `Add another aspect...` 選單選項。  

{% img /images/posts/PostSharpContracts/8.png %}

<br/>


從這邊的精靈介面我們可以看到許多內建的 Contract 可供選取，像是檢查 URL、檢查 Email Address、檢查 Phone Number ...等。這邊筆者要檢查的是 Email Address，所以選取 `Require a valid email address`，按下 Next 按鈕繼續。    

{% img /images/posts/PostSharpContracts/9.png %}

<br/>

一樣將精靈跑完運行即可。  

<br/>


Link
----
* [Contracts](http://doc.postsharp.net/contracts)
