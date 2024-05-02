---
title: "PL/SQL  SQL CODING GUIDELINE 49 - Avoid use of unreferenced FOR loop indexes"
date: "2017-06-12 23:20:04"
tags: [PL/SQL and SQL Coding Guidelines]
---


條款四十九，避免未使用的 FOR loop 索引。  

<!-- More -->

<br/>


像是下面這樣的程式使用了 numeric FOR loop，卻未使用 FOR loop 的索引，導致程式碼變得更為複雜沒有效率。  

```psql
DECLARE
    ...
BEGIN
    l_row := co_lower_bound;
    l_value := co_first_value;
    <<for_loop>>
    FOR i IN co_lower_bound .. co_upper_bound LOOP
        sys.dbms_output.put_line(l_row || co_delimiter || l_value); 
        l_row := l_row + co_row_incr;
        l_value := l_value + co_value_incr;
   END LOOP for_loop;
END;
```

<br/>



比較好的作法是要看看是否能透過索引撰寫出更適合的程式，如果不行則要反思這邊使用 numeric FOR loop 是否合適。  

```psql
DECLARE
    ...
BEGIN
    <<for_loop>>
    FOR i IN co_lower_bound .. co_upper_bound 
    LOOP
        sys.dbms_output.put_line(i || co_delimiter || to_char(co_first_value + i * co_value_incr));
    END LOOP for_loop;
END;
```
