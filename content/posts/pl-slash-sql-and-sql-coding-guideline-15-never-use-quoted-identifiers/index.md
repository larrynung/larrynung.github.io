---
title: "PL/SQL amp; SQL CODING GUIDELINE 15 - Never use quoted identifiers"
date: "2015-12-05 18:42:00"
description: "PL/SQL &amp; SQL CODING GUIDELINE 15 - Never use quoted identifiers"
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
---


條款十五是說在變數宣告時，變數的名稱不要加上雙引號。  

<!-- More -->

<br/>


像是下面這樣，宣告的變數加上雙引號是合法的。  

```psql
DECLARE 
	"v_str" VARCHAR2(30) ; 
BEGIN 
	…
END main;
```

<br/>


但不建議這樣宣告，建議還是不要加上雙引號。  

```psql
DECLARE 
	v_str VARCHAR2(30) ; 
BEGIN 
	…
END main;
```
