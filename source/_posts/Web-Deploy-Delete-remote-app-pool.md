---
title: Web Deploy - Delete remote app pool
date: 2017-02-05 22:42:06
tags: [Web Deploy]
---

如要使用 Web Deploy 刪除遠端 application pool，可以指定 Web Deploy 使用 delete 操作，dest 使用 appPoolConfig provider，並帶入要刪除的 application pool 名稱，及用 computerName provider setting 指定遠端電腦的位置。

<!-- More -->

    msdeploy –verb:delete –dest: appPoolConfig ="<DestAppPool>",computerName=<DestServer>

<br/>


{% asset_img 1.png %}

<br/>

