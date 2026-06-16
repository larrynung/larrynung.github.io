---
title: "Web Deploy - Export package"
date: "2015-07-08 23:13:00"
description: "要將 IIS 網站 Application 或 Server 匯出，我們可以透過 Web Deploy 的匯出功能來做。先確定 Server 有安裝 Web Deploy，安裝後在 IIS 的 Application 或是 Server 節點上按下滑鼠右鍵，"
tags: [Web Deploy]
---

要將 IIS 網站 Application 或 Server 匯出，我們可以透過 Web Deploy 的匯出功能來做。先確定 Server 有安裝 Web Deploy，安裝後在 IIS 的 Application 或是 Server 節點上按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中應該會多出 Deploy 的功能選項。這邊點選 [Deploy | Export Server Package...] 選單選項。

![1.png](/images/posts/ExportWebDeployPackage/1.png)

點選後會彈出匯出對話框，可選取要匯出的內容。確定後點選 `Next` 按鈕繼續。

![2.png](/images/posts/ExportWebDeployPackage/2.png)

接著要設定參數的部份，設定完後一樣按下 `Next` 按鈕繼續。

![3.png](/images/posts/ExportWebDeployPackage/3.png)

最後這邊要選取匯出的檔案位置。

![4.png](/images/posts/ExportWebDeployPackage/4.png)

![5.png](/images/posts/ExportWebDeployPackage/5.png)

選取完按下 `Next` 按鈕進行匯出。

![6.png](/images/posts/ExportWebDeployPackage/6.png)

匯出完成會帶出 Summary 資訊。

![7.png](/images/posts/ExportWebDeployPackage/7.png)

Link
----
* [Export a Package through IIS Manager : The Official Microsoft IIS Site](http://www.iis.net/learn/publish/using-web-deploy/export-a-package-through-iis-manager)