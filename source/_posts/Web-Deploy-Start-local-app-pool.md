---
title: Web Deploy - Start local app pool
date: 2017-01-06 13:39:55
tags: [Web Deploy]
---

如要使用 Web Deploy 啟動本地 Application，可以指定 Web Deploy 使用 sync 操作，source 使用 recyleApp，dest 使用 recycleApp，並帶入要啟動的 Application，且指定 recyleMode 為 StartAppPool。  

<!-- More -->

    msdeploy -verb:sync -source:recycleApp -dest:recycleApp="<DestApp>",recycleMode="StartAppPool"

<br/>


{% asset_img 1.png %}

<br/>