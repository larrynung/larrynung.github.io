---
title: "LogDevice - Removing log using ldshell"
date: 2018-10-10 23:31:32
tags: [LogDevice]
---

要使用 ldshell 刪除 LogDevice 的 Log，可以使用 -c 參數指定使用 Interactive Mode，帶入  LogDevice 的設定檔，帶入 logs remove 及指定要刪除的 Log 即可。  

<!-- More -->

    ldshell -c <Config> logs remove <Log>

{% asset_img 1.png %}

<br/>


Link
---
* [Log configuration · LogDevice](https://logdevice.io/docs/Logs.html)
