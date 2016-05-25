---
layout: post
title: "PostSharp - Adding Detailed Tracing to a Code Base"
date: 2015-02-02 00:01:00
comments: true
categories: [PostSharp]
keywords: "PostSharp, Tracing"
description: "PostSharp - Adding Detailed Tracing to a Code Base"
---

要使用 PostSharp 為程式加入些簡易的 Log 資訊，在安裝完 PostSharp 擴充套件後，我們可以在類別上直接按下右鍵，在彈出的滑鼠右鍵快顯選單中，選取 `Add logging...` 選單選項。

<!--More -->

{% img /images/posts/PostSharpDetailedTraching/1.png %}

<br/>


接著 PostSharp 擴充套件會帶出精靈視窗，這邊要我們選取 Log 的 Profile，這邊選取 Default Profile 後按下 Next 按鈕即可。  

{% img /images/posts/PostSharpDetailedTraching/2.png %}

<br/>


再來是要決定 Log 機制背後要用哪種服務，有 Trace、Console、Log4Net、NLog、Enterprise Library，一樣選取完後按下 Next 按鈕繼續。  

{% img /images/posts/PostSharpDetailedTraching/3.png %}

<br/>


Summary 頁面這邊只是告訴我們繼續下去會做什麼事，不外乎就是加入套件引用、加上 Attribute、 設定 Config，一樣按下 Next 繼續。  

{% img /images/posts/PostSharpDetailedTraching/4.png %}

<br/>


如 Summary 頁面所提，要處理的東西有點多，進度要稍微跑一下。  

{% img /images/posts/PostSharpDetailedTraching/5.png %}

<br/>


跑完後按下 Finish 按鈕結束精靈頁面。  

<br/>


可以看到專案已套上對應的修改，已引用該引用的套件、產生副檔名為 psproj 的設定檔、Attribute 也正確的加上。  

{% img /images/posts/PostSharpDetailedTraching/6.png %}

<br/>


滑鼠移上去再次確認，沒意外的話就會看到確實已經套用完成(若沒有這畫面可能是因為資料還未更新完成，可嘗試重建專案看看)。

{% img /images/posts/PostSharpDetailedTraching/7.png %}

<br/>


運行後 Log 會送入對應的服務，像這邊筆者用的是 Console 服務，所以會直接印在 Console 視窗內，而使用的設定是 Default，所以可以看到訊息是進出 Method 都會寫，且印出的資訊會含方法的名稱、參數...等等。  

{% img /images/posts/PostSharpDetailedTraching/8.png %}

<br/>


Link
----
* [Walkthrough: Adding Detailed Tracing to a Code Base](http://doc.postsharp.net/logging)
