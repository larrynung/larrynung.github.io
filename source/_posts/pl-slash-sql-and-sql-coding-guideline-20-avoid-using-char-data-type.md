---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 20 - Avoid using CHAR data type"
date: 2015-12-05 19:35:00
comments: true
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
description: "PL/SQL &amp; SQL CODING GUIDELINE 20 - Avoid using CHAR data type"
---

條款二十，避免使用 Char。  

<!-- More -->

<br/>


Oracle 的 Char 型態在宣告時需指定大小，宣告多大就佔多大。像是下面這邊筆者宣告了 4000 的 char，則該變數即佔了 4000，儘管這邊只賦予了短短的幾個字元進去。  

```psql
DECLARE 
    v_str char(4000) := 'test'; 
BEGIN 
    DBMS_OUTPUT.PUT_LINE(Length(v_str)); 
END;
```

<br/>



取而代之的是應該改用 varchar2 型態。  

```psql
DECLARE 
    v_str varchar2(4000) := 'test'; 
BEGIN 
    DBMS_OUTPUT.PUT_LINE(Length(v_str)); 
END;
```
