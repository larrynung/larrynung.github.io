---
title: Web Deploy - Stop local application
date: 2017-01-05 13:33:29
tags: [Web Deploy]
---

如要使用 Web Deploy 停止本地 Application，可以指定 Web Deploy 使用 sync 操作，source 使用 recycleApp，dest 使用 recycleApp，並帶入要回收的 Application，且指定 recycleMode 為 StopAppPool。  

<!-- More -->

    msdeploy -verb:sync -source:recycleApp -dest:recycleApp="<DestApp>",recycleMode="StopAppPool"

<br/>


{% asset_img 1.png %}

<br/>
