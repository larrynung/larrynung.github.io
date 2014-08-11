---
layout: post
title: "ReSharper - Heap Allocation Viewer Extension"
date: 2014-08-12 00:10
comments: true
categories: [Visual Studio]
keywords: "Visual Studio, ReSharper, Heap, Boxing"
description: "ReSharper - Heap Allocation Viewer Extension"
---

Heap Allocation Viewer 是 Reshaper 的擴充套件，能將 Heap 相關的操作 (像是 Local object allocation、Boxing、Delegate creation、Closure creation ) 進行 Highlight。  

<!-- More -->

<br/>

使用前需先開啟 ReSharper 的 Extension Manager。  

{% img /images/posts/HeapAllocationViewer/1.png %}

<br/>


搜尋框輸入 heapview 關鍵字，下載並安裝 Heap Allocation Viewer 套件 (若搜尋不到，可能是因為 ReSharper 太舊，需更新為 8.1 以後的版本)。  

{% img /images/posts/HeapAllocationViewer/2.png %}

<br/>

{% img /images/posts/HeapAllocationViewer/3.png %}

<br/>

{% img /images/posts/HeapAllocationViewer/4.png %}

<br/>


安裝好後，Visual Studio 即會將 Heap 相關的操作 Highlight。  

{% img /images/posts/HeapAllocationViewer/5.png %}

<br/>

{% img /images/posts/HeapAllocationViewer/6.png %}

<br/>

以筆者來說，加裝該套件的主要原因是它可以幫我們 Highlight 程式中 Boxing 問題，而且在開發時當 Boxing 問題發生可以很容易的意識到。  

<br/>

該套件也支援掃整個專案或是方案，用 Reshaper 的 Find Code Issues 功能就能找出所有 Boxing 問題的發生點。 

{% img /images/posts/HeapAllocationViewer/7.png %}
