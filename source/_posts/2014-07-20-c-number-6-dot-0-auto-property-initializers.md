---
layout: post
title: "C# 6.0 - Auto-property initializers"
date: 2014-07-20 23:11:00
comments: true
categories: [C#]
keywords: "C#, Auto-Property"
description: "C# 6.0 - Auto-property initializers"
---

Auto-property initializers 是預計要在 C# 6.0 釋出的新功能，目前已可在 Visual Studio 14 中透過設定將功能開啟進行體驗，只要在方案檔中加上： 

<!-- More -->

    <LangVersion>experimental</LangVersion> 


或是透過 .Net Fiddle 也可以，Compiler 那邊選取 Roslyn 就可以了。  

<br/>

Auto-property initializers 能讓開發人員在宣告 Auto-property 的同時就順道做初始的動作。不用另行在建構子中設定。也不再寫用回一般的 Property 寫法，然後在 Field 宣告時設定。 

<br/>

它的語法很直覺，簡單來說就是本來的 Auto-property 後面直接接上賦值的語法。像是: 

    public string Property { get; set; } = "Value";


除了一般可讀可寫的 Property 外，唯讀的甚至是靜態的 Property 該語法也都支援。 

<br/>

以一個較完整的例子來看，程式寫起來會像下面這樣：

<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/jg1JXQ" frameborder="0"></iframe>  

<br/>

程式寫起來可以看到比以往精簡許多，運行後屬性也都有正確的賦值。  

<br/>

反組譯看一下，可以看到比較接近透過變數初始器去做賦值的動作，會在基底類別初始前宣告，也會標注 beforefieldinit。

{% img /images/posts/AutoPropertyInitializers/1.png %}

{% img /images/posts/AutoPropertyInitializers/2.png %}
