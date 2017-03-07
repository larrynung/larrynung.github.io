---
title: >-
  PL/SQL & SQL CODING GUIDELINE 32 - Avoid using %NOTFOUND directly after the
  FETCH when working with BULK OPERATIONS and LIMIT clause. Use
  [array_name].COUNT() instead to check whether further FETCHs are needed
date: 2016-08-13 00:00:11
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
---

條款三十二，當使用 BULK 與 LIMIT 操作時，避免直接在後面用 %NOTFOUND 判斷是否有資料處理，應改用 COUNT() 判斷。  

<!-- More -->

<br/>


像是下面這樣的撰寫方式，迴圈內每次會處理 5 筆資料，假設今天總資料量為 14，那第三次處理時因為剩餘的筆數 4 小於 LIMIT 設定的筆數 5，%NOTFOUND 會為 true 跳離，剩餘的資料就都沒有跑到。  

{% codeblock lang:sql %}
-- This example will only show 10 of 14 employees 
DECLARE 
    TYPE t_employee_type IS TABLE OF emp%ROWTYPE; 
    t_employees t_employee_type; 
    CURSOR c_emp 
        IS SELECT * 
            FROM emp ORDER BY empno; 
BEGIN 
    OPEN c_emp; 
    <<process_emp>> 
    LOOP 
        FETCH c_emp BULK COLLECT INTO t_employees LIMIT 5; 
        EXIT process_emp WHEN c_emp%NOTFOUND; 
        <<display_emp>> 
        FOR i IN 1..t_employees.COUNT() 
        LOOP 
            sys.dbms_output.put_line(t_employees(i).ename); 
        END LOOP display_emp; 
    END LOOP process_emp; 
    CLOSE c_emp; 
END;
{% endcodeblock %}

<br/>


要解決這樣的問題可以改用 COUNT() 去判斷是否為 0，為 0 則跳掉，這樣所有的資料都會跑到，但以總筆數為 14，單次處理筆數為 5 的例子來看，這寫法會在跑到第四次時才發現剩餘筆數為 0 跳離，多跑了一次迴圈運算。  

{% codeblock lang:sql %}
-- This example does 4 fetches where 3 were sufficient 
DECLARE 
    TYPE t_employee_type IS TABLE OF emp%ROWTYPE; 
    t_employees t_employee_type; 
    CURSOR c_emp 
        IS SELECT * 
            FROM emp 
            ORDER BY empno; 
BEGIN 
    OPEN c_emp; 
    <<process_emp>> 
    LOOP 
        FETCH c_emp BULK COLLECT INTO t_employees LIMIT 5; 
        EXIT WHEN t_employees.COUNT() = 0; 
        <<display_emp>> 
        FOR i IN 1..t_employees.COUNT() 
        LOOP 
            sys.dbms_output.put_line(t_employees(i).ename); 
        END LOOP display_emp; 
    END LOOP process_emp; 
    CLOSE c_emp; 
END;
{% endcodeblock %}

<br/>


最好的方式是將跳離的判斷往後移，同時判斷 COUNT() 與 %NOTFOUND，這樣只有總筆數剛好能被單次處理筆數整除的狀況下才會多跑一次，以總筆數 14 的例子來看，如果單次處理筆數為 5，那迴圈只要跑三次即可。  

{% codeblock lang:sql %}
-- This examples does the trick (3 fetches only and process all rows) 
DECLARE 
    TYPE t_employee_type IS TABLE OF emp%ROWTYPE; 
    t_employees t_employee_type; 
    CURSOR c_emp 
        IS SELECT * 
            FROM emp 
            ORDER BY empno; 
BEGIN 
    OPEN c_emp; 
    <<process_emp>> 
    LOOP 
        FETCH c_emp BULK COLLECT INTO t_employees LIMIT 5; 
        <<display_emp>> 
        FOR i IN 1..t_employees.COUNT() 
        LOOP 
            sys.dbms_output.put_line(t_employees(i).ename); 
        END LOOP display_emp; 
        EXIT WHEN t_employees.COUNT() = 0 OR c_emp%NOTFOUND; 
    END LOOP process_emp; 
    CLOSE c_emp; 
END;
{% endcodeblock %}
