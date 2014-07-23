---
layout: post
title: "C# 6.0 - Using static members"
date: 2014-07-21 23:05
comments: true
categories: [C#]
keywords: "C#, Static, Using"
description: "C# 6.0 - Using static members"
---

Using static members 是預計要在 C# 6.0 釋出的新功能，目前已可在 Visual Studio 14 中透過設定將功能開啟進行體驗，只要在方案檔中加上： 

<!-- More -->

    <LangVersion>experimental</LangVersion>
 

或是透過 .Net Fiddle 也可以，Compiler 那邊選取 Roslyn 就可以了。  

<br/>

Using static members 能讓開發人員更方便的對指定類別的靜態成員做存取。對於程式中有大量的靜態成員存取操作時特別好用。    

<br/>

使用上與 Namespace 的 Using 類似，只是後面帶的不是到 Namespace 而已，而是進一步再向下帶到 Class。用 Using 指定要存取的類別後，在程式中就可以直接存取該類別的靜態成員，就如同自身的成員一般。  

<br/>

以一個較完整的例子來看，程式寫起來會像下面這樣：  

<iframe width="100%" height="475" src="https://dotnetfiddle.net/Widget/5BMb2R" frameborder="0"></iframe>  

<br/>

可以看到這邊程式的一開始就先使用 Using 引用 Console 類別，後續我們就可以在程式中直接存取 Console 類別的靜態成員，像是取用 Title 、或是呼叫 WriteLine 方法。  

<br/>

反組譯看一下，可以發現其實該語法也只是編譯器幫我們在編譯時做了些處理。  

{% img /images/posts/UsingStaticMembers/1.png %}
