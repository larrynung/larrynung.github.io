---
layout: post
title: "Code Cracker"
date: 2015-02-10 08:37:00
comments: true
tags: [Roslyn, Visual Studio]
keywords: "Roslyn, CodeCracker"
description: "CodeCracker"
---

Code Cracker 是 Roslyn analyzer 的 Library，有點類似 FxCop 的 Rule，依不同的範疇實做了很多相關的檢查，可以看到有 Design、Globalization、Maintainability、Naming、Performance、Portabili、Security ...等。雖然還未完全實作完畢，但目前已經相當多的檢查 Rule 了。    

<!-- More -->

{% img /images/posts/CodeCracker/1.png %}

<br/>


安裝上一樣是提供 VSIX 或是 NuGet Package 兩種，若是要套到所有專案，可直接透過 Extension and Updates 安裝。  

{% img /images/posts/CodeCracker/2.png %}

<br/>


若是只要套用到單一專案，可直接透過 NuGet 安裝。不論是要用 NuGet 的 GUI 介面。    

{% img /images/posts/CodeCracker/3.png %}

<br/>


或是直接透過 NuGet 命令都可以。  

    Install-Package CodeCracker.CSharp -IncludePrerelease

    Install-Package CodeCracker.VisualBasic -IncludePrerelease


用 NuGet 安裝的話，Analyzer 會出現在方案總管的 References\Analyzers 節點下。  

{% img /images/posts/CodeCracker/4.png %}

<br/>


展開 Analyzer 節點可進一步看到支援的 Rule。  

{% img /images/posts/CodeCracker/5.png %}

<br/>


在編輯視窗做個簡單的測試，像是放個空的解構子，或是方法的參數宣告了但不使用，沒意外的話應該要會被 Code Cracker 的 Analyzer 偵測出來。  

{% img /images/posts/CodeCracker/6.png %}

<br/>


Link
-----
* [Welcome to Code Cracker!](http://code-cracker.github.io/)
* [code-cracker/code-cracker · GitHub](https://github.com/code-cracker/code-cracker)
