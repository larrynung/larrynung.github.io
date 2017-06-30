---
title: >-
  PL/SQL & SQL CODING GUIDELINE 55 - Avoid use of the RAISE_APPLICATION_ERROR
  built-in procedure with a hard-coded - 20,NNN error number or hard-coded
  message
date: 2017-06-30 13:49:05
tags: [PL/SQL and SQL Coding Guidelines]
---

條款五十五，避免直接使用 RAISE_APPLICATION_ERROR hard code 帶入 error number 與 error message 拋出錯誤。  

<!-- More -->

<br/>


像是下面這樣的程式，程式中直接使用 RAISE_APPLICATION_ERROR hard code 帶入 error number 與 error message 拋出錯誤，這樣 error number 與 error message 會散在許多地方，且會有重複撰寫的可能性，並不是建議採用。  

```psql
BEGIN 
  raise_application_error(-20501,'Invalid employee_id'); 
END;
```

<br/>


建議將之封裝，集中撰寫，不僅修改方便，維護起來也方便。  

```psql
BEGIN 
  err_up.raise(in_error => err.co_invalid_employee_id); 
END;
```