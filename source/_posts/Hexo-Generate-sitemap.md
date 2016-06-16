---
title: Hexo - Generate sitemap
date: 2016-06-16 22:02:19
tags: Hexo
---

要為 Hexo 部落格放置 Sitemap 檔，可以安裝 [hexo-generator-sitemap](https://github.com/hexojs/hexo-generator-sitemap) 套件。  

<!-- More -->

    npm install hexo-generator-sitemap --save

{% asset_img 1.png %}

<br/>


開啟 Hexo 設定檔，設定 sitemap 檔案。  

    sitemap:
        path: sitemap.xml

{% asset_img 2.png %}

<br/>


當建立靜態檔案就會產生指定的 sitemap 檔案。

{% asset_img 3.png %}

<br/>


Link
---
* [hexojs/hexo-generator-sitemap: Sitemap generator for Hexo.](https://github.com/hexojs/hexo-generator-sitemap)
