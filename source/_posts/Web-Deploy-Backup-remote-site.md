---
title: Web Deploy - Backup remote site
date: 2016-12-28 13:33:52
tags: [Web Deploy]
---

如要使用 Web Deploy 備份本地站台，可以指定 Web Deploy 使用 sync 操作，source 使用 backupManager，dest 也使用 backupManager，並指定要備份的站台名稱，及用 computerName provider setting 指定遠端電腦的位置。  

<!-- More -->

    msdeploy.exe -verb:sync -source:backupManager -dest:backupManager=<DestSite>,computerName=<DestServer>

<br/>


{% asset_img 1.png %}

<br/>