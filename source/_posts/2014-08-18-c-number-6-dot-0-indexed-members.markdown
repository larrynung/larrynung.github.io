---
layout: post
title: "C# 6.0 - Indexed Members"
date: 2014-08-18 23:43
comments: true
categories: [C#]
keywords: "C#, Indexed Members"
description: "C# 6.0 - Indexed Members"
---

Indexed Members 是預計要在 C# 6.0 釋出的新功能，目前已可在 Visual Studio 14 中透過設定將功能開啟進行體驗，只要在方案檔中加上：  

<!-- More -->

    <LangVersion>experimental</LangVersion>

或是透過 .Net Fiddle 也可以，Compiler 那邊選取 Roslyn 就可以了。  

<br/>

以往我們在存取 Dictionary Member 的時候程式撰寫起來會像這樣：  

<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/qbnRaw" frameborder="0"></iframe>  

<br/>

簡單來說就是直接透過索引子帶入 Key 的方式進行存取。  

<br/>

而在 C# 6.0 後， Indexed Members 提供開發人員另一種存取 Dictionary Member 方式。只要像 `$.Key` 這樣撰寫就可直接對 Dictionary Member 進行存取。  

<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/EUlTKH" frameborder="0"></iframe>  

<br/>

若有需要這邊也可以進一步結合 C# 6.0 的 Element Initializers 進行 Dictionary 的初始化。  

<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/YbqJ1t" frameborder="0"></iframe>  
