---
title: LogDevice - Write data into a log
date: 2018-10-05 23:42:52
tags: [LogDevice]
---

要將 Log 寫入 LogDevice，需要用 echo 輸出要寫入的 data，用 Pipline 將之帶入 ldwrite，並指定設定檔位置，以及要寫入的位置即可。  

<!-- More -->

    echo <Data> | ldwrite <Config> <Sequence>

<br/>


像這邊筆者就將 hello 這樣的資料寫到了 LogDevice 的第一個位置。

{% asset_img 1.png %}
 
<br/>


Link
----
* [Creating your first cluster · LogDevice](https://logdevice.io/docs/FirstCluster.html)
