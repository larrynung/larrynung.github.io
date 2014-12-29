---
layout: post
title: "Windows Azure - MediaWiki in Azure"
date: 2014-12-29 12:22
comments: true
categories: [Windows Azure, MediaWiki]
keywords: "Windows Azure, MediaWiki"
description: "MediaWiki in Azure"
---

用 Azure 架設 MediaWiki，我們可以到 Azure 的入口網站，切換至網頁管理頁面。  

<!-- More -->

{% img /images/posts/MediaWikiInAzure/1.png %}

<br/>


按下左下角的新增按鈕。  

{% img /images/posts/MediaWikiInAzure/2.png %}

<br/>


然後從組件庫中建立我們要的服務。  

{% img /images/posts/MediaWikiInAzure/3.png %}

<br/>


也就是 MediaWiki 服務，選取後按下 Next 繼續。  

{% img /images/posts/MediaWikiInAzure/4.png %}

<br/>


接著要進行服務的細部設定，像是服務的網址、Wiki 的名稱、登入的帳密...等。設定完一樣按下 Next 繼續。    

{% img /images/posts/MediaWikiInAzure/5.png %}

<br/>


最後是設定 MySQL 資料庫。  

{% img /images/posts/MediaWikiInAzure/6.png %}

<br/>


到這邊設定告一段落，系統會開始進行服務的佈署。  

{% img /images/posts/MediaWikiInAzure/7.png %}

<br/>


佈署完成按下下方的瀏覽按鍵。  

{% img /images/posts/MediaWikiInAzure/8.png %}

<br/>


我們即可看到 MediaWiki 服務運行的結果，但因為是第一次使用，所以此時還未有 LocalSettings.php 設定檔，為此我們可以按下畫面中的連結產生預設的設定先。  

{% img /images/posts/MediaWikiInAzure/9.png %}

<br/>


按下後 MediaWiki 就可正常使用了，這邊直接用服務建立時所設定的帳密進行登入就可以了。  

{% img /images/posts/MediaWikiInAzure/10.png %}

<br/>


若還需進一步的修改與設定，我們可以使用 FTP 登入該 Azure 服務，修改裡面的 LocalSettings.php。  
