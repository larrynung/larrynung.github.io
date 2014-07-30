---
layout: post
title: "C# 6.0 - Exception filters"
date: 2014-07-30 22:43
comments: true
categories: [C#]
keywords: "C#, Exception Filters"
description: "C# 6.0 - Exception filters"
---

Exception filters 是預計要在 C# 6.0 釋出的新功能，目前已可在 Visual Studio 14 中透過設定將功能開啟進行體驗，只要在方案檔中加上：

<!-- More -->

    <LangVersion>experimental</LangVersion>

或是透過 .Net Fiddle 也可以，Compiler 那邊選取 Roslyn 就可以了。

<br/>

Exception filters 能讓開發人員很容易的在攔截例外時順帶做些過濾的動作。不用再像以前一樣要先將例外攔截，攔截後比對過濾，然後再對符合的例外做對應的處理，不符合的例外則向外擴。

<br/>

它的語法很直覺，簡單來說就只是在 Try/Catch 的 Catch 後面加上 if 條件式進行過濾。

<br/>

程式寫起來會像下面這樣：

<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/bS323c" frameborder="0"></iframe>  

<br/>

反組譯看一下，可以看到 Exception filters 這邊會被編譯成 filter 區塊的部份，跟用舊方法處理比起來是不同的編譯碼。  

{% img /images/posts/ExceptionFilters/1.png %}

<br/>

最後這邊做個新舊方法的測試比較：

<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/9sBem3" frameborder="0"></iframe>  

<br/>

可以看到效能的部份其實是差不多的，新語法感覺是沒有任何的效能優化。
