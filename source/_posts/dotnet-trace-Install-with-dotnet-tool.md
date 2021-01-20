---
title: dotnet-trace - Install with dotnet tool
date: 2021-01-18 08:58:33
tags: [dotnet-trace]
---

要用 dotnet tool 安裝 dotnet-trace，可調用 dotnet tool install 帶入 --global 參數指定安裝至全域，並在最後帶入 dotnet-trace 指定安裝
dotnet-trace 套件。  

<!-- More -->

    dotnet tool install --global dotnet-trace

{% asset_img 1.png %}

<br>


安裝後可調用 dotnet-trace 命令，帶入 --version 參數，確認安裝是否正確無誤。  

    dotnet-trace --version

{% asset_img 2.png %}

<br>


Link
====
* [dotnet-trace diagnostic tool - .NET CLI | Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/core/diagnostics/dotnet-trace)
