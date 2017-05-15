---
title: >-
  PL/SQL & SQL CODING GUIDELINE 31 - Always use %NOTFOUND instead of NOT %FOUND
  to check whether a cursor was successful
date: 2016-08-07 23:54:50
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
---

條款三十一，Always use %NOTFOUND instead of NOT %FOUND to check whether a cursor was successful。  

<!-- More -->

<br/>


不要用 Not %FOUND 去撰寫判斷邏輯。  
```sql
LOOP 
    FETCH c_employees INTO r_employee; 
    EXIT WHEN NOT c_employees%FOUND; 
    ... 
END LOOP;
```

<br/>


取而代之的是要用 %NOTFOUND 去撰寫判斷邏輯。  
```sql
LOOP 
    FETCH c_employees INTO r_employee; 
    EXIT WHEN c_employees%NOTFOUND; 
    ... 
END LOOP;
```

<br/>


這樣可讀性會比較好。  
