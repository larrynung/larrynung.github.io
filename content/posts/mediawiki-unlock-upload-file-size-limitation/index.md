---
title: "MediaWiki - Unlock upload file size limitation"
date: "2014-06-15 00:07:00"
description: "MediaWiki - Unlock upload file size limitation"
tags: [MediaWiki ]
---


MediaWiki 在檔案上傳這邊預設是有 2MB 的限制在。

<!-- More -->

{% img /images/posts/MediaWikiUnlickFileLimit/1.png %}

<br/>


若要對此設定值做些調整，我們可以開啟 `Php.ini`。

{% img /images/posts/MediaWikiUnlickFileLimit/2.png %}

<br/>


調整 `upload_max_filesize` 設定值。  

{% img /images/posts/MediaWikiUnlickFileLimit/3.png %}

<br/>


以及調整 `post_max_size` 設定值。 

{% img /images/posts/MediaWikiUnlickFileLimit/4.png %}

<br/>


調整完存檔退出，檔案上傳這邊就會生效。

{% img /images/posts/MediaWikiUnlickFileLimit/5.png %}

<br/>
