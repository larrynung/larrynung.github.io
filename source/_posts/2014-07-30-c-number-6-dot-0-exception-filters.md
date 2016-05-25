---
layout: post
title: "C# 6.0 - Exception filters"
date: 2014-07-30 22:43:00
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

Exception filters 能讓開發人員很容易的在攔截例外時順帶做些過濾的動作，藉此處理符合過濾條件的例外，且不對例外呼叫堆疊造成不良的影響。  

<br/>

以往我們必須要先將例外攔截，接著進行比對過濾，最後將符合的例外做對應的處理，不符合的例外繼續讓它向外擴出。但是這樣的作法會讓例外呼叫堆疊看不到實際發生的例外點，只看到重新擴出例外的點，造成除錯上的困難。  

{% img /images/posts/ExceptionFilters/1.png %}

<br/>

Exception filters 的出現能幫助開發人員解決這樣的問題。  

<br/>

它的語法很直覺，簡單來說就只是在 Try/Catch 的 Catch 後面加上 if 條件式進行過濾。

    try {...} catch(Exception e) if (...) {...}

<br/>

程式寫起來會像下面這樣：

<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/bS323c" frameborder="0"></iframe>  

<br/>

反組譯看一下，可以看到 Exception filters 這邊會被編譯成 filter 區塊的部份，從 IL 這邊就直接支援。  

{% img /images/posts/ExceptionFilters/2.png %}

<br/>


這樣的寫法不僅直覺，且不會對例外呼叫堆疊造成不良的影響。

{% img /images/posts/ExceptionFilters/3.png %}

<br/>


最後這邊做個新舊方法的測試比較：

<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/9sBem3" frameborder="0"></iframe>  

<br/>

可以看到效能的部份其實是差不多的，新語法感覺是沒有任何的效能優化。
