---
title: "Web Deploy - Import Package"
date: "2015-07-10 21:48:00"
description: "Web Deploy - Import Package"
tags: [Web Deploy]
---

要將 Application 或 Server 的匯出檔匯入 IIS，我們可以透過 Web Deploy 的匯入功能來做。先確定 Server 有安裝 Web Deploy，安裝後在 IIS 的 Application 或是 Server 節點上按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中應該會多出 Deploy 的功能選項。這邊點選 [Deploy | Import Server Package…] 選單選項。

![1.png](/images/posts/ImportWebDeployPackage/1.png)

點選後會彈出匯入對話框，選取要匯入的匯出檔。

![2.png](/images/posts/ImportWebDeployPackage/2.png)

![3.png](/images/posts/ImportWebDeployPackage/3.png)

![4.png](/images/posts/ImportWebDeployPackage/4.png)

接著要選取要匯入的內容。確定後點選 `Next` 按鈕繼續。

![5.png](/images/posts/ImportWebDeployPackage/5.png)

接著會彈出確認對話框，確認是否要進行匯入的動作，確定無誤則按下 `OK` 按鈕繼續。

![6.png](/images/posts/ImportWebDeployPackage/6.png)

匯入完成會帶出 Summary 資訊，按下 `Finish` 按鈕即可。

![7.png](/images/posts/ImportWebDeployPackage/7.png)

對話框關閉後我們可以看到網站已被正常的匯入。

![8.png](/images/posts/ImportWebDeployPackage/8.png)

Link
----
* [Import a Package through IIS Manager : The Official Microsoft IIS Site](http://www.iis.net/learn/publish/using-web-deploy/import-a-package-through-iis-manager)