---
layout: post
title: "Microsoft.CodeAnalysis.CSharp.FxCopAnalyzers"
date: 2014-11-03 23:17:00
comments: true
categories: [Roslyn,  Visual Studio]
keywords: "Roslyn, Visual Studio, FxCop, Analyzer"
description: "Microsoft.CodeAnalysis.CSharp.FxCopAnalyzers"
---

Microsoft.CodeAnalysis.CSharp.FxCopAnalyzers 是一個 Diagnostic Analyzer 套件，是 FxCop 部分檢查規則的 Analyzer 實作。  

<!-- More -->

{% img /images/posts/FxCopAnalyzers/1.png %}

<br/>


因為目前仍是 Preview 版本，所以這邊在使用時需先叫出 Package Manager Console，然後叫用命令安裝：

    Install-Package Microsoft.CodeAnalysis.CSharp.FxCopAnalyzers -Pre

{% img /images/posts/FxCopAnalyzers/2.png %}

<br/>


安裝完後，我們可以看到方案總管的 Analyzers 節點下多了兩個 Analyzer。  

{% img /images/posts/FxCopAnalyzers/3.png %}

<br/>


展開節點可以看到該 Analyzer 所 Support 的分析。  

{% img /images/posts/FxCopAnalyzers/4.png %}

<br/>


回到程式編輯這邊，可以看到當我們程式撰寫不符合 Analyzer 的規定時，編譯器就會提出對應的警告，像這邊就告知我們要實作 IDisposible 介面，也提供了對應的修正。  

{% img /images/posts/FxCopAnalyzers/5.png %}

<br/>
