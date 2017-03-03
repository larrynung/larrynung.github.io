---
title: >-
  PL/SQL & SQL CODING GUIDELINE 41 - Always use a CURSOR FOR loop to process the
  complete cursor results unless you are using bulk operations
date: 2017-03-03 10:01:57
tags: [PL/SQL]
keywords: "PL/SQL"
---

條款四十一，總是使用 CURSOR for loop，除非使用 Bulk operations。

<!-- More -->

<br/>

像是下面這樣的程式：

{% codeblock lang:psql %}
...
BEGIN 
  <<read_employees>> 
  LOOP
    FETCH c_employees INTO r_employee;  
	EXIT read_employees WHEN c_employees%NOTFOUND;
    … 	
  END LOOP read_employees; 
  CLOSE c_employees;
END;
{% endcodeblock %}

<br/>


可以像下面這樣改寫，程式碼的維護性會比較好。

{% codeblock lang:psql %}
...
BEGIN 
  <<read_employees>> 
  FOR r_employee IN c_employee 
  LOOP 
    … 
  END LOOP read_employees; 
END;

{% endcodeblock %}

<br/>
