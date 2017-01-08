---
title: Web Deploy - Stop remote IIS
date: 2017-01-08 23:35:42
tags: [Web Deploy]
---

如要使用 Web Deploy 停止遠端 IIS，可以指定 Web Deploy 使用 sync 操作，source 使用 runcommand，dest 使用 runcommand，並帶入要運行的遠端命令（以這邊來說就是用 iisreset /stop 去停止 IIS 的命令），及用 computerName provider setting 指定遠端電腦的位置。  

<!-- More -->

    msdeploy -verb:sync -source:runcommand -dest:runCommand="iisreset /stop",computerName=<DestServer>

<br/>


{% asset_img 1.png %}

<br/>
