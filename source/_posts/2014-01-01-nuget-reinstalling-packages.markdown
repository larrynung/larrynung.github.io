---
layout: post
title: "NuGet - Reinstalling Packages"
date: 2014-01-01 23:11
comments: true
categories: NuGet
keywords: NuGet,Reinstall
description: "NuGet - Reinstalling Packages"
---

NuGet 在2.7版後開始支援重新安裝套件的功能，當碰到專案中的 NuGet 套件參考路徑錯誤，或是當專案的 .Net Framework 版本用的與 NuGet 套件用的不符時特別適用。

<!-- More -->

使用時先開啟 Package Manager Console 工具視窗，在裡面輸入命令:

    Update-Package -reinstall


NuGet 就會幫你重新加入所有使用到的套件。

若要指定重新安裝特定套件，可在命令後面帶上 Package

    Update-Package -reinstall [Package]


像是要指定重新安裝 Log4Net 就可以輸入命令:

    Update-Package -reinstall Log4Net

{% img /images/posts/NuGetReinstallingPackages/1.png %}


Link
----
* [Reinstalling Packages and its Pitfalls](http://docs.nuget.org/docs/workflows/reinstalling-packages)
