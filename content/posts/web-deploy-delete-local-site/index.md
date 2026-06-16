---
title: "Web Deploy - Delete local site"
date: "2017-02-05 21:54:22"
description: "如要使用 Web Deploy 刪除本地站台，可以指定 Web Deploy 使用 delete 操作，dest 使用 appHostConfig provider，並帶入要刪除的站台名稱即可。 msdeploy –verb:delete –dest:apphostconfig=\"\""
tags: [Web Deploy]
---

如要使用 Web Deploy 刪除本地站台，可以指定 Web Deploy 使用 delete 操作，dest 使用 appHostConfig provider，並帶入要刪除的站台名稱即可。

msdeploy –verb:delete –dest:apphostconfig=""

![1.png](1.png)