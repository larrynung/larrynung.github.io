---
title: >-
  PL/SQL & SQL CODING GUIDELINE 52 - Never assign predefined exception names to
  user defined exceptions
date: 2017-06-17 21:00:16
tags: [PL/SQL and SQL Coding Guidelines]
---

條款五十二，不要使用自定義錯誤去重新定義 Oracle 預先定義的錯誤。  

<!-- More -->

<br/>


像是下面這樣的程式，使用自定義錯誤重新定義了 no_data_found 錯誤，就是不建議的作法。  

```sql
DECLARE 
  no_data_found EXCEPTION; 
  …
BEGIN 
  ... 
EXCEPTION 
  WHEN no_data_found 
  THEN 
    sys.dbms_output.put_line(co_no_data_found); 
END;
```

<br/>


比較好的作法應該是反思是否需要重新定義 Oracle 預先定義的錯誤、是否應該定義的是不同的錯誤。  

```sql
DECLARE 
  empty_value EXCEPTION; 
  ... 
BEGIN 
  ... 
EXCEPTION 
  WHEN empty_value 
  THEN 
    sys.dbms_output.put_line(co_empty_value); 
  WHEN no_data_found 
  THEN 
    sys.dbms_output.put_line(co_no_data_found); 
END;
```
