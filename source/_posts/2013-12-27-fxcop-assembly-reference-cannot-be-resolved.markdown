---
layout: post
title: "FxCop - assembly reference cannot be resolved"
date: 2013-12-27 23:31
comments: true
categories: FxCop
keywords: FxCop, Unresolved, GAC
description: "FxCop - assembly reference cannot be resolved"
---

在使用 FxCop 分析組件時，某些組件在用命令列載入時會跳出 `cannot be resolve`  這樣的錯誤訊息。  

<!--More-->

{% img /images/posts/FxCopUnresolvedAssembly/1.png %}


改用 FxCop 嘗試載入的話，也會找不到相依的組件而彈出詢問對話框。  

{% img /images/posts/FxCopUnresolvedAssembly/2.png %}


這樣的問題是由於某些相依的組件找不到所導致，而這些組件有時候只是在 GAC 內。所以要解決這樣的問題，可以在 FxCop 點選 `Project/Options...` 主選單選項，將開出的 Options 對話視窗切換至 `Spelling & Analysis` 頁籤，勾選 `Search Global Assembly Cache for missing references` 勾選框。  

{% img /images/posts/FxCopUnresolvedAssembly/3.png %}

{% img /images/posts/FxCopUnresolvedAssembly/4.png %}


若是使用命令列驅動 FxCop 分析，可帶入命令列參數 `/gac`。

    FxCopCmd /file:[Assembly] /gac


這樣 FxCop 就會嘗試由 GAC 中找尋遺失的組件參考。
