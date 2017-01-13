---
title: Web Deploy - Dump remote site
date: 2016-12-19 23:45:43
tags: [Web Deploy]
---

如要使用 Web Deploy 將遠端站台資訊 dump 出來，可以指定 Web Deploy 使用 dump 操作
，因為站台的指定是用 appHostConfig provider，所以將 source 指定為 appHostConfig provider，並帶入站台的名稱。  

<!-- More -->

<br/>

透過 Remote Agent Service 去做遠端電腦連線的話，dest 這邊要使用 computerName provider setting 去指定遠端電腦的位置。  

    msdeploy -verb:dump -source:appHostConfig="<SourceSite>",computerName=<SourceServer>


<br/>


{% asset_img 1.png %}

<br/>


如果要透過 Web Management Service 去做遠端電腦連線的話，則 dest 這邊要使用 wmsvc provider setting 去指定遠端電腦的位置。  

    msdeploy -verb:dump -source:appHostConfig="<SourceSite>",wmsvc=<DestServer>,userName=<UserName>,password=<Password> -allowUntrusted


<br/>


{% asset_img 2.png %}

<br/>