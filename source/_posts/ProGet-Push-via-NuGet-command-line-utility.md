---
title: ProGet - Push via NuGet command line utility
date: 2017-09-11 22:12:15
tags: [ProGet]
---

要透過 NuGet 命令上傳 NuGet 套件到 ProGet 的 NuGet feed，可在 ProGet 的 NuGet feed 頁面按下 Add Package 按鈕。  

<!-- More -->

{% asset_img 1.png %}

<br/>


點選 Push via NuGet Command Line Utility。  

{% asset_img 2.png %}

<br/>


這邊會告知怎樣使用 NuGet 命令上傳 NuGet 套件。  

{% asset_img 3.png %}

<br/>


參照說明使用 NuGet 命令上傳指定 NuGet 套件。  

    nuget push [Package] [APIKey] -source [FeedUrl]

{% asset_img 4.png %}

<br/>


若未設定 API key，可用 [UserName]:[Password] 替代。  

<br/>


命令調用完選取的套件即會上傳到 ProGet 的 feed。  

{% asset_img 5.png %}

<br/>



{% asset_img 6.png %}

<br/>
