---
layout: post
title: ".NET Core - Getting started"
date: 2016-01-16 18:05:00
comments: true
tags: [.NET Core]
keywords: ".NET Core"
description: ".NET Core - Getting started"
---

要使用 .NET Core，首先需至 [Getting started with .NET Core](http://dotnet.github.io/getting-started/) 這邊下載對應的安裝檔案。  

<!-- More -->

{% img /images/posts/DotnetCoreGettingStarted/1.png %}

<br/>


接著執行下載下來的安裝包進行安裝。  

{% img /images/posts/DotnetCoreGettingStarted/2.png %}

<br/>


{% img /images/posts/DotnetCoreGettingStarted/3.png %}

<br/>


{% img /images/posts/DotnetCoreGettingStarted/4.png %}

<br/>


{% img /images/posts/DotnetCoreGettingStarted/5.png %}

<br/>


{% img /images/posts/DotnetCoreGettingStarted/6.png %}

<br/>


{% img /images/posts/DotnetCoreGettingStarted/7.png %}

<br/>


接著開啟命令列，建立一個專案目錄，在專案目錄下輸入命令 dotnet new 建立 .NET Core 的專案，建立的專案內應該會含有 NuGet.Config、Program.cs、project.json 這三個檔案。  

{% img /images/posts/DotnetCoreGettingStarted/8.png %}

<br/>


接著我們要呼叫命令 dotnet restore 將依賴的套件進行還原。  

{% img /images/posts/DotnetCoreGettingStarted/9.png %}

<br/>


還原後輸入命令 dotnet run 運行專案即可。  

{% img /images/posts/DotnetCoreGettingStarted/10.png %}

<br/>


Link
----
* [Getting started with .NET Core](http://dotnet.github.io/getting-started/)
