---
title: ">-"
date: "2017-04-21 13:25:51"
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
---


條款四十三，遍巡 dense array 時，建議使用 1 當做 lower boundary，使用 COUNT() 當做 upper boundary。  

<!-- More -->

<br/>


像是下面這樣的程式，使用了 FIRST() 與 LAST() 做為遍巡走訪的條件，dense array 不為空時可以正常運作，但當 dense array 為空時則會發生錯誤。  

```psql
DECLARE 
  t_employees t_employee_type := t_employee_type(); 
BEGIN 
  <<process_employees>> 
  FOR i IN t_employees.FIRST()..t_employees.LAST()
  LOOP
   … 
  END LOOP process_employees; 
END;
```

<br/>


簡單的解決方式可以加判斷 dense array 是否為空。  

```psql
DECLARE 
  t_employees t_employee_type := t_employee_type(); 
BEGIN 
  <<process_employees>> 
  IF t_employees IS NOT EMPTY 
  THEN 
    FOR i IN t_employees.FIRST()..t_employees.LAST() 
    LOOP 
      … 
    END LOOP process_employees; 
  END IF; 
END;
```

<br/>


但建議的方式是改以 1 與 COUNT() 做為遍巡走訪的條件。  

```psql
DECLARE 
  t_employees t_employee_type := t_employee_type(); 
BEGIN 
  <<process_employees>> 
  FOR i IN 1..t_employees.COUNT() 
  LOOP 
    … 
  END LOOP process_employees; 
END;
```

<br/>
