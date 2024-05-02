---
title: "migrate - MySQL/MariaDB driver"
date: "2019-09-02 08:45:50"
tags: [migrate]
---


migrate 要對 MySQL/MariaDB 進行資料庫的 Migration，migrate 的資料庫這邊要參照下列格式設定。  

<!-- More -->

    mysql://user:password@tcp(host:port)/dbname?query


</br>


Migration 檔案用 SQL 語法下去撰寫。  

![1.png](1.png)

</br>


![2.png](2.png)

</br>


![3.png](3.png)

</br>


![4.png](4.png)

</br>


就可以透過 migrate 做資料庫的 Migration。  

![5.png](5.png)

</br>


運行 Migration 後資料庫內會多個 schema_migrations 資料表，用以存放 Migration 的資訊。  

![6.png](6.png)

</br>


schema_migrations 資料表內只會有一筆紀錄，只會有 version 與 dirty 資訊，沒有 Migration 的版本紀錄，也沒有 CRC 檢查碼驗證。  

![7.png](7.png)

</br>


Link
====
* [MySQL](https://github.com/golang-migrate/migrate/tree/master/database/mysql)
