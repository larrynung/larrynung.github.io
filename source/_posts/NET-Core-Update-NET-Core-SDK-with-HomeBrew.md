---
title: .NET Core - Update .NET Core SDK with HomeBrew
date: 2019-12-12 08:24:39
tags: [.NET Core, HomeBrew]
---

用 HomeBrew 安裝的 .NET core SDK，可直接用 HomeBrew 進行更新。  

<!-- More -->

</br>


像是筆者電腦中的 .NET Core SDK 是 3.0 的版本。

    dotnet --version

{% asset_img 1.png %}

</br>


要升級到最新版的 .NET core SDK 3.1，可直接透過 HomeBrew cask reinstall 命令去更新 dotnet-sdk 套件。

    brew cask reinstall dotnet-sdk

{% asset_img 2.png %}

</br>


.NET core SDK 就會被要升級到 3.1 最新版。

    dotnet --version

{% asset_img 3.png %}
