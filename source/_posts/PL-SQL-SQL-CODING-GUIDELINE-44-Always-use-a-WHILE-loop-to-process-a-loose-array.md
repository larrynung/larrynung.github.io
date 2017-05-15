---
title: >-
  PL/SQL & SQL CODING GUIDELINE 44 - Always use a WHILE loop to process a loose
  array
date: 2017-05-03 13:50:12
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
---

條款四十四，總是使用 WHILE loop 去處理 loose array。  

<!-- More -->

<br/>


像是下面這樣的程式用 FOR loop 去遍巡處理 loose array，這不是被建議使用的寫法，雖然大部分的狀況下可以正常運行，但是當 loose array 的內容被刪除時，這樣的處理會因為 null 元素而運行錯誤。  

```psql
DECLARE 
  ...
  l_index PLS_INTEGER; 
BEGIN 
  ...
  IF t_employees IS NOT NULL THEN
    <<process_employees>>
    FOR i IN 1..t_employees.COUNT()
    LOOP
      ...
    END LOOP process_employees;
  END IF;
END;
```

<br/>


建議使用 WHILE loop 遍巡處理 loose array，才不會因為 Null 元素導致錯誤。  

```psql
DECLARE 
  ...
  l_index PLS_INTEGER; 
BEGIN 
  l_index := t_employees.FIRST(); 

  <<process_employees>> 
  WHILE l_index IS NOT NULL 
  LOOP 
    ...
    l_index := t_employees.NEXT(l_index); 
  END LOOP process_employees; 
END;
```