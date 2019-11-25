---
title: dotnet-dump - Analyze .Net Core dump file
date: 2019-11-25 08:40:09
tags: [dotnet-dump]
---

Dump 出 .Net Core 的 Dump file 後。  

<!-- More -->

{% asset_img 1.png %}

</br>


可使用 dotnet-dump analyze 帶上 Dump file 的位置進行 Dump 檔的分析。  

    dotnet-dump analyze $dump_file

{% asset_img 2.png %}

</br>


分析是使用 SOS 命令，像是要查詢 Thread，可輸入 clrthreads 命令。  

    clrthreads

{% asset_img 3.png %}

</br>


要查詢呼叫堆疊，可輸入 clrstack 命令。  

    clrstack

{% asset_img 4.png %}

</br>


要查看是什麼錯誤導致程式死掉，可使用 pe 命令。

    pe -lines

{% asset_img 5.png %}
