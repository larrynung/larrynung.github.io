---
title: Gitea - Install with docker
date: 2017-09-20 22:39:47
tags: [Gitea, Docker]
---

透過 Docker 使用 Gitea，可用 docker pull 將 Gitea 容器拉回。  

<!-- More -->

    docker pull gitea/gitea:latest

{% asset_img 1.png %}

<br/>


然後建立一個目錄用以存放資料。  

{% asset_img 2.png %}

<br/>


使用 docker run 啟動 Gitea 容器，將剛建立的目錄掛載為資料卷。  

    docker run -d --name=gitea -p 10022:22 -p 80:3000 -v /gitea:/data gitea/gitea:latest

{% asset_img 3.png %}

<br/>


即可使用 Gitea 服務。  

{% asset_img 4.png %}

<br/>


Link
----
* [Docker 安裝 - Docs](https://docs.gitea.io/zh-tw/install-with-docker/)
