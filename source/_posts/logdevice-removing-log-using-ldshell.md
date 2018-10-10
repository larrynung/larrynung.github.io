---
title: "LogDevice - Removing log using ldshell"
date: 2018-10-10 23:31:32
tags: [LogDevice]
---

要使用 ldshell 刪除 LogDevice 的 log，可以使用 -c 參數指定 LogDevice 的設定檔，後面帶著 logs remove 指定要刪除的 log。  

<!-- More -->

    ldshell -c <Config> logs remove <Log>

{% asset_img 1.png %}

<br/>


Link
---
* [Log configuration · LogDevice](https://logdevice.io/docs/Logs.html)
