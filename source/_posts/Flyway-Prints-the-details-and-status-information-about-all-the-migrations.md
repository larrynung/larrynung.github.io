---
title: Flyway - Prints the details and status information about all the migrations
date: 2019-07-30 21:06:26
tags: [Flyway]
---

要透過 Flyway 查閱 Migration 的資訊或是運行狀態，可透過 Flyway 的 info 命令。  

<!-- More -->

    flyway info


</br>


Flyway info 會將資料庫內的 Migration 資訊與本地的 Migration 整理後呈現。  

{% asset_img 1.png %}

</br>


像是這邊筆者有一個空的資料庫，本地放了兩個 Migration 檔，運行 Flyway info 後會看到兩個在 Pending 狀態的 Migration。  

    flyway info

{% asset_img 2.png %}

</br>


將 Migration migrate 進資料庫。  

    flyway migrate

{% asset_img 3.png %}

</br>


再次調用 Flyway info，可看到兩個 Migration 都切到了 Success 狀態。  

    flyway info

{% asset_img 4.png %}
