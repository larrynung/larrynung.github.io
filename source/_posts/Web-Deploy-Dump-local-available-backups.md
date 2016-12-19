---
title: Web Deploy - Dump local available backups
date: 2016-12-19 23:53:26
tags: [Web Deploy]
---

如要使用 Web Deploy 將本地可以使用的備份資訊 dump 出來，可以指定 Web Deploy 使用 dump 操作，source 使用 backupManager，帶入要查詢的站台名稱即可。  

<!-- More -->

    msdeploy.exe -verb:dump -source:backupManager=<SourceSite>

<br/>


{% asset_img 1.png %}

<br/>

