---
title: PL/SQL & SQL CODING GUIDELINE 36 - Try to use CASE rather than DECODE
date: 2016-08-27 23:34:16
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
---

條款三十六，嘗試使用 CASE 而不要用 DECODE。  

<!-- More -->

<br/>


用 DECODE 的可讀性較低，不易閱讀。  

```psql
BEGIN 
    SELECT DECODE(dummy, 'A', 1 
        , 'B', 2 
        , 'C', 3 
        , 'D', 4  
        , 'E', 5
         , 'F', 6 
        , 7) 
    INTO l_result 
    FROM dual; 
...
```

<br/>


改用 CASE 撰寫雖然程式變多，但閱讀起來相對會比較清楚。  

```psql
BEGIN 
    l_result := CASE dummy 
        WHEN 'A' THEN 1 
        WHEN 'B' THEN 2 
        WHEN 'C' THEN 3 
        WHEN 'D' THEN 4 
        WHEN 'E' THEN 5 
        WHEN 'F' THEN 6 
        ELSE 7 
    END; 
...
```
