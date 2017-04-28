---
title: NuGet - Can't find online packages
date: 2017-04-28 13:29:36
tags: [NuGet]
---

使用 NuGet 時，若碰到查詢線上的 NuGet 套件一直在 Loding，且透過 'Package Manager Console' 下命令也無法進行套件的安裝的話。  

<!-- More -->

{% asset_img 1.png %}

<br/>


可嘗試將 '%AppData%\NuGet\Nuget.config' 刪除。  

{% asset_img 2.png %}

<br/>


並將 Visual Studio 重啟，沒意外的話應該就會恢復正常了。  

{% asset_img 3.png %}

<br/>


Link
----
* [visual studio - Manage NugetPackage for Solution can't find any online packages - Stack Overflow](http://stackoverflow.com/questions/30845856/manage-nugetpackage-for-solution-cant-find-any-online-packages)