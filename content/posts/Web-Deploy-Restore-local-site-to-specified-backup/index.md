---
title: "Web Deploy - Restore local site to specified backup"
date: "2016-12-29 13:33:57"
tags: [Web Deploy]
---


如要使用 Web Deploy 還原本地站台至指定備份，可以指定 Web Deploy 使用 sync 操作，source 使用 backupManager，dest 使用 backupManager，並指定要還原的站台以及要用來還原的備份檔。  

<!-- More -->

    msdeploy.exe -verb:sync -source:backupManager -dest:backupManager=<DestSite>/<BackupFile>

<br/>


![1.png](1.png)

<br/>
