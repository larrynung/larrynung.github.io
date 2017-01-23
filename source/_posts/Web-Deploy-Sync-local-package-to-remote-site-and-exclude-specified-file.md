---
title: Web Deploy - Sync local package to remote site and exclude specified file
date: 2017-01-23 13:55:35
tags: [Web Deploy]
---

如要使用 Web Deploy 將 Web Deploy Package 佈署到遠端站台並忽略同步指定的檔案，可以指定 Web Deploy 使用 sync 操作，source 使用 package provider，帶入 Web Deploy Package 的檔案位置，dest 這邊使用 appHostConfig，指定要佈署的本地站台，用 skip operation setting 指定 objectname 為 `filePath`，absolutepath 帶入要忽略同步的檔案位置。  

<!-- More -->

<br/>

透過 Remote Agent Service 去做遠端電腦連線的話，dest 這邊要使用 computerName provider setting 去指定遠端電腦的位置。  

    msdeploy -verb:sync -source:package=<Package> -dest:appHostConfig="<DestSite>",computerName=<DestServer> -skip:objectname='filePath',absolutepath='<FilePath>'

<br/>


{% asset_img 1.png %}

<br/>