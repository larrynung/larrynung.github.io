---
layout: post
title: "Roslyn - Introduce diagnostic analyzer"
date: 2014-11-12 22:55
comments: true
categories: [Roslyn]
keywords: "Roslyn, Analyzer"
description: "Roslyn - Introduce diagnostic analyzer"
---

Diagnostic Analyzer 功能是用來診斷分析程式碼的，開發人員可自行撰寫 Diagnostic Analyzer 去擴充 Roslyn 的編譯器，實作自己的程式碼診斷邏輯。  

<!-- More -->

<br/>

他有兩種不同的使用方式，一種是包裝成 VSIX 檔，需要安裝使用。安裝後 Diagnostic Analyzer 的診斷會針對 Visual Studio 開啟的所有專案，就好像是內建的診斷一般。  


<br/>

另一種則是建置成一般的 Dll 檔，需要依需求在個別專案中引用使用。使用上需搭配 Visual Studio 14 以後的版本，在方案總管中找到 Analyzers 節點，按右鍵加入 Analyzer。或是直接透過 NuGet 加入引用也可以。  

<br/>


最後這邊可以看一下 Channel9 的介紹，這段影片會介紹他自己寫的 Diagnostic Analyzer是如何對 C# 6.0 的 Feature 做出診斷與建議，並帶到一些實作上的細節，看完相信對於 Diagnostic Analyzer 會更加的了解。  

<iframe src="//channel9.msdn.com/Blogs/Roslyn/Analyzer-sample-in-Dev14-CTP3/player" width="960" height="540" allowFullScreen frameBorder="0"></iframe>
