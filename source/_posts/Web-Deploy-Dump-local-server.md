---
title: Web Deploy - Dump local server
date: 2016-12-16 13:50:18
tags: [Web Deploy]
---

如要使用 Web Deploy 將本地 server 資訊 dump 出來，可以指定使用 dump 操作，並將 source provider 指定為 WebServer provider 即可。

<!-- More -->

    msdeploy -verb:dump -source:webServer

<br/>


{% asset_img 1.png %}

<br/>