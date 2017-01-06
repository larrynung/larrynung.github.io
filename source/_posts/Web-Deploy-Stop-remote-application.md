---
title: Web Deploy - Stop remote application
date: 2017-01-05 23:51:31
tags: [Web Deploy]
---

如要使用 Web Deploy 停止遠端 Application，可以指定 Web Deploy 使用 sync 操作，source 使用 recycleApp，dest 使用 recycleApp，並帶入要回收的 Application，指定 recylceMode 為 StopAppPool，及用 computerName provider setting 指定遠端電腦的位置。  

<!-- More -->

    msdeploy -verb:sync -source:recycleApp -dest:recycleApp="<DestApp>",recycleMode=" StopAppPool" , computerName=<DestServer>

<br/>


{% asset_img 1.png %}

<br/>
