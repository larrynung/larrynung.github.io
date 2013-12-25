---
layout: post
title: "NuGet - Local cache source"
date: 2013-12-25 22:45
comments: true
categories: Nuget
keywords: NuGet
description: "NuGet - Local cache source"
---

在安裝 NuGet 套件時，NuGet 會將使用到的 Package 存放起來以備後續重覆安裝時使用。存放的套件若有需要，我們可開啟 Visual Studio 的 Options 對話框，切換到 Package Manager 下的 General 頁籤，進行 Package 的清除或是瀏覽。  

<!--More-->

{% img /images/posts/NuGetLocalCacheSource/1.png %}


這邊點選 `Browse...` 按鈕，我們可以查看 NuGet 幫我們快取了哪些 NuGet 套件。  

{% img /images/posts/NuGetLocalCacheSource/2.png %}


這邊我們可以將該目錄位置複製下來，再次回到 Options 對話框，這次切到 Package Manager 下的 Package Sources 頁籤。在這邊添加一個 Source ，Source 位置指到我們剛剛所複製的位置，也就是 NuGet 套件快取所存放的位置。  

{% img /images/posts/NuGetLocalCacheSource/3.png %}


設定好後按下 OK 按鈕將 Options 對話框關閉。接著開啟 Manage NuGet Packages 對話框，左側 Source選用剛剛我們所新加的 Source ，我們可以看到所有快取的 NuGet 套件，這代表著我們可以在此使用快取的 NuGet 套件進行安裝，即使此時網路無法連至 NuGet Server。  

{% img /images/posts/NuGetLocalCacheSource/4.png %}


Link
----
* [Install NuGet Packages from the Cache](http://ihadthisideaonce.com/2012/03/09/install-nuget-packages-from-the-cache/)
* [How to access NuGet when NuGet.org is down (or you're on a plane)](http://www.hanselman.com/blog/HowToAccessNuGetWhenNuGetorgIsDownOrYoureOnAPlane.aspx)
