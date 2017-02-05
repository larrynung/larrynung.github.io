---
title: Web Deploy - Delete local app pool
date: 2017-02-05 22:22:44
tags: [Web Deploy]
---

如要使用 Web Deploy 刪除本地 application pool，可以指定 Web Deploy 使用 delete 操作，dest 使用 appPoolConfig provider，並帶入要刪除的 application pool 名稱即可。  

<!-- More -->

    msdeploy –verb:delete –dest: appPoolConfig ="<DestAppPool>"

<br/>


{% asset_img 1.png %}

<br/>
