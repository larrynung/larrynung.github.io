---
title: Web Deploy - Sync local site to local package
date: 2016-12-26 22:58:25
tags: [Web Deploy]
---

要用 Web Deploy 將本地站台打包成 Web Deploy Package，可以指定 Web Deploy 使用 sync 操作，source 使用 appHostConfig provider，帶入要打包的站台名稱，dest 使用 package provider，指定打包後的 Web Deploy Package 位置即可。

<!-- More -->

<br/>

    msdeploy -verb:sync -source:appHostConfig="<SourceSite>" -dest: package=<Package> 

<br/>


{% asset_img 1.png %}

<br/>
