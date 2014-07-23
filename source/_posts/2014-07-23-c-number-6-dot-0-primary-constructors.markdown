---
layout: post
title: "C# 6.0 - Primary Constructors"
date: 2014-07-23 14:27
comments: true
categories: [C#]
keywords: "C#"
description: "C# 6.0 - Primary Constructors"
---

Primary Constructors 是預計要在 C# 6.0 釋出的新功能，目前已可在 Visual Studio 14 中透過設定將功能開啟進行體驗，只要在方案檔中加上：

<!-- More -->

    <LangVersion>experimental</LangVersion>

或是透過 .Net Fiddle 也可以，Compiler 那邊選取 Roslyn 就可以了。  

<br/>

以往在撰寫建構子多載時，通常我們會有一個首要建構子負責做初始的功能，其它建構子透過建構子鏈去叫用首要建構子。像是下面這樣：  

<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/NAPlOB" frameborder="0"></iframe>  

<br/>

但這樣的處理方式，使用建構子鏈叫用首要建構子的動作並未強制，難免有時候會有所遺漏，或是不小心又另闢一條路去作初始動作。而且首要建構子通常也只是做很簡易的賦值動作，為此明確宣告一個建構子在語法上看起來是有些冗餘。  

<br/>

C# 6.0 的 Primary Constructors 語法能讓開發人員在宣告 Class 的同時就連帶設定首要的建構子。只要在 Class 宣告後接著宣告首要建構子欲接受的參數即可（可以想成 Class 與建構子的合併宣告）。像是下面這樣：  

<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/RcNVVW" frameborder="0"></iframe>  

<br/>

從這段程式中我們可以看到 Primary Constructors 可以結合 [Auto-property initializers](http://larrynung.github.io/2014/07/20/c-number-6-dot-0-auto-property-initializers/) 語法去做賦值的動作，冗餘的建構子宣告不再需要了，程式因此變得更加的精簡。而且透過 Primary Constructors 語法設定首要建構子，所有非首要的建構子被強制要叫用首要建構子。

<br/>

反組譯看一下，其實也只是編譯器編譯時幫我們做了對應的宣告：  

{% img /images/posts/PrimaryConstructors/1.png %}

<br/>

另外可以注意到這邊，在這範例中筆者特地宣告了一個 name 區域變數，程式仍舊可以正常運行，不會跟首要建構子的參數衝突。表示首要建構子那邊的參數範圍只會影響到 Field 與 Property，對於方法的參數甚至是方法內的區域變數並不造成影響。  

<br/>

除了透過[Auto-property initializers](http://larrynung.github.io/2014/07/20/c-number-6-dot-0-auto-property-initializers/) 語法去做賦值外，Primary Constructors 也可以讓我們直接宣告 Field，只要在宣告首要建構子的參數時順帶指定 Modifier 就可以了。像是下面這樣：


<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/pgvNvg" frameborder="0"></iframe>  

<br/>

最後一提，如果類別要繼承，首要建構子又要呼叫基底建構子的話，Primary Constructors 也可以支援，像下面這樣處理即可：

<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/c8NkSv" frameborder="0"></iframe>
