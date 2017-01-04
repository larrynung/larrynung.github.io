---
title: "Web Deploy - Recycle local application"
date: 2017-01-03 13:36:33
tags: [Web Deploy]
---

如要使用 Web Deploy 回收本地 Application，可以指定 Web Deploy 使用 sync 操作，source 使用 recyleApp，dest 使用 recycleApp，並帶入要回收的 Application。  

<!-- More -->

    msdeploy -verb:sync -source:recycleApp -dest:recycleApp="<DestApp>"

<br/>


{% asset_img 1.png %}

<br/>
