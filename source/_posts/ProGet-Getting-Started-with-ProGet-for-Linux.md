---
title: ProGet - Getting Started with ProGet for Linux
date: 2017-09-08 23:26:07
tags: [ProGet]
---

要在 Linux 架設 ProGet，目前只有 Docker 的 Solution。  

<!-- More -->

<br/>


建立 Docker 容器的網路連結。  

    docker network create proget

{% asset_img 1.png %}

<br/>


建立 Postgres 資料庫容器供 ProGet 使用。  

    docker run -d -v /etc/localtime:/etc/localtime:ro -v /var/proget/db:/var/lib/postgresql/data --net=proget --name=proget-postgres --restart=unless-stopped postgres:9.5

{% asset_img 2.png %}

<br/>


建立 ProGet 容器。  

    docker run -d -v /etc/localtime:/etc/localtime:ro -v /var/proget/packages:/var/proget/packages -v /var/proget/extensions:/var/proget/extensions -p 80:80 --net=proget --name=proget --restart=unless-stopped inedo/proget:latest

{% asset_img 3.png %}

<br/>


ProGet 即可正常運作。  

{% asset_img 4.png %}

<br/>


若要停止服務，可用 docker stop 停止 proget 與 proget-postgres 容器。  

    docker stop proget proget-postgres 

{% asset_img 5.png %}

<br/>


若要啟動服務，可用 docker start 啟動 proget 與 proget-postgres 容器。  

    docker start proget proget-postgres 

{% asset_img 6.png %}

<br/>


要查閱 ProGet 運行的問題，可用 docker logs。  

    docker logs proget

<br/>


要更新 ProGet 的話，可將當前的 ProGet 容器停止，將當前的 ProGet 容器改名，然後重新拉取 ProGet 容器，將拉取的 ProGet 容器啟動，最後刪除掉之前的 ProGet 即可。    

    docker stop proget
    docker rename proget proget-old
    docker pull inedo/proget:latest
    docker run -d --volumes-from=proget-old -p 80:80 --net=proget --name=proget --restart=unless-stopped inedo/proget:latest
    docker rm proget-old

<br/>


Link
----
* [Getting Started with ProGet for Linux | Inedo](http://inedo.com/support/kb/1100/getting-started-with-proget-for-linux)
