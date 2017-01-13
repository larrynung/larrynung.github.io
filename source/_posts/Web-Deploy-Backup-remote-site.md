---
title: Web Deploy - Backup remote site
date: 2016-12-28 13:33:52
tags: [Web Deploy]
---

如要使用 Web Deploy 備份本地站台，可以指定 Web Deploy 使用 sync 操作，source 使用 backupManager，dest 也使用 backupManager，並指定要備份的站台名稱。  

<!-- More -->

<br/>

透過 Remote Agent Service 去做遠端電腦連線的話，dest 這邊要使用 computerName provider setting 去指定遠端電腦的位置。  

    msdeploy.exe -verb:sync -source:backupManager -dest:backupManager=<DestSite>,computerName=<DestServer>

<br/>


{% asset_img 1.png %}

<br/>


如果要透過 Web Management Service 去做遠端電腦連線的話，則 dest 這邊要使用 wmsvc provider setting 去指定遠端電腦的位置。  

    msdeploy.exe -verb:sync -source:backupManager -dest:backupManager=<DestSite>,wmsvc=<DestServer>,userName=<UserName>,password=<Password> -allowUntrusted


<br/>


{% asset_img 2.png %}

<br/>