---
title: Hexo - Deploy blog post
date: 2016-06-12 23:36:32
tags: Hexo
---

要發佈文章至遠端 repository，第一次使用之前，需要先安裝 Hexo 的 Deployer 套件。Hexo 支援多種 Deployer，這邊可視需要安裝。  

<!-- More -->

<br/>


像是筆者用的是 GitHub page 去 host 部落格，因此安裝的是 hexo-deployer-git。  

    npm install hexo-deployer-git --save

{% asset_img 1.png %}

<br/>


Deployer 套件安裝完後，要開啟部落格的設定檔設定 Deploy 的參數，像是 Deployer 的型態以及 repository 的位置等。  

{% asset_img 2.png %}

<br/>


設定完後我們就可以開始進行發佈的動作。  

<br/>


先產生發佈需要的靜態檔案。  

    hexo generate
    hexo g

<br/>


再用 hexo deploy 進行發佈即可。

    hexo deploy

<br/>

Link
---
* [Deployment | Hexo](https://hexo.io/docs/deployment.html)
