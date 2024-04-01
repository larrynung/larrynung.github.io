---
title: ">-"
date: "2017-06-06 12:13:21"
tags: [PL/SQL and SQL Coding Guidelines]
---


條款四十五，避免使用 EXIT 去跳離迴圈，除非使用的是 basic loop。  

<!-- More -->

<br/>


像是下面這樣的程式，使用了 EXIT 去跳離迴圈，但是非 basic loop 都有迴圈的邊界條件可以設定，可以做到一樣的事情，所以這樣的寫法並不是很好。  

```psql
...
i := co_min_value;
<<while_loop>>
WHILE (i <= co_max_value)
LOOP
  i := i + co_increment;
  EXIT while_loop WHEN i > co_max_value;
END LOOP while_loop;

<<for_loop>>
FOR i IN co_min_value..co_max_value
LOOP
  ...
  EXIT for_loop WHEN i = co_max_value;
END LOOP for_loop;

<<process_employees>>
FOR r_employee IN (SELECT last_name FROM employees)
LOOP
  ...
  EXIT process_employees;
END LOOP process_employees;
...
```

<br/>


若使用非 basic loop，建議使用邊界條件來跳離迴圈。而 basic loop 因為沒有邊界條件的設定，因此也只能使用 EXIT 來跳離迴圈。  

```psql
<<while_loop>>
WHILE (i <= co_max_value)
LOOP
  i := i + co_increment;
END LOOP while_loop;

<<basic_loop>>
LOOP
  EXIT basic_loop;
END LOOP basic_loop;

<<for_loop>>
FOR i IN co_min_value..co_max_value
LOOP
  ...
END LOOP for_loop;

<<process_employees>>
FOR r_employee IN (SELECT last_name FROM employees)
LOOP
  ...
END LOOP process_employees;
```
