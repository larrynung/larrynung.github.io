---
title: "Web Deploy - Install  setup web deploy"
date: "2016-12-05 23:31:31"
description: "Web Deploy 程式可至微軟網站下載。 下載完點擊安裝。 安裝類型建議選取 Custom，確認一下要安裝的元件。 這邊的元件有 IIS Manager UI 模組，安裝完會將 Web Deploy 部分功能整合在 IIS Manager。"
tags: [Web Deploy]
---

Web Deploy 程式可至微軟網站下載。

![1.png](1.png)

![2.png](2.png)

下載完點擊安裝。

![3.png](3.png)

![4.png](4.png)

![5.png](5.png)

安裝類型建議選取 Custom，確認一下要安裝的元件。

![6.png](6.png)

這邊的元件有 IIS Manager UI 模組，安裝完會將 Web Deploy 部分功能整合在 IIS Manager。比較重要的需要確認 Management Service 與 Remote Agent Service 的安裝狀況，因為 Web Deploy 佈署時可能會走這兩條路 ，所以需要視需要將之勾選安裝。

![7.png](7.png)

![8.png](8.png)

![9.png](9.png)

![10.png](10.png)

如果剛有選取 Manager Service 或是 Remote Agent Service，安裝完就可以看到系統內會有新增對應的服務(Web Management Service 與 Web Deployment Agent Service)，我們需要確保服務是正常啟用的。

![11.png](11.png)

除了確定服務啟動外，也可以開啟瀏覽器訪問 `http://localhost/MSDEPLOYAGENTSERVICE` 去驗證 Remote Agent Service 是否正常運作。

![12.png](12.png)

至於 Manager Service 這邊，可以開啟 IIS Manager 的 `Management Service`。

![13.png](13.png)

確定這邊的 `Enable remote connections` 是勾選的，以及 Port 號正確，若不修改就是走預設的 8172 Port。

![14.png](14.png)

如果要使用非 Admin 權限佈署，可以開啟 `IIS Manager Permissions`。

![15.png](15.png)

新增指定的 User。

![16.png](16.png)

![17.png](17.png)

![18.png](18.png)

Link
----
* [Web Deploy 3.5 : The Official Microsoft IIS Site](https://www.iis.net/downloads/microsoft/web-deploy)