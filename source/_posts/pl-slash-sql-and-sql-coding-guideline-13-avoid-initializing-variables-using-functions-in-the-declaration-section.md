---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 13 - Avoid initializing variables using functions in the declaration section"
date: 2015-11-26 05:52:00
comments: true
tags: [PL/SQL]
keywords: "PL/SQL"
description: "PL/SQL &amp; SQL CODING GUIDELINE 13 - Avoid initializing variables using functions in the declaration section"
---

條款十三是說要避免在變數宣告的同時呼叫 function 去初始變數。  

<!-- More -->

{% codeblock lang:psql %}
DECLARE 
	l_company_name VARCHAR2(30) := util_pck.get_company_name(in_id => 47);
BEGIN 
	… 
END;
{% endcodeblock %}

<br/>


因為在變數宣告的地方呼叫 function 去初始變數，function 發生例外時是無法攔截處理的。  

<br/>


因此要像下面這樣將宣告與初始拆開處理。  

{% codeblock lang:psql %}
DECLARE 
	 v_str VARCHAR2(30); 
BEGIN 
	<<init>> 
	BEGIN 
		v_str := util_pck.get_company_name(inId => 47); 
	EXCEPTION 
		WHEN VALUE_ERROR THEN 
			...
	END init; 
END;
{% endcodeblock %}
