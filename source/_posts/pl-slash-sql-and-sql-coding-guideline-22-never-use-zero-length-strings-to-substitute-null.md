---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 22 - Never use zero-length strings to substitute NULL"
date: 2015-12-15 05:11:00
comments: true
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
description: "PL/SQL &amp; SQL CODING GUIDELINE 22 - Never use zero-length strings to substitute NULL"
---

條款二十二，不要用空字串去代替 Null 值。  

<!-- More -->

<br/>

在  Oracle 這邊不論是對的 Varchar 或是 Varchar2 型態賦予空字串，Oracle 都會將其視為 Null，所以這邊不建議將其設為空字串。  

{% codeblock lang:psql %}
DECLARE 
    v_str varchar2(4000) := ''; 
BEGIN 
    DBMS_OUTPUT.PUT_LINE(CASE WHEN v_str is null THEN 'null' ELSE 'not null' END); 
END;
{% endcodeblock %}

<br/>


而是應該像下面，沒特別塞值時預設就是 Null。  

{% codeblock lang:psql %}
DECLARE 
    v_str varchar2(4000); 
BEGIN 
    DBMS_OUTPUT.PUT_LINE(CASE WHEN v_str is null THEN 'null' ELSE 'not null' END); 
END;
{% endcodeblock %}
