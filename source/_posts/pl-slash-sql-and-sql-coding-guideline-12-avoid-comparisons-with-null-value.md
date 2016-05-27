---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 12 - Avoid comparisons with null value"
date: 2015-11-26 01:12:00
comments: true
categories: 
keywords: 
description: "PL/SQL &amp; SQL CODING GUIDELINE 12 - Avoid comparisons with null value"
---

條款十二是在說當判斷變數是否為 null 時，不要像下面這樣使用 `=` 去判斷。

<!-- More -->

{% codeblock lang:psql %}
DECLARE 
	v_str VARCHAR2(30); 
BEGIN 
	if v_str = null then 
		…
	end if; 
END;
{% endcodeblock %}

<br/>


因為 null 不等於任何東西，即使是 null 也不等於 null。  

{% img /images/posts/PLSQLCopRule12/1.png %}

<br/>


正確的方式應該是用 is 或 is not 去做判斷。  

{% codeblock lang:psql %}
DECLARE 
	v_str VARCHAR2(30); 
BEGIN 
	if v_str is null then 
		…
	end if; 
END;
{% endcodeblock %}
