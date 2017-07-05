---
title: PL/SQL & SQL CODING GUIDELINE 57 - Avoid using Oracle’s predefined exceptions
date: 2017-07-05 13:18:58
tags: [PL/SQL and SQL Coding Guidelines]
---

條款五十七，避免使用 Oracle 預先定義好的例外。

<!-- More -->

<br/>


像是下面這段程式，在程式中主動拋出了 Oracle 預先定義好的例外就不是建議的做法。  

```plsql
BEGIN 
  RAISE NO_DATA_FOUND; 
END;
```

<br/>


應該要避免直接使用 Oracle 預先定義好的例外。  

```plsql
DECLARE 
  my_exception EXCEPTION; 
BEGIN 
  RAISE my_exception; 
END;
```