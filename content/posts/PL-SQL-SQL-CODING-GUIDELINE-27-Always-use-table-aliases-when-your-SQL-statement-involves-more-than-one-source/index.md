---
title: ">-"
date: "2016-06-07 22:41:27"
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
---


條款二十七，當使用多個來源做搜尋時，總是使用資料表別名。  

<!-- More -->

<br/>


像是下面這樣，資料從兩個資料表來，如果不給資料表取別名我們會無法輕易識別資料是從哪個資料表來的。  

```c#
SELECT 
    a.pid ,a.name ,a.birthday ,b.country 
FROM person a JOIN country b ON (a.cid = b.cid) 
WHERE …
```
