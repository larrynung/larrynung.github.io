---
title: "[.NET Concept].NET 4.0 DLR (Dynamic Language Runtime) 概述"
date: "2009-08-15 01:26:47"
description: "為了讓.NET語言支援更為動態的語法，在.NET 4.0的架構中特別導入了DLR (Dynamic Language Runtime)。 之所以會導入DLR到.NET Framework中，"
tags: [.NET Concept]
---

為了讓.NET語言支援更為動態的語法，在.NET 4.0的架構中特別導入了DLR (Dynamic Language Runtime)。

![image_thumb_1.png](/images/posts/10058/image_thumb_1.png)

之所以會導入DLR到.NET Framework中，一方面是為了提供動態類型語言(Ruby、Python)所必需要有的功能、一方面則是為了讓靜態類型語言(VB、C#)能藉此從中獲取動態類型語言所具備的優勢，像是Expression Trees、Dynamic Dispatch、與Call Site Caching。

![image_thumb_2.png](/images/posts/10058/image_thumb_2.png)

DLR主要是由Expression Trees、Dynamic Dispatch、與Call Site Caching所組成。其功能分別為

Expression Trees: 讓程式得以在執行階段運行，且易於了解，並可以在執行階段把程式作最佳化。

Dynamic Dispatch: 允許不同的語言互相溝通。

Call Site Caching: 提供較佳的效能

DLR強大的地方在於具有許多Binder，透過這些Binder我們能很輕鬆的與Python、Ruby等動態類型語言或是其它平台互通。

![image_thumb_3.png](/images/posts/10058/image_thumb_3.png)

![image_thumb.png](/images/posts/10058/image_thumb.png)

## Link

* [WIKI - Dynamic Language Runtime (簡體)](http://zh.wikipedia.org/wiki/Dynamic_Language_Runtime)
* [WIKI - Dynamic Language Runtime (EN)](http://en.wikipedia.org/wiki/Dynamic_Language_Runtime)
* [Jim Hugunin's Thinking Dynamic - A Dynamic Language Runtime (DLR)](http://blogs.msdn.com/hugunin/archive/2007/04/30/a-dynamic-language-runtime-dlr.aspx)
* [Bruno Terkaly - Microsoft Developer Evangelist - C# 4.0 – Dynamic Language Runtime](http://blogs.msdn.com/brunoterkaly/archive/2009/07/23/c-4-0-dynamic-language-runtime.aspx)
* [MSDN - Dynamic Language Runtime Overview](http://msdn.microsoft.com/en-us/library/dd233052(VS.100).aspx)
* [MSDN - Expression Trees](http://msdn.microsoft.com/en-us/library/bb397951(VS.100).aspx)
* [CodePlex - Dynamic Language Runtime](http://www.codeplex.com/dlr)
