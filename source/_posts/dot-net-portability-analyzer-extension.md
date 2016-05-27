---
layout: post
title: ".NET Portability Analyzer Extension"
date: 2014-12-07 23:59:00
comments: true
categories: [Visual Studio]
keywords: ".NET, Extension" 
description: ".NET Portability Analyzer Extension"
---

.NET Portability Analyzer Extension 是微軟出的 Visual Studio 擴充套件，能偵測程式是否具備 Portability，並針對不具 Portability 的地方提供對應的修改建議，讓開發人員在做跨平臺的開發上更加的便利。 

<!-- More -->

{% img /images/posts/PortabilityAnalyzerExtension/1.png %}

<br/>

Channel9 這邊有相關的介紹影片，建議可以稍微瀏覽一下，可以幫助我們快速上手。  
<iframe src="//channel9.msdn.com/Blogs/funkyonex/Fun-with-the-Interns-Charles-Lowell-on-the-NET-API-Portability-Analyzer/player" width="960" height="540" allowFullScreen frameBorder="0"></iframe>

<br/>


使用前記得先將擴充套件裝上。 

<br/>

裝好後需先至 Options 這邊設定所要分析的平臺。 

{% img /images/posts/PortabilityAnalyzerExtension/2.png %}

<br/>


在使用上，該擴充套件有兩種不同的使用方式。一種是對選取的組件進行分析，透過 [Analyze/Analyze Assembly Portability...] 主選單選項去觸發。 

{% img /images/posts/PortabilityAnalyzerExtension/3.png %}

<br/>


{% img /images/posts/PortabilityAnalyzerExtension/4.png %}

<br/>


產生的報表能顯示出程式在各平台的支援程度，及細部的支援比較。  
{% img /images/posts/PortabilityAnalyzerExtension/5.png %}

<br/>


另一種則是對選取的專案進行分析，透過方案總管的滑鼠右鍵選單選項觸發。 

{% img /images/posts/PortabilityAnalyzerExtension/6.png %}

<br/>


一樣會產生類似的報表，但是因為透過專案的方式觸發有程式原碼，所以報表還會進一步的給予我們對應的修改建議，Error List 工具視窗這邊也會顯示出對應的訊息。  
{% img /images/posts/PortabilityAnalyzerExtension/7.png %}

<br/>

Link
----
* [.NET Portability Analyzer extension](https://visualstudiogallery.msdn.microsoft.com/1177943e-cfb7-4822-a8a6-e56c7905292b)
* [Leveraging existing code across .NET platforms - .NET Blog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/dotnet/archive/2014/08/06/leveraging-existing-code-across-net-platforms.aspx)
