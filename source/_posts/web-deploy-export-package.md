---
layout: post
title: "Web Deploy - Export package"
date: 2015-07-08 23:13:00
comments: true
categories: [Web Deploy]
keywords: "Web Deploy, Export"
description: "Web Deploy - Export package"
---

要將 IIS 網站 Application 或 Server 匯出，我們可以透過 Web Deploy 的匯出功能來做。先確定 Server 有安裝 Web Deploy，安裝後在 IIS 的 Application 或是 Server 節點上按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中應該會多出 Deploy 的功能選項。這邊點選 [Deploy | Export Server Package...] 選單選項。  

<!-- More -->


{% img /images/posts/ExportWebDeployPackage/1.png %}

<br/>


點選後會彈出匯出對話框，可選取要匯出的內容。確定後點選 `Next` 按鈕繼續。  

{% img /images/posts/ExportWebDeployPackage/2.png %}

<br/>


接著要設定參數的部份，設定完後一樣按下 `Next` 按鈕繼續。  

{% img /images/posts/ExportWebDeployPackage/3.png %}

<br/>


最後這邊要選取匯出的檔案位置。  

{% img /images/posts/ExportWebDeployPackage/4.png %}

<br/>


{% img /images/posts/ExportWebDeployPackage/5.png %}

<br/>


選取完按下 `Next` 按鈕進行匯出。  

{% img /images/posts/ExportWebDeployPackage/6.png %}

<br/>


匯出完成會帶出 Summary 資訊。  

{% img /images/posts/ExportWebDeployPackage/7.png %}

<br/>


Link
----
* [Export a Package through IIS Manager : The Official Microsoft IIS Site](http://www.iis.net/learn/publish/using-web-deploy/export-a-package-through-iis-manager)
