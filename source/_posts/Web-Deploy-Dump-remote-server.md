---
title: Web Deploy - Dump remote server
date: 2016-12-19 13:40:40
tags: [Web Deploy]
---

如要使用 Web Deploy 將遠端 server 資訊 dump 出來，可以指定 Web Deploy 使用 dump 操作，將 source 指定為 WebServer provider，用 computerName provider setting 指定遠端電腦的位置即可。

<!-- More -->

    msdeploy -verb:dump -source:webServer,computerName=<DestServer>

<br/>


{% asset_img 1.png %}

<br/>