---
title: migrate - MongoDB driver
date: 2019-09-02 11:24:21
tags: [migrate]
---

migrate 要對 MongoDB 進行資料庫的 Migration，Migration 檔案內要放置要給 MongoDB 用 db.runCommand 運行的命令，附檔名為 json。  

<!-- More -->

{% asset_img 1.png %}

</br>


{% asset_img 2.png %}

</br>


{% asset_img 3.png %}

</br>


{% asset_img 4.png %}

</br>


migrate 的資料庫這邊要參照下列格式設定。就可以透過 migrate 做資料庫的 Migration。

    mongodb://user:password@host:port/dbname?query

{% asset_img 5.png %}

</br>


運行 Migration 後資料庫內會多個 schema_migrations collection，用以存放 Migration 的資訊。

{% asset_img 6.png %}

</br>


Link
====
* [MongoDB](https://github.com/golang-migrate/migrate/tree/master/database/mongodb)
