---
title: >-
  PL/SQL & SQL CODING GUIDELINE 34 - Avoid procedure or function calls between a
  SQL operation and an implicit cursor
date: 2016-08-13 07:55:57
tags:
---

條款三十四，避免在 SQL 語句運行與 implicit cursor 中間使用 procedure 或是 function。  

<!-- More -->

<br/>


像是下面的例子先刪除了一些資料，後續要用 SQL%ROWCOUNT 去判斷刪除的筆數，但中間卻調用了其它 function，導致 SQL%ROWCOUNT 的值不如我們的預期。  

{% codeblock lang:sql %}
CREATE PROCEDURE remove_emp_and_process (in_id IN emp.empno%TYPE) 
AS 
BEGIN 
    DELETE FROM emp 
        WHERE empno = in_id 
    RETURNING deptno INTO l_deptno; 
    process_department (...); 
    IF SQL%ROWCOUNT > 1 
    THEN 
        -- Too many rows deleted! Rollback and recover... 
        ROLLBACK; 
    END IF; 
END remove_emp_and_process;
{% endcodeblock %}
