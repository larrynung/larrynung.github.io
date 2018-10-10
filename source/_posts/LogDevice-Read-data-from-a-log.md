---
title: LogDevice - Read data from a log
date: 2018-10-07 23:26:39
tags: [LogDevice]
---

要讀取 LogDevice 內的資料，可以調用 ldtail 命令，帶入設定檔位置以及要讀取的位置。  

<!-- More -->

    ldtail <Config> <Sequence>

<br/>


像是筆者就將 hello 寫入了 LogDevice 內的第一個位置，可像下面這樣將之讀出。  

{% asset_img 1.png %}

<br/>


Link
----
* [Creating your first cluster · LogDevice](https://logdevice.io/docs/FirstCluster.html)
