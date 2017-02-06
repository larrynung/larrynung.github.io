---
title: Web Deploy - Delete local site content
date: 2017-02-06 14:04:51
tags: [Web Deploy]
---

如要使用 Web Deploy 刪除本地站台內容，可以指定 Web Deploy 使用 delete 操作，dest 使用 contentPath provider，並帶入要刪除的 content 即可。  

<!-- More -->

    msdeploy -verb:delete -dest:contentPath=<ContentPath>

<br/>


{% asset_img 1.png %}

<br/>