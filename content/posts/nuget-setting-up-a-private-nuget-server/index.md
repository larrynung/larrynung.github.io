---
title: "NuGet - Setting up a private NuGet server"
date: "2014-02-23 12:11:00"
description: "要架設一台私人的 NuGet Server，我們可以先在 Visual Studio 上開啟一個空的網頁專案。 接著透過 NuGet 安裝 NuGet Server 這樣一個 NuGet Server 網站就已經準備完成了，直接將之在 Visual Studio 上運行起來看看，"
tags: [NuGet]
---

要架設一台私人的 NuGet Server，我們可以先在 Visual Studio 上開啟一個空的網頁專案。

![1.png](/images/posts/CreatePrivateNuGetServer/1.png)

接著透過 NuGet 安裝 NuGet Server

![2.png](/images/posts/CreatePrivateNuGetServer/2.png)

這樣一個 NuGet Server 網站就已經準備完成了，直接將之在 Visual Studio 上運行起來看看，應該可以看到 NuGet Server 實際運行起來的樣子。這邊會有一個精簡的頁面告知 NuGet Server 正在運行，並提供在 Visual Studio 上要用來設定的網址，以及怎樣發送 NuGet 套件上 NuGet Server。

![3.png](/images/posts/CreatePrivateNuGetServer/3.png)

在 Visual Studio 初步的測試沒問題的話，準備將整個網站部署到 IIS 上面

![4.png](/images/posts/CreatePrivateNuGetServer/4.png)

![5.png](/images/posts/CreatePrivateNuGetServer/5.png)

![6.png](/images/posts/CreatePrivateNuGetServer/6.png)

![7.png](/images/posts/CreatePrivateNuGetServer/7.png)

![8.png](/images/posts/CreatePrivateNuGetServer/8.png)

記得 IIS Website 的 Application pool 這邊要設定為使用 .Net 4.0

![9.png](/images/posts/CreatePrivateNuGetServer/9.png)

![10.png](/images/posts/CreatePrivateNuGetServer/10.png)

部署完成再用瀏覽器做個確定，應該會看到之前我們在 Visual Studio 試跑出來的畫面。

確定無誤，將 NuGet Package 放至指定位置，接著就可以將該 NuGet Server 加進 Visual Studio 內使用。

![11.png](/images/posts/CreatePrivateNuGetServer/11.png)

![12.png](/images/posts/CreatePrivateNuGetServer/12.png)