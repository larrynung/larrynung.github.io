---
title: Web Deploy - Start remote application
date: 2017-01-08 23:00:12
tags: [Web Deploy]
---

如要使用 Web Deploy 去啟動遠端 Application，可以指定 Web Deploy 使用 sync 操作，source 使用 recycleApp，dest 使用 recycleApp，並帶入要回收的 Application，且指定 recycleMode 為 StartAppPool。  

<!-- More -->

<br/>

透過 Remote Agent Service 去做遠端電腦連線的話，dest 這邊要使用 computerName provider setting 去指定遠端電腦的位置。  

    msdeploy -verb:sync -source:recycleApp -dest:recycleApp="<DestApp>",recycleMode="StartAppPool", computerName=<DestServer>

<br/>


{% asset_img 1.png %}

<br/>


如果要透過 Web Management Service 去做遠端電腦連線的話，則 dest 這邊要使用 wmsvc provider setting 去指定遠端電腦的位置。  

    msdeploy -verb:sync -source:recycleApp -dest:recycleApp="<DestApp>",recycleMode="StartAppPool",wmsvc=<DestServer>,userName=<UserName>,password=<Password> -allowUntrusted


<br/>


{% asset_img 2.png %}

<br/>
