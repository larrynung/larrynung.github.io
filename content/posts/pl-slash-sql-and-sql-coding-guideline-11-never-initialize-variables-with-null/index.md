---
title: "PL/SQL & SQL CODING GUIDELINE 11 - Never initialize variables with NULL"
date: "2015-11-25 05:44:00"
description: "條款十一是說不要將變數初始為 NULL。 因為預設就是初始為 Null。"
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
---

條款十一是說不要將變數初始為 NULL。

```psql
DECLARE
v_str VARCHAR2(30) := null;
BEGIN
...
END;
```

因為預設就是初始為 Null。

```psql
DECLARE
v_str VARCHAR2(30);
BEGIN
...
END;
```