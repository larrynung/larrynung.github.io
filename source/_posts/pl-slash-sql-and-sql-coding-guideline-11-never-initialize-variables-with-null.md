---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 11 - Never initialize variables with NULL"
date: 2015-11-25 05:44:00
comments: true
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
description: "PL/SQL &amp; SQL CODING GUIDELINE 11 - Never initialize variables with NULL"
---

條款十一是說不要將變數初始為 NULL。  

<!-- More -->

```psql
DECLARE 
	v_str VARCHAR2(30) := null; 
BEGIN 
	... 
END;
```

<br/>


因為預設就是初始為 Null。  

```psql
DECLARE 
	v_str VARCHAR2(30); 
BEGIN 
	... 
END;
```
