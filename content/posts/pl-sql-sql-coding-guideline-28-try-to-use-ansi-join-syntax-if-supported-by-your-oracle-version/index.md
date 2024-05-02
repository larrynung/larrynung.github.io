---
title: ">-"
date: "2016-06-07 23:58:35"
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
---


條款二十八，如果 Oracle 版本支援，請使用 ANSI-Join。  

<!-- More -->

<br/>


因為 ANSI-Join 使用上比較沒有那麼多限制，支援 outer join，且能將 join 條件與 query 條件分開。


使用上會像是下面這樣：  

```psql
SELECT 
    a.pid ,a.name ,a.birthday ,b.country 
FROM person a JOIN country b ON (a.cid = b.cid) 
WHERE …
```
