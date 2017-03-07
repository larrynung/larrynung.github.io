---
title: PL/SQL & SQL CODING GUIDELINE 40 - Always label your loops
date: 2017-03-02 10:25:50
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
---

條款四十，如果程式中有 loop，嘗試使用 label 讓他的區塊範圍更為清楚。

<!-- More -->

<br/>

像是下面這樣的程式：

{% codeblock lang:psql %}
BEGIN 
  FOR r_employee IN (SELECT * FROM emp) 
  LOOP 
    … 
  END LOOP; 
END;
{% endcodeblock %}

<br/>


可以像下面這樣改寫，在 loop 的前面加上 Label，然後在 End 後加上 Label Name。

{% codeblock lang:psql %}
BEGIN 
  <<process_employees>> 
  FOR r_employee IN (SELECT * FROM emp) 
  LOOP 
    … 
  END LOOP process_employees; 
END;
{% endcodeblock %}

<br/>


這樣程式碼的區塊範圍清楚許多。  