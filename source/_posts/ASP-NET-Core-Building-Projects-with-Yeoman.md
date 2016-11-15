---
title: ASP.NET Core - Building Projects with Yeoman
date: 2016-11-15 23:53:54
tags: [ASP.NET Core]
---

要使用 Yeoman 去建立 ASP.NET Core 專案，首先需安裝 Yeoman 與 bower。  

<!-- More -->

    npm install -g yo bower

<br/>


再來要安裝 ASP.NET generator。  

    npm install -g generator-aspnet

{% asset_img 1.png %}

<br/>


ASP.NET generator 安裝完後，透過 Yeoman 叫用 ASP.NET generator。  

    yo aspnet

{% asset_img 2.png %}

<br/>


選取要使用的應用程式範本。  

{% asset_img 3.png %}

<br/>


設定應用程式名稱，Yeoman 就會幫我們建立應用程式專案。  

{% asset_img 4.png %}

<br/>


應用程式專案建立完整個目錄結構會像下面這樣：  

{% asset_img 5.png %}

<br/>


到這邊就可以開啟專案來開發應用程式了，開發完成，我們可以還原會使用到的套件。  

    dotnet restore

{% asset_img 6.png %}

<br/>


然後將應用程式運行起來看看 (dotnet run 會順帶運行 dotnet build，這種情況下 dotnet build 可省略不調用)。  

    dotnet build
    dotnet run


{% asset_img 7.png %}

<br/>


{% asset_img 8.png %}

<br/>


Link
----
* [Building Projects with Yeoman](https://docs.microsoft.com/en-us/aspnet/core/client-side/yeoman)
* [Creating a new ASP.NET Core project using Yeoman · asp.net core from the ground up](https://openlearningportal.gitbooks.io/all-about-asp-net-core/content/creating_a_new_aspnet_core_project_using_yeoman.html)
