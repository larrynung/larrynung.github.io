---
title: "PL/SQL  SQL CODING GUIDELINE 56 - Avoid unhandled exceptions"
date: "2017-07-04 13:21:50"
tags: [PL/SQL and SQL Coding Guidelines]
---


條款五十六，避免未處理的例外。

<!-- More -->

<br/>


像是下面這段程式，當沒資料或是資料過多時 Select into 就會丟出例外。  

```plsql
CREATE OR REPLACE PACKAGE BODY department_api IS 
  FUNCTION name_by_id (in_id IN departments.department_id%TYPE) 
    RETURN departments.department_name%TYPE IS 
    l_department_name departments.department_name%TYPE; 
  BEGIN 
    SELECT department_name 
    INTO l_department_name 
    FROM departments 
    WHERE department_id = in_id; 

    RETURN l_department_name; 
  END name_by_id; 
END department_api;
```

<br/>


建議是要確保程式不會有未處理的例外，像是上面這樣的程式就要加處理 NO_DATA_FOUND 與 TOO_MANY_ROWS。  

```plsql
CREATE OR REPLACE PACKAGE BODY department_api IS 
  FUNCTION name_by_id (in_id IN departments.department_id%TYPE) 
    RETURN departments.department_name%TYPE IS 
    l_department_name departments.department_name%TYPE; 
  BEGIN 
    SELECT department_name 
    INTO l_department_name 
    FROM departments 
    WHERE department_id = in_id; 

    RETURN l_department_name; 
  EXCEPTION 
    WHEN NO_DATA_FOUND 
    THEN 
      RETURN NULL; 
    WHEN TOO_MANY_ROWS 
    THEN 
      RAISE; 
    END name_by_id; 
END department_api;
```
