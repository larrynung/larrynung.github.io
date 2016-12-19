---
title: Web Deploy - Dump remote available backups
date: 2016-12-20 00:02:34
tags: [Web Deploy]
---

如要使用 Web Deploy 將遠端可以使用的備份資訊 dump 出來，可以指定 Web Deploy 使用
 dump 操作，source 使用 backupManager，帶入要查詢的站台名稱，及用 computerName provider setting 指定遠端電腦的位置即可。

<!-- More -->

    msdeploy.exe -verb:dump -source:backupManager=<SourceSite>,computerName=<DestServer>

<br/>


{% asset_img 1.png %}

<br/>


