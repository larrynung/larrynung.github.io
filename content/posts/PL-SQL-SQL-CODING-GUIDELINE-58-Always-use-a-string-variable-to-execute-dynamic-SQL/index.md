---
title: ">-"
date: "2017-07-10 13:36:21"
tags: [PL/SQL and SQL Coding Guidelines]
---


條款五十八，總是使用字串變數去執行 Dynamic SQL。  

<!-- More -->

<br/>


像是下面這段程式直接將要執行的字串帶入執行 Dynamic SQL 就不被建議。  

```plsql
DECLARE
  l_empno emp.empno%TYPE := 4711;
BEGIN
  EXECUTE IMMEDIATE 'DELETE FROM emp WHERE epno = :p_empno' USING l_empno;
END;
```

<br/>


建議的做法是用字串變數儲存要執行的 Dynamic SQL 語法，在將字串變數帶入動態運行。這樣的做法在串接複雜語句時會比較容易，在例外處理上若有需要也可以直接將變數拿來使用。  

```plsql
DECLARE
  l_empno emp.empno%TYPE := 4711;
  l_sql VARCHAR2(32767);
BEGIN
  l_sql := 'DELETE FROM emp WHERE epno = :p_empno';
  EXECUTE IMMEDIATE l_sql USING l_empno;
EXCEPTION
  WHEN others
  THEN
    DBMS_OUTPUT.PUT_LINE(l_sql);
END;
```
