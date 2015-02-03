---
layout: post
title: "PostSharp - Tracing Parameter Values Upon Exception"
date: 2015-02-04 00:06
comments: true
categories: [PostSharp]
keywords: "PostSharp"
description: "PostSharp - Tracing Parameter Values Upon Exception"
---

要使用 PostSharp 為程式加入 Exception 的 Log 處理，在安裝完 PostSharp 擴充套件後，我們可以在類別上直接按下右鍵，在彈出的滑鼠右鍵快顯選單中，選取 `Add logging...` 選單選項。  

<!-- More -->

{% img /images/posts/PostSharpTracingUponException/1.png %}

<br/>


接著 PostSharp 擴充套件會帶出精靈視窗，這邊要我們選取 Log 的 Profile，因為要這篇要示範 Exception 的處理，所以遠取 Exceptions 的 Profile 後按下 Next 按鈕即可。  

{% img /images/posts/PostSharpTracingUponException/2.png %}

<br/>


再來是要決定 Log 機制背後要用哪種服務，有 Trace、Console、Log4Net、NLog、Enterprise Library，一樣選取完後按下 Next 按鈕繼續。  

{% img /images/posts/PostSharpTracingUponException/3.png %}

<br/>


Summary 頁面這邊只是告訴我們繼續下去會做什麼事，不外乎就是加入套件引用、加上 LogException Attribute、 設定 Config，一樣按下 Next 繼續。  

{% img /images/posts/PostSharpTracingUponException/4.png %}

<br/>


如 Summary 頁面所提，要處理的東西有點多，進度要稍微跑一下。  

{% img /images/posts/PostSharpTracingUponException/5.png %}

<br/>


跑完後按下 Finish 按鈕結束精靈頁面。

{% img /images/posts/PostSharpTracingUponException/6.png %}

<br/>


可以看到專案已套上對應的修改，已引用該引用的套件、產生副檔名為 psproj 的設定檔、Attribute 也正確的加上。  

{% img /images/posts/PostSharpTracingUponException/7.png %}

<br/>


滑鼠移上去再次確認，沒意外的話就會看到確實已經套用完成(若沒有這畫面可能是因為資料還未更新完成，可嘗試重建專案看看)。  

{% img /images/posts/PostSharpTracingUponException/8.png %}

<br/>


運行後 Log 會送入對應的服務。  

{% img /images/posts/PostSharpTracingUponException/9.png %}

<br/>


Link
----
* [Walkthrough: Tracing Parameter Values Upon Exception](http://doc.postsharp.net/exception-tracing)
