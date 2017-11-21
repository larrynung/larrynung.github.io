---
title: >-
  PL/SQL & SQL CODING GUIDELINE 59 - Try to use output bind arguments in the
  RETURNING INTO clause of dynamic INSERT, UPDATE, or DELETE statements rather
  than the USING clause
date: 2017-11-21 13:28:09
tags: [PL/SQL & SQL CODING GUIDELINE]
---

條款五十九，嘗試使用 RETURNING INTO，而非使用 Using OUT 綁定輸出參數。

<!-- More -->

<br/>


像是下面這段程式使用了 Using OUT 語法去綁定輸出參數就不被建議。  

```sql
CREATE OR REPLACE PACKAGE BODY employee_api IS 
  PROCEDURE upd_salary (in_employee_id IN employees.employee_id%TYPE ,in_increase_pct IN types_up.percentage ,out_new_salary OUT employees.salary%TYPE) 
  IS 
    co_sql_stmt CONSTANT types_up.big_string_type := ' UPDATE employees SET salary = salary + (salary / 100 * :1) WHERE employee_id = :2 RETURNING salary INTO :3'; 
  BEGIN 
    EXECUTE IMMEDIATE co_sql_stmt 
    USING in_increase_pct, in_employee_id, OUT out_new_salary; 
  END upd_salary; 
END employee_api; /
```

<br/>


建議的做法是用 RETURNING INTO 語法去綁定輸出參數。  

```sql
CREATE OR REPLACE PACKAGE BODY employee_api IS 
  PROCEDURE upd_salary (in_employee_id IN employees.employee_id%TYPE ,in_increase_pct IN types_up.percentage ,out_new_salary OUT employees.salary%TYPE) 
  IS 
    co_sql_stmt CONSTANT types_up.big_string_type := 'UPDATE employees SET salary = salary + (salary / 100 * :1) WHERE employee_id = :2 RETURNING salary INTO :3'; 
  BEGIN 
    EXECUTE IMMEDIATE co_sql_stmt 
    USING in_increase_pct, in_employee_id 
    RETURNING INTO out_new_salary; 
  END upd_salary; 
END employee_api; /
```