---
title: >-
  PL/SQL & SQL CODING GUIDELINE 46 - Always use EXIT WHEN instead of an IF
  statement to exit from a loop
date: 2017-06-07 09:52:06
tags: [PL/SQL and SQL Coding Guidelines]
---

條款四十六，總是使用 EXIT WHILE loop 去跳離迴圈，不要使用 IF...EXIT。  

<!-- More -->

<br/>


像是下面這樣的程式使用 IF 判斷要跳離迴圈的條件是否成立，成立的話使用 EXIT 跳離迴圈。如果 IF 判斷只是單純的用來處裡跳離迴圈的條件判斷，那這樣的撰寫方式就不是那麼洽當，程式碼變得比較冗餘，且不好維護。  

```sql
BEGIN 
  <<process_employees>> 
  LOOP 
    ... 
    IF 
      ... 
    THEN 
      EXIT process_employees; 
    END IF; 
    ... 
  END LOOP process_employees; 
END;
```

<br/>


比較好的做法是用 EXIT WHEN，將跳離迴圈的判斷直接寫在 EXIT WHEN 後面，這樣程式會比較簡短、清晰、且易於維護。  

```sql
BEGIN 
  <<process_employees>> 
  LOOP 
    ... 
    EXIT process_employees WHEN (...); 
  END LOOP process_employees; 
END;
```