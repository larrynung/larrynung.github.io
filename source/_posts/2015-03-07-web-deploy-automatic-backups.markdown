---
layout: post
title: "Web Deploy - Automatic Backups"
date: 2015-03-07 12:37
comments: true
categories: [Web Deploy]
keywords: "Web Deploy, Backup"
description: "Web Deploy - Automatic Backups"
---

若想讓 Web Deploy 在 Deploy 時自動幫我們進行網站的備份，甚至是控管備份的數量，我們可以將 Web Deploy 的 Automatic Backups 功能啟用。  

<!-- More -->

<br/>


要啟用時我們需將 Server IIS 的 Configuration Editor 開啟，可以針對整台機器進行設定，或是針對 Site 進行設定，這邊視個人需求而定。    

{% img /images/posts/WebDeployAutoBackup/1.png %}

<br/>


Configuration Editor 開啟後，上方的 Section 記得切到 system.webServer/wdeploy/backup。接著將 enabled 與 turnedOn 設為 True，按下右側的 Apply 進行套用，即完成 Automatic Backups 功能開啟的動作。  

{% img /images/posts/WebDeployAutoBackup/2.png %}

<br/>


若有需要這邊我們也可以更改 backupPath 去設定備份的位置，或是更改 numberOfBackups 去設定備份保留的數量。  

<br/>


功能開啟後，只要透過 Web Deploy 進行佈署，Web Deploy 即會幫我們自動將 Application 備份。我們可以從 Web Deploy 的 Deploy 訊息看到該功能是否有成功的生效。   

{% img /images/posts/WebDeployAutoBackup/3.png %}

<br/>


若是在備份時失敗，Web Deploy 的 Deploy 訊息也會告知。  

{% img /images/posts/WebDeployAutoBackup/4.png %}

<br/>


備份的檔案會放置在我們所設定的備份位置，裡面也只是整個 Application 的壓縮以及一些還原用的設定。  

{% img /images/posts/WebDeployAutoBackup/5.png %}

<br/>


備份完後我們可以用 msdeploy 進行查閱、還原、刪除之類的動作。  

<br/>


像是要查閱某個 WebSite 下有哪些備份，我們可以用...    

    msdeploy.exe -verb:dump -source:backupManager=<siteName>

{% img /images/posts/WebDeployAutoBackup/6.png %}

<br/>


要還原至特定備份，我們可以用...

    msdeploy.exe -verb:sync -source:backupManager -dest:backupManager=<siteName>/<backupFileName>

{% img /images/posts/WebDeployAutoBackup/7.png %}

<br/>


要用最後的備份進行還原，我們可以用...

    msdeploy.exe -verb:sync -source:backupManager -dest:backupManager=<siteName>,useLatest=true

{% img /images/posts/WebDeployAutoBackup/8.png %}

<br/>


Link
----
* [Web Deploy Automatic Backups : The Official Microsoft IIS Site](http://www.iis.net/learn/publish/using-web-deploy/web-deploy-automatic-backups)
