---
title: Docker - Remove all unused local volumes
date: 2019-04-18 15:11:43
tags: [Docker]
---

Docker 用久了本地可能會殘留許多的資料卷。  

<!-- More -->

<br/>


像是筆者電腦中就殘留了那麼多。    

    docker volume ls

{% asset_img 1.png %}

<br/>


這時可以透過 volume 的 prune 命令將本地沒在使用的資料卷給清除。  

    docker volume prune

{% asset_img 2.png %}

<br/>


這邊會顯示清出了多少的空間。  

{% asset_img 3.png %}

<br/>


再次查詢做個確認，應該會看到資料卷正常的被清掉。  

{% asset_img 4.png %}
