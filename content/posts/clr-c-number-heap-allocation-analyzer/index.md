---
title: "Clr C# Heap Allocation Analyzer"
date: "2014-11-05 00:00:00"
description: "Clr C# Heap Allocation Analyzer"
tags: [Roslyn, CSharp, Visual Studio]
---


Clr C# Heap Allocation Analyzer 是 Diagnostic Analyzers 的套件，功能上有點類似 [ReSharper - Heap Allocation Viewer Extension](http://larrynung.github.io/2014/08/12/resharper-heap-allocation-viewer-extension/)，能對 Heap 的操作部分做些 Highlight。  

<!-- More -->

<br/>


這邊可先參閱一下影片的介紹：  

<iframe width="560" height="315" src="//www.youtube.com/embed/Tw-wgT-cXYU" frameborder="0" allowfullscreen></iframe>

<br/>


該套件提供兩種安裝方式，一種是選擇安裝 VSIX，用 Extension Manager 搜尋安裝或是自 [NuGet Gallery | Clr C# Heap Allocation Analyzer 1.0.0.5](https://www.nuget.org/packages/ClrHeapAllocationAnalyzer/) 下載安裝，好處是可以將效果套用至所有專案。  
{% img /images/posts/HeapAllocationAnalyzer/1.png %}

<br/>


一種則是用 NuGet By 專案安裝，好處是可以只套用至特定的專案。  

{% img /images/posts/HeapAllocationAnalyzer/2.png %}

<br/>


安裝完後，在程式編輯時即會呈現進行對應的分析，像是筆者這邊的程式即被偵測出有 Boxing 的動作。  

{% img /images/posts/HeapAllocationAnalyzer/3.png %}

<br/>


Link
----
* [NuGet Gallery | Clr C# Heap Allocation Analyzer 1.0.0.5](https://www.nuget.org/packages/ClrHeapAllocationAnalyzer/)
* [Clr Heap Allocation Analyzer extension](https://visualstudiogallery.msdn.microsoft.com/f9b47b93-8675-4ae0-9c52-5da8027c4bb8)
