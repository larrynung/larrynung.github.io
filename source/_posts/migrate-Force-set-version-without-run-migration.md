---
title: migrate - Force set version without run migration
date: 2019-08-19 09:02:59
tags: [migrate]
---

migrate 的 force 命令可不運行 migration 就強制設定版本。  

<!-- More -->

</br>


像是筆者這邊有個沒套過 migration 的資料庫。

    migrate -source $source -database $database version

{% asset_img 1.png %}

</br>


筆者強制設定資料庫版本。  

    migrate -source $source -database $database force $version

{% asset_img 2.png %}

</br>


資料庫版本就會被強制設為指定的版本。  

    migrate -source $source -database $database version

{% asset_img 3.png %}
