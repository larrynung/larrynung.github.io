---
title: LogDevice - Rename log using ldshell
date: 2018-10-11 00:00:52
tags: [LogDevice]
---

要使用 ldshell 將 LogDevice 的 Log 更名，可以使用 -c 參數指定使用 Interactive Mode，帶入 LogDevice 的設定檔，帶入 logs rename 以及新舊 Log name 即可。  

<!-- More -->

    ldshell -c <Config> logs rename <OldLogName> <NewLogName>

{% asset_img 1.png %}

<br/>


Link
----
* [Log configuration · LogDevice](https://logdevice.io/docs/Logs.html)
