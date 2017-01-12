---
title: Web Deploy - Recycle remote application
date: 2017-01-04 13:48:31
tags: [Web Deploy]
---

如要使用 Web Deploy 回收遠端 Application，可以指定 Web Deploy 使用 sync 操作，source 使用 recyleApp，dest 使用 recycleApp，並帶入要回收的 Application。  

<!-- More -->

<br/>

透過 Remote Agent Service 去做遠端電腦連線的話，dest 這邊要使用 computerName provider setting 去指定遠端電腦的位置。 

    msdeploy -verb:sync -source:recycleApp -dest:recycleApp="<DestApp>",computerName=<DestServer>

<br/>


{% asset_img 1.png %}

<br/>


如果要透過 Web Management Service 去做遠端電腦連線的話，則 dest 這邊要使用 wmsvc provider setting 去指定遠端電腦的位置。  

    msdeploy -verb:sync -source:recycleApp -dest:recycleApp="<DestApp>",wmsvc=<DestServer>,userName=<UserName>,password=<Password> -allowUntrusted


<br/>


{% asset_img 2.png %}

<br/>
