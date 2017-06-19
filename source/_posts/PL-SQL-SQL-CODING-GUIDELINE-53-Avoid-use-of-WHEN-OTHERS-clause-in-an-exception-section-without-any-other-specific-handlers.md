---
title: >-
  PL/SQL & SQL CODING GUIDELINE 53 - Avoid use of WHEN OTHERS clause in an
  exception section without any other specific handlers
date: 2017-06-18 23:33:16
tags: [PL/SQL and SQL Coding Guidelines]
---

條款五十三，避免單獨使用 WHEN OTHERS 去處理例外。  

<!-- More -->

<br/>


像是下面這樣的程式，使用 WHEN OTHERS 搭配 IF 條件式與 SQLCODE 去處理例外，就是不建議的作法。  

```psql
...
EXCEPTION 
  WHEN OTHERS 
  THEN 
    IF SQLCODE = -1 
    THEN 
      update_instead (...); 
    ELSE 
      err.log; 
      RAISE; 
    END IF;
...
```

<br/>



如果明確使用例外的名稱去處理例外，可以免去不必要的 IF 判斷，及 SQLCODE 的使用。  

```psql
...
EXCEPTION 
  WHEN DUP_VAL_ON_INDEX 
  THEN 
    update_instead (...); 
  WHEN OTHERS 
  THEN 
    err.log; 
    RAISE;
...
```


