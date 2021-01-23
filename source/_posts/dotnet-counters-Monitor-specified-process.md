---
title: dotnet-counters - Monitor specified process
date: 2021-01-21 09:09:50
tags: [dotnet-counters]
---

dotnet-counters 可用來監控 .Net Core 的 Process，像是這邊筆者準備了一份簡單的程式想要觀察其 CPU 與 Memory 這些資源上的變化狀況。  

<!-- More -->

{% asset_img 1.png %}

<br>


將程式運行起來。  

    dotnet run

{% asset_img 2.png %}

<br>


運行起來後可用 dotnet-trace 查詢 Process。  

    dotnet-trace ps

{% asset_img 3.png %}

<br>


接著就可透過 dotnet-counters 監控指定 Process 的資源使用狀態。  

    dotnet-counters monitor --refresh-interval $refreshInterval -p $processId

<br>


像是這邊剛剛查閱到了 dotnet run 起了兩個 Process，我們可以帶入 Process Id 監控。  

    dotnet-counters monitor --refresh-interval 1 -p 35603

{% asset_img 4.png %}

<br>


{% asset_img 5.png %}

<br>


    dotnet-counters monitor --refresh-interval 1 -p 35608

{% asset_img 6.png %}

<br>


{% asset_img 7.png %}

<br>


dotnet-counters 會將指定 Process 的資源使用狀況依照指定的時間更新，直至程式結束。  

{% asset_img 8.png %}

<br>


{% asset_img 9.png %}

<br>


{% asset_img 10.png %}

<br>


Link
====
* [Debug high CPU usage - .NET Core | Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/core/diagnostics/debug-highcpu?tabs=linux)
