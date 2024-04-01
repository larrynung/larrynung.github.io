---
title: "Flyway - Migrates the schema to the latest version"
date: "2019-07-29 23:27:32"
tags: [Flyway]
---


Flyway 把所有的資料庫變更都稱為 Migration，套用資料庫變更的動作即為 Migrate。  

<!-- More -->

![1.png](1.png)

</br>


Migration 分為 Versioned、 Undo、 Repeatable 三種。  

</br>


Versioned Migration 是一般的 Migration，帶有版號，且只能運行一次。檔案格式如下:  

![2.png](2.png)

</br>


Undo Migration 是用來還原 Versioned Migration 用的 Migration。檔案格式如下:  

![3.png](3.png)

</br>


Repeatable Migration 是可重複運行的 Migration。檔案格式如下:  

![4.png](4.png)

</br>


這邊筆者實際放入個檔名為 V1__Create_person_table.sql 的 Versioned Migration 到 sql 目錄，表示第一版變更，變更內容為 Create person table。  

![5.png](5.png)

</br>


Migration 內容如下，只是簡單的建立一個名為 PERSON 的資料表。  

```sql
create table PERSON (
    ID int not null,
    NAME varchar(100) not null
);
```

![6.png](6.png)

</br>


調用 Flyway migrate 命令套用資料庫的變更。  

    flyway migrate

![7.png](7.png)

</br>


連進資料庫可看到確實套上了資料庫的變更，連帶多了一張 flyway_schema_history 的資料表，裡面存放 Flyway 套用變更的紀錄。  

![8.png](8.png)

</br>


Migrate 時會依這紀錄檢查是否需要套用資料庫的變更。  

![9.png](9.png)
