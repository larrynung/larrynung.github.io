---
title: "Flyway - Repairs the schema history table"
date: "2019-08-01 21:31:10"
description: "Flyway 的 Repair 功能可用來修復 Flyway 存放在資料庫內的資料。 像是 Migrate 發生錯誤，可用來清楚錯誤狀態。或是重新套用 Migration，去修復 Migration type/description/checkchecksum。"
tags: [Flyway]
---

Flyway 的 Repair 功能可用來修復 Flyway 存放在資料庫內的資料。

![1.png](1.png)

像是 Migrate 發生錯誤，可用來清楚錯誤狀態。或是重新套用 Migration，去修復 Migration type/description/checkchecksum。

像是這邊筆者的資料庫狀態如下...

![2.png](2.png)

因為沒有造資料表所以塞資料的 Migration migrate 時會出錯。

![3.png](3.png)

這時資料庫內的 Migration 的狀態會是 Failed。

![4.png](4.png)

這時使用 Repair 功能...

flyway repair

![5.png](5.png)

資料庫內的 Migration 會回到 Pending 狀態。

![6.png](6.png)