---
title: "MariaDB - List table constraints"
date: "2019-05-22 21:58:49"
description: "要查詢資料庫的 Constraints 可查閱 information_schema schema 的 table_constraints table。 Link List table check constraints in MariaDB database - MariaDB Query…"
tags: [MariaDB]
---

要查詢資料庫的 Constraints 可查閱 information_schema schema 的 table_constraints table。

```sql
select *
from information_schema.table_constraints
order by table_schema, table_name;
```

![1.png](1.png)

Link
----
* [List table check constraints in MariaDB database - MariaDB Query Toolbox](https://dataedo.com/kb/query/mariadb/list-table-check-constraints)