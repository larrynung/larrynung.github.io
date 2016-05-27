---
layout: post
title: "Windows Azure - Enable MediaWiki File Upload"
date: 2015-01-11 22:23:00
comments: true
categories: [Windows Azure, MediaWiki] 
keywords: "Azure, MediaWiki"
description: "Windows Azure - Enable MediaWiki File Upload"
---

使用 Azure 架設 MediaWiki，若要啟動檔案上傳的功能，我們需要在建立 MediaWiki 時，將 Enable MediaWiki File Uplad 以及 Use Windows Azure Storage As File Backend 設定開啟，並設定 Windows Azure Storage Account Name 以及 Windows Azure Storage Account Key。  

<!-- More -->>

{% img /images/posts/EnableAzureMediaWikiFileUplad/1.png %}


填寫 Windows Azure Storage Account Name 以及 Windows Azure Storage Account Key 的值時，可參閱儲存體的存取金鑰。  

{% img /images/posts/EnableAzureMediaWikiFileUplad/2.png %}


這樣建立出來的 MediaWiki 就會啟用 MediaWiki 的 WindowsAzureStorage Extension，可以看到建立好的 LocalSetting.php 內會自動設好相關的設定。

{% img /images/posts/EnableAzureMediaWikiFileUplad/3.png %}


建立出來的 MediaWiki 也可以正常的將檔案上傳上去。
