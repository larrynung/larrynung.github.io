---
title: "PL/SQL amp; SQL CODING GUIDELINE 10 - Try to use subtypes for constructs used often in your application"
date: "2015-11-24 05:33:00"
description: "PL/SQL &amp; SQL CODING GUIDELINE 9 - Try to use subtypes for constructs used often in your application"
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
---


條款十是在說如果有些常用的型態使用，建議將它設成 SubType，像是下面這邊 VARCHAR2(4000) 程式中如果常用的話，就可以將它設成 SubType。  

<!-- More -->

<br/>


```psql
DECLARE 
	v_str VARCHAR2(4000); 
BEGIN 
	… 
END;
```

<br/>


這邊將它設成名為 STRING_MAX 的 SubType，後續可直接拿來宣告使用。  

```psql
CREATE OR REPLACE PACKAGE PKG_SUBTYPE 
AS 
	SUBTYPE STRING_MAX IS VARCHAR2(4000); 
END PKG_SUBTYPE; 

DECLARE 
	v_str PKG_SUBTYPE.STRING_MAX; 
BEGIN 
	... 
END;
```
