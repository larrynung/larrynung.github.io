---
title: Hexo - Getting started
date: 2016-06-10 18:39:27
tags: Hexo
---

要使用 Hexo，我們需先安裝 Hexo 的命令列程式。  

<!-- More -->

    npm install hexo-cli -g

{% asset_img 1.png %}

<br/>


接著初始化部落格。  

    hexo init [Folder]

{% asset_img 2.png %}

<br/>


初始的動作會產生對應的目錄。  

{% asset_img 3.png %}

<br/>


並下載需要的檔案。

{% asset_img 4.png %}

<br/>
  

初始完後進到部落格目錄，還原 npm 套件，即可將之運行起來。 

    cd [Folder]
    npm install
    hexo server 

{% asset_img 5.png %}

<br/>


運行起來後，用瀏覽器瀏覽 http://localhost:4000 即可看到部落格運行起來的樣子。  

{% asset_img 6.png %}

<br/>


Link
---
* [Hexo](https://hexo.io/)
