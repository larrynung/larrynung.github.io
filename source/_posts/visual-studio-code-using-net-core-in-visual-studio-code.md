---
title: "Visual Studio Code - Using .NET Core in Visual Studio Code"
date: 2017-09-06 12:09:03
tags: [Visual Studio Code]
---

要用 Visual Studio Code 開發 .NET Core，需先安裝 .NET Core SDK。  

<!-- More -->

<br/>


然後安裝 Visual Studio Code 的 C# Extension。  

{% asset_img 1.png %}

<br/>


C# Extension 安裝後進行重啟。  

{% asset_img 2.png %}

<br/>


{% asset_img 3.png %}

<br/>


將 Visual Studio Code 切至專案目錄，透過 Terminal 視窗建立專案。  

    dotnet new [ProjectTemplate]

{% asset_img 4.png %}

<br/>


{% asset_img 5.png %}

<br/>


還原套件。  

    dotnet restore

{% asset_img 6.png %}

<br/>


運行結果。  

    dotnet run

{% asset_img 7.png %}

<br/>


若要除錯的話，需先建立 launch.json 檔。  

{% asset_img 8.png %}

<br/>


{% asset_img 9.png %}

<br/>


將 program 位置設為專案輸出檔的位置，以筆者這邊的例子來說就是 "${workspaceRoot}/bin/BPC/Debug/netcoreapp1.1/Test.dll"。  

{% asset_img 10.png %}

<br/>


再來建立 task.json 檔。  

{% asset_img 11.png %}

<br/>


{% asset_img 12.png %}

<br/>


{% asset_img 13.png %}

<br/>


{% asset_img 14.png %}

<br/>


最後設斷點啟動除錯即可。  

{% asset_img 15.png %}

<br/>


{% asset_img 16.png %}

<br/>


Link
----
* [C# programming with Visual Studio Code](https://code.visualstudio.com/docs/languages/csharp)
* [.NET Core and Visual Studio Code](https://code.visualstudio.com/docs/other/dotnet)
* [Get started with C# and Visual Studio Code - C# Guide | Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/core/tutorials/with-visual-studio-code)