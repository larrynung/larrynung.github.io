---
title: "MediaWiki - How to check MediaWiki's version"
date: "2014-12-27 23:47:00"
description: "MediaWiki - How to check MediaWiki's version"
tags: [MediaWiki]
---

有些時候我們會需要知道已安裝的 MediaWiki 版本，像是要安裝 MediaWiki 的套件前我們就會需要明確的知道是否能在其上正常運作。

要查閱安裝的 MediaWiki 版本，我們有三種方式。

一種是進到 Wiki 的 Version 頁面查閱(搜尋框輸入Special:Version)。

![1.png](/images/posts/CheckMediaWikiVersion/1.png)

或是透過網頁原始碼查閱。

![2.png](/images/posts/CheckMediaWikiVersion/2.png)

抑或是透過 DefaultSettings.php 檔的 $wgVersion 設定也可得知。

![3.png](/images/posts/CheckMediaWikiVersion/3.png)