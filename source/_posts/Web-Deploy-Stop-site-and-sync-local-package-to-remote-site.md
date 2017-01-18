---
title: Web Deploy - Stop site and sync local package to remote site
date: 2017-01-18 13:54:39
tags: [Web Deploy]
---

如要使用 Web Deploy 將 Web Deploy Package 佈署到遠端站台，且要在佈署前停止 IIS，在佈署後啟動 IIS (Sop site => Sync local package to remote site => Start site
)。可以指定 Web Deploy 使用 sync 操作，presync 指定佈署前要運行的命令 (以這邊來說就是 appcmd.exe stop apppool <DestSite>)，postsync 指定佈署後要運行的命令 (以這邊來說就是 appcmd.exe start apppool <DestSite>)，source 使用 package provider，帶入 Web Deploy Package 的檔案位置，dest 這邊使用 appHostConfig，指定要佈署的本地站台，及用 computerName provider setting 指定遠端電腦的位置即可。

<!-- More -->

<br/>

透過 Remote Agent Service 去做遠端電腦連線的話，dest 這邊要使用 computerName provider setting 去指定遠端電腦的位置。  

    msdeploy -verb:sync -presync:runCommand="%windir%\system32\inetsrv\appcmd.exe stop apppool <DestSite>",successReturnCodes=0,waitinterval=15000,computerName=<DestServer> -source:package=<Package> -dest:appHostConfig="<DestSite>",computerName=<DestServer> -postsync:runCommand="%windir%\system32\inetsrv\appcmd.exe start apppool <DestSite>",successReturnCodes=0,waitinterval=15000,computerName=<DestServer>

<br/>


{% asset_img 1.png %}