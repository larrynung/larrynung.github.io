---
title: "[Visual Studio]Visual Studio 2010 New Feature ndash; Add Reference Dialog Improvements"
date: "2010-03-16 09:42:05"
description: "[Visual Studio]Visual Studio 2010 New Feature &ndash; Add Reference Dialog Improvements"
tags: [Visual Studio]
---

VS2010在加入參考對話框上也做了兩項加強。在以往的版本，當我們要加入參考時，總是會需要等很久，加入參考對話框才會出現。這是因為以往的版本，在加入參考對話框開啟時，預設開啟的頁面會是.NET頁面。而在.NET與COM兩個頁面通常會有很多資料需要載入，像是GAC的組件等等，載入的動作也不是非同步處理的，所以開啟十分的緩慢。

VS2010解決了這樣的問題，預設開啟的頁面被改為Projects頁面，而Projects頁面多半要顯示的資料是最少的，因此開啟時不需要花費太多時間在做載入的動作，能夠快速的進入加入參考對話框。

![](/images/posts/14065/)

另外加入參考對話框內資料載入的動作，在VS2010中改為用非同步的方式來處理，操作上更為快速順暢，也能在載入的同時做頁面的切換，或是關閉加入參考對話框。