---
layout: post
title: "MediaWiki - Create wiki page"
date: 2014-02-22 21:42:00
comments: true
categories: [MediaWiki] 
keywords: "MediaWiki"
description: "MediaWiki - Create wiki page"
---

MediaWiki 要建立 Wiki Page，大致來說有下列幾種方式:  

<!-- More -->

* 透過網址列去建立  
* 透過連結 Wiki Page 的方式建立  
* 透過搜尋框搜尋後建立  

這邊分別簡單的帶過...   

<br/>

透過網址列去建立
----------------

使用這種方式去建立 Wiki Page，需要帶入特定格式的網址至網址列。 

網址格式會像下面這樣:  

    http://[Wiki url]/index.php?title=[Title]&action=edit

<br/>

將特定的網址帶入  

{% img /images/posts/CreateMediaWikiPage/1.png %}

<br/>

就可以建立出對應的 Wiki Page。 

{% img /images/posts/CreateMediaWikiPage/2.png %}

<br/>

透過連結 Wiki Page 的方式建立
-----------------------------

要建立一個 Wiki Page，通常是因為有連結的需求。可能是側邊欄，也有可能是其它 Wiki Page。無論是哪種，我們都會透過語法將 Wiki Page 做個連結。 

連結後回頭看一下撰寫的 Wiki Page，這時將滑鼠移上去，會很明顯的看到該連結頁面不存在。 

{% img /images/posts/CreateMediaWikiPage/3.png %}

<br/>

點擊連結即可建立對應的 Wiki Page。 

<br/>

透過搜尋框搜尋後建立
--------------------

這邊需先透過搜尋框搜尋欲建立的 Wiki Page 是否已經存在。 

{% img /images/posts/CreateMediaWikiPage/4.png %}

<br/>

若不存在， MediaWiki 會在這邊告知搜尋的 Wiki Page 不存在，同時會有個建立頁面的快速連結，點擊下去即可建立指定的 Wiki Page。

{% img /images/posts/CreateMediaWikiPage/5.png %}

<br/>

Link
-----
* [在mediawiki中創建新頁面- WordPress 中文文檔](http://codex.wordpress.org.cn/%E5%9C%A8mediawiki%E4%B8%AD%E5%88%9B%E5%BB%BA%E6%96%B0%E9%A1%B5%E9%9D%A2)

