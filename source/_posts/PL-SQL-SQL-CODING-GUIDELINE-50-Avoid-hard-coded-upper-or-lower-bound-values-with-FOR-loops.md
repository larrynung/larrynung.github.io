---
title: >-
  PL/SQL & SQL CODING GUIDELINE 50 - Avoid hard-coded upper or lower bound
  values with FOR loops
date: 2017-06-13 23:15:20
tags: [PL/SQL and SQL Coding Guidelines]
---

條款五十，避免 hard-codeed FOR loop 的上下邊界值。  

<!-- More -->

<br/>


像是下面這段程式 hard-coded 了 FOR loop 的上下邊界值，這樣的撰寫預期上下邊界值是不會被變動的，且後續再看這段程式可能也會不理解為何上下邊界值會帶這樣的值，程式的維護性上會比較差。  

```sql
BEGIN
    <<for_loop>>
    FOR i IN 1..5
    LOOP
        sys.dbms_output.put_line(i); 
    END LOOP for_loop;
END;
```

<br/>


比較好的做法是不要將上下邊界值 hard-coded，可能用常數設定其值，並給予較具意義的常數名稱，讓程式的可讀性與可維護性更好。  

```sql
DECLARE
    co_lower_bound CONSTANT SIMPLE_INTEGER := 1; 
    co_upper_bound CONSTANT SIMPLE_INTEGER := 5;
BEGIN
    <<for_loop>>
    FOR i IN co_lower_bound..co_upper_bound 
    LOOP
        sys.dbms_output.put_line(i); 
    END LOOP for_loop;
END;
```
