---
title: Hexo - Setup robots.txt
date: 2016-07-18 23:43:41
tags: Hexo
---

要為 Hexo 部落格加上 robots.txt，我們可以安裝 hexo-generator-robotstxt 套件。  

<!-- More -->

    npm install hexo-generator-robotstxt --save

{% asset_img 1.png %}

<br/>


安裝完後開啟站台設定檔，設定啟用 hexo-generator-robotstxt plugins。   

{% asset_img 2.png %}

<br/>


然後加入 robots.txt 的設定。  

{% asset_img 3.png %}

<br/>


設定完後存擋，接著產生靜態檔案，就可以看到 robots.txt 會順帶被產生出來。  

{% asset_img 4.png %}

<br/>


{% asset_img 5.png %}

<br/>


Link
----
* [GitHub - leecrossley/hexo-generator-robotstxt: Basic robots.txt generator plugin for Hexo](https://github.com/leecrossley/hexo-generator-robotstxt)
