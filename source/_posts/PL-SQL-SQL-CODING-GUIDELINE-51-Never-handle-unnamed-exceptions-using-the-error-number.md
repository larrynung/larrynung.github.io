---
title: >-
  PL/SQL & SQL CODING GUIDELINE 51 - Never handle unnamed exceptions using the
  error number
date: 2017-06-16 00:03:38
tags: [PL/SQL and SQL Coding Guidelines]
---

條款五十一，不要使用 Error Number 去處理 Unnamed Exceptions。  

<!-- More -->

</br>


像是下面這樣的程式，直接使用 Error Number -2291 去處理 Unnamed Exception 就不是建議的作法。  

```sql
BEGIN 
  ... 
EXCEPTION 
  WHEN OTHERS 
  THEN 
    IF SQLCODE = -2291 
    THEN 
      ... 
    END IF; 
END;
```

<br/>


比較好的作法是透過 pragma exception_init 將未命名的內部錯誤做個命名，然後直接用這個命名去攔截對應的錯誤做對應的處理。

```sql
DECLARE 
  e_parent_missing EXCEPTION; 
  PRAGMA EXCEPTION_INIT(e_parent_missing,-2291); 
  ... 
BEGIN 
  ... 
EXCEPTION 
  WHEN e_parent_missing 
  THEN 
    ... 
END;
```
