---
title: Web Deploy - Dump remote site
date: 2016-12-19 23:45:43
tags: [Web Deploy]
---

如要使用 Web Deploy 將遠端站台資訊 dump 出來，可以指定 Web Deploy 使用 dump 操作
，因為站台的指定是用 appHostConfig provider，所以將 source 指定為 appHostConfig provider，並帶入站台的名稱，及用 computerName provider setting 指定遠端電腦的位置即可。

<!-- More -->

    msdeploy -verb:dump -source:appHostConfig="<SourceSite>",computerName=<SourceServer>


<br/>


{% asset_img 1.png %}

<br/>

