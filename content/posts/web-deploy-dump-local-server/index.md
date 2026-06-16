---
title: "Web Deploy - Dump local server"
date: "2016-12-16 13:50:18"
description: "如要使用 Web Deploy 將本地 server 資訊 dump 出來，可以指定 Web Deploy 使用 dump 操作，並將 source 指定為 WebServer provider 即可。 msdeploy -verb:dump -source:webServer"
tags: [Web Deploy]
---

如要使用 Web Deploy 將本地 server 資訊 dump 出來，可以指定 Web Deploy 使用 dump 操作，並將 source 指定為 WebServer provider 即可。

msdeploy -verb:dump -source:webServer

![1.png](1.png)