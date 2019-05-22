---
title: MariaDB - List table constraints
date: 2019-05-22 21:58:49
tags: [MariaDB]
---

要查詢資料庫的 Constraints 可查閱 information_schema schema 的 table_constraints table。  

<!-- More -->

```sql
select *
from information_schema.table_constraints
order by table_schema, table_name;
```

{% asset_img 1.png %}

</br>


Link
----
* [List table check constraints in MariaDB database - MariaDB Query Toolbox](https://dataedo.com/kb/query/mariadb/list-table-check-constraints)
