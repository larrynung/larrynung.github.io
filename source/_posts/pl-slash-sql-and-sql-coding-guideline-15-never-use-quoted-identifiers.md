---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 15 - Never use quoted identifiers"
date: 2015-12-05 18:42:00
comments: true
categories: 
keywords: 
description: "PL/SQL &amp; SQL CODING GUIDELINE 15 - Never use quoted identifiers"
---

條款十五是說在變數宣告時，變數的名稱不要加上雙引號。  

<!-- More -->

<br/>


像是下面這樣，宣告的變數加上雙引號是合法的。  

{% codeblock lang:psql %}
DECLARE 
	"v_str" VARCHAR2(30) ; 
BEGIN 
	…
END main;
{% endcodeblock %}

<br/>


但不建議這樣宣告，建議還是不要加上雙引號。  

{% codeblock lang:psql %}
DECLARE 
	v_str VARCHAR2(30) ; 
BEGIN 
	…
END main;
{% endcodeblock %}
