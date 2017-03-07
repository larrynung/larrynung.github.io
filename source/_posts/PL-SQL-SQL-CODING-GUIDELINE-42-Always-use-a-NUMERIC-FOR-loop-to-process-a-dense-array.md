---
title: >-
  PL/SQL & SQL CODING GUIDELINE 42 - Always use a NUMERIC FOR loop to process a
  dense array
date: 2017-03-07 13:42:25
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
---

條款四十二，總是使用 NUMERIC FOR loop 去處理 dense array。  

<!-- More -->

<br/>


像是下面這樣的程式：

{% codeblock lang:psql %}
...
BEGIN 
  <<process_employees>> 
  LOOP 
    EXIT process_employees WHEN i > t_employees.COUNT();
    … 
    i := i + 1;
  END LOOP process_employees; 
END;
{% endcodeblock %}

<br/>


可以像下面這樣改寫，程式碼的維護性會比較好。

{% codeblock lang:psql %}
...
BEGIN 
  <<process_employees>> 
  FOR i IN 1..t_employees.COUNT() 
  LOOP 
    … 
  END LOOP process_employees; 
END;
{% endcodeblock %}

<br/>