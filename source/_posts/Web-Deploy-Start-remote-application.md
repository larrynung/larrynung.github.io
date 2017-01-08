---
title: Web Deploy - Start remote application
date: 2017-01-08 23:00:12
tags: [Web Deploy]
---

如要使用 Web Deploy 啟動遠端 Application，可以指定 Web Deploy 使用 sync 操作，source 使用 recycleApp，dest 使用 recycleApp，並帶入要回收的 Application，且指定 recycleMode 為 StartAppPool，及用 computerName provider setting 指定遠端電腦的位置。  

<!-- More -->

    msdeploy -verb:sync -source:recycleApp -dest:recycleApp="<DestApp>",recycleMode="StartAppPool", computerName=<DestServer>

<br/>


