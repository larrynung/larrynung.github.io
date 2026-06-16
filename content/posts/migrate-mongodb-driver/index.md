---
title: "migrate - MongoDB driver"
date: "2019-09-02 11:24:21"
description: "migrate 要對 MongoDB 進行資料庫的 Migration，Migration 檔案內要放置要給 MongoDB 用 db.runCommand 運行的命令，附檔名為 json。 migrate 的資料庫這邊要參照下列格式設定。就可以透過 migrate 做資料庫的 Migration。"
tags: [migrate]
---

migrate 要對 MongoDB 進行資料庫的 Migration，Migration 檔案內要放置要給 MongoDB 用 db.runCommand 運行的命令，附檔名為 json。

![1.png](1.png)

![2.png](2.png)

![3.png](3.png)

![4.png](4.png)

migrate 的資料庫這邊要參照下列格式設定。就可以透過 migrate 做資料庫的 Migration。

mongodb://user:password@host:port/dbname?query

![5.png](5.png)

運行 Migration 後資料庫內會多個 schema_migrations collection，用以存放 Migration 的資訊。

![6.png](6.png)

Link
====
* [MongoDB](https://github.com/golang-migrate/migrate/tree/master/database/mongodb)