---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 8 - Try to use anchored declarations for variables"
date: 2015-11-19 05:41:00
comments: true
categories: 
keywords: 
description: "PL/SQL &amp; SQL CODING GUIDELINE 8 - Try to use anchored declarations for variables"
---

條款八，使用 anchored declarations。  

<!-- More -->

<br/>


像是下面這樣的程式：  

{% codeblock lang:psql %}
DECLARE 
	v_empName VARCHAR2(10); 
BEGIN 
	… 
END;
{% endcodeblock %}

<br/>


預期要帶入的是 emp table 的 ename，這在 emp table 的 schema 中是其實是已經定義好的。如果像上面這樣另行宣告可能會不小心設錯，或是 schema 修改時會很麻煩。  

<br/>


若是使用 anchored declarations，型態會直接參照 schema 的定義，免去像這樣的困擾。  

{% codeblock lang:psql %}
DECLARE 
	 v_empName emp.ename%TYPE; 
BEGIN 
	… 
END;
{% endcodeblock %}
