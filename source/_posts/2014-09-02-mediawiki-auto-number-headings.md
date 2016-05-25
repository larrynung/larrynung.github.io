---
layout: post
title: "MediaWiki - Auto-number headings"
date: 2014-09-02 23:35:00
comments: true
categories: [MediaWiki]
keywords: "MediaWiki"
description: "MediaWiki - Auto-number headings"
---

MediaWiki 在使用標頭時，預設是不會有自動編號的，這樣的呈現方式在瀏覽時我們會不易知道是哪個章節。當然你也可以自己在撰寫標頭時附上編號，但總是比較麻煩點，如果沒有太特殊的需求，我們是可以直接將 MediaWiki 的標頭自動編號功能給開啟。  

<!-- More -->

<br/>

要將自動編號功能給開啟，首先要先將 LocalSettings.php 檔案開啟。  

{% img /images/posts/MediaWikiAutoNumberHeadings/1.png %}

<br/>

找到 `$wgDefaultUserOptions['numberheadings']` 設定，將其值設定為 1。  

    $wgDefaultUserOptions['numberheadings'] = 1;

{% img /images/posts/MediaWikiAutoNumberHeadings/2.png %}

<br/>


這樣 MediaWiki 的標頭前面就會自動編號。  

{% img /images/posts/MediaWikiAutoNumberHeadings/3.png %}

<br/>

Link
----
* [Auto-number headings - MediaWiki](http://www.mediawiki.org/w/index.php?title=Auto-number_headings)
