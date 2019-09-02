---
title: migrate - MySQL/MariaDB driver
date: 2019-09-02 08:45:50
tags: [migrate]
---

migrate 要對 MySQL/MariaDB 進行資料庫的 Migration，migrate 的資料庫這邊要參照下列格式設定。  

<!-- More -->

    mysql://user:password@tcp(host:port)/dbname?query


</br>


Migration 檔案用 SQL 語法下去撰寫。  

{% asset_img 1.png %}

</br>


{% asset_img 2.png %}

</br>


{% asset_img 3.png %}

</br>


{% asset_img 4.png %}

</br>


就可以透過 migrate 做資料庫的 Migration。  

{% asset_img 5.png %}

</br>


運行 Migration 後資料庫內會多個 schema_migrations 資料表，用以存放 Migration 的資訊。  

{% asset_img 6.png %}

</br>


Link
====
* [MySQL](https://github.com/golang-migrate/migrate/tree/master/database/mysql)
