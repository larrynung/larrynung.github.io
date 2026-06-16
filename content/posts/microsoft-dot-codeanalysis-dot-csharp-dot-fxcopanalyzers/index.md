---
title: "Microsoft.CodeAnalysis.CSharp.FxCopAnalyzers"
date: "2014-11-03 23:17:00"
description: "Microsoft.CodeAnalysis.CSharp.FxCopAnalyzers 是一個 Diagnostic Analyzer 套件，是 FxCop 部分檢查規則的 Analyzer 實作。"
tags: [Roslyn,  Visual Studio]
---

Microsoft.CodeAnalysis.CSharp.FxCopAnalyzers 是一個 Diagnostic Analyzer 套件，是 FxCop 部分檢查規則的 Analyzer 實作。

![1.png](/images/posts/FxCopAnalyzers/1.png)

因為目前仍是 Preview 版本，所以這邊在使用時需先叫出 Package Manager Console，然後叫用命令安裝：

Install-Package Microsoft.CodeAnalysis.CSharp.FxCopAnalyzers -Pre

![2.png](/images/posts/FxCopAnalyzers/2.png)

安裝完後，我們可以看到方案總管的 Analyzers 節點下多了兩個 Analyzer。

![3.png](/images/posts/FxCopAnalyzers/3.png)

展開節點可以看到該 Analyzer 所 Support 的分析。

![4.png](/images/posts/FxCopAnalyzers/4.png)

回到程式編輯這邊，可以看到當我們程式撰寫不符合 Analyzer 的規定時，編譯器就會提出對應的警告，像這邊就告知我們要實作 IDisposible 介面，也提供了對應的修正。

![5.png](/images/posts/FxCopAnalyzers/5.png)