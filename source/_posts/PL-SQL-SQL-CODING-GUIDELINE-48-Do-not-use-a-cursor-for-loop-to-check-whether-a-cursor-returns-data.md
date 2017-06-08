---
title: >-
  PL/SQL & SQL CODING GUIDELINE 48 - Do not use a cursor for loop to check
  whether a cursor returns data
date: 2017-06-08 22:04:27
tags: [PL/SQL and SQL Coding Guidelines]
---

條款四十八，不要遍巡 CURSOR 去確認是否含有資料。  

<!-- More -->

<br/>


像是下面這段程式片巡走訪 CURSOR 以確認是否含有資料，這樣並不是很好的寫法。  

```sql
DECLARE 
  l_employee_found BOOLEAN := FALSE; 
  … 
BEGIN 
  <<check_employees>> 
  FOR r_employee IN c_employee 
  LOOP 
    l_employee_found := TRUE; 
  END LOOP check_employees; 
END;
```

<br/>


比較好的作法應該像是下面這段程式這樣，將 CURSOR 開啟，嘗試 Fetch 一筆資料，利用 CURSOR 的 %FOUND 去判斷是否含有資料，最後將 CURSOR 關閉。  

```sql
DECLARE 
  l_employee_found BOOLEAN := FALSE; 
  … 
BEGIN 
  OPEN c_employee; 
  FETCH c_employee INTO r_employee; 
  l_employee_found := c_employee%FOUND; 
  CLOSE c_emplyoee; 
END;
```
