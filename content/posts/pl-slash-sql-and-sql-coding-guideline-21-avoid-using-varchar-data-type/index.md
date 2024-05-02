---
title: "PL/SQL amp; SQL CODING GUIDELINE 21 - Avoid using VARCHAR data type"
date: "2015-12-05 20:10:00"
description: "PL/SQL &amp; SQL CODING GUIDELINE 21 - Avoid using VARCHAR data type"
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
---


條款二十一，避免使用 Varchar 型態。  

<!-- More -->

<br/>


Varchar 型態在工業標準上是可以儲存空字串的，但在 Oracle 這邊並未遵循這樣的標準，當將空字串存放至 Varchar 型態，Oracle 這邊會將空字串變為 null 值，就跟 Varchar2 型態是一樣的，但難保哪天會改回遵循工業標準。  

```psql
DECLARE 
    v_str varchar(4000);
BEGIN 
    …
END;
```

<Br/>


因此在 Oracle 這邊建議不要使用 Varchar 型態，建議使用 Varchar2 型態。

```psql
DECLARE 
    v_str varchar2(4000); 
BEGIN 
    …
END;
```
