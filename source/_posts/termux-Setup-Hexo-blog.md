---
title: Termux - Setup Hexo blog
date: 2018-10-16 08:17:03
tags: [Termux, Hexo]
---

在 Termux 使用 Hexo 並沒什麼特別之處。  

<!-- more -->

</br>


一樣是要先將 Hexo CLI 安裝到全域。  

    npm install hexo-cli -g

{% asset_img 1.jpg %}

</br>


接著初始化 Blog。  

    hexo init <Folder>

{% asset_img 2.jpg %}

</br>


進入剛初始化產出的目錄

{% asset_img 3.jpg %}

</br>


運行 Hexo 服務。  

    hexo s

{% asset_img 4.jpg %}

</br>


訪問 http://127.0.0.1:4000 即可看到 Blog 運行的結果。  

{% asset_img 5.jpg %}
