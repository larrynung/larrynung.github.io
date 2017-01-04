---
title: Web Deploy - Recycle remote application
date: 2017-01-04 13:48:31
tags: [Web Deploy]
---

如要使用 Web Deploy 回收遠端 Application，可以指定 Web Deploy 使用 sync 操作，source 使用 recyleApp，dest 使用 recycleApp，並帶入要回收的 Application，及用 computerName provider setting 指定遠端電腦的位置。  

<!-- More -->

    msdeploy -verb:sync -source:recycleApp -dest:recycleApp="<DestApp>" , computerName=<DestServer>

<br/>


{% asset_img 1.png %}

<br/>
