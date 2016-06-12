---
title: Hexo - Getting started
date: 2016-06-10 18:39:27
tags: Hexo
---

要使用 Hexo，我們需先確定已有安裝 Git & Node.js。  

<!-- More -->

<br/>


接著安裝 Hexo 的命令列程式。  

    npm install hexo-cli -g

{% asset_img 1.png %}

<br/>


與初始化部落格。  

    hexo init [Folder]

{% asset_img 2.png %}

<br/>


初始的動作會產生對應的目錄，並下載需要的檔案。  

{% asset_img 3.png %}

<br/>


整個目錄結構會像下面這樣。_config.yml 是 Hexo 站台的設定檔，package.json 是 Node.js 的套件設定檔，scaffoids 目錄內存放的是部落格會用到的樣板，source 目錄內存放的是部落格文章等未經加工建立的來源擋，themes 目錄內放置的是部落格的主題。  

{% asset_img 4.png %}

<br/>


再來要開啟 _config.yml 設定部落格。  

{% asset_img 5.png %}

<br/>  


設定完後存擋。  

<br/>


進到部落格目錄，還原 npm 套件，即可將之運行起來。 

    cd [Folder]
    npm install
    hexo server 

{% asset_img 6.png %}

<br/>


運行起來後，用瀏覽器瀏覽 http://localhost:4000 即可看到部落格運行起來的樣子。  

{% asset_img 7.png %}

<br/>


Link
---
* [Hexo](https://hexo.io/)
