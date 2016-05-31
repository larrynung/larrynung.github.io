---
layout: post
title: "Remove #region block with Regex"
date: 2015-10-21 23:22:00
comments: true
tags: 
keywords: 
description: "Remove #region block with Regex"
---

最近又回頭維護前人的程式，還是很多地方都看不習慣。像是 Region 的濫用讓程式維護起來就很痛苦，程式中很多方法內都存在許多的 Region 區塊，這些區塊都依個人主觀的功能下去劃分，問題發生時不是劃分的人其實很難精準的找到程式在哪個 Region 區塊。且如果方法中的功能真的可以內聚到 Region 區塊之中，那為何不拆解成方法或是負責對應職責的類別呢？  

<!-- More -->

<br/>


為了解決這個問題，我們可以用 Visual Studio 內建的取代功能，帶入正規表示式快速的將 Region 取代掉。  

    ^[ \t]*\#(region|endregion).*\n

<br/>


{% img /images/posts/RemovingRegionBlock/1.png %}

<br/>

Link
----
* [c# - removing #region - Stack Overflow](http://stackoverflow.com/questions/5083430/removing-region)
