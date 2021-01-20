---
title: dotnet-counters - Install with dotnet tool
date: 2021-01-20 06:51:32
tags: [dotnet-counters]
---

要用 dotnet tool 安裝 dotnet-counters，可調用 d    otnet tool install 帶入 --global 參數指定安裝至全域，並在最後帶入 dotnet-counters 指定安裝 dotnet-counters 套件。     

<!-- More -->                               

    dotnet tool install --global dotnet-counters

{% asset_img 1.png %}                      

<br>


安裝後可調用 dotnet-counters 命令，帶入 --version 參數，確認安裝是否正確無誤。             


    dotnet-counters --version

{% asset_img 2.png %}

<br>


 Link
 ====
* [dotnet-counters diagnostic tool - .NET CLI | Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/core/diagnostics/dotnet-counters)
