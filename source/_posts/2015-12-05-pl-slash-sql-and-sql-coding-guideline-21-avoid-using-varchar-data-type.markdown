---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 21 - Avoid using VARCHAR data type"
date: 2015-12-05 20:10
comments: true
categories: 
keywords: 
description: "PL/SQL &amp; SQL CODING GUIDELINE 21 - Avoid using VARCHAR data type"
---

條款二十一，避免使用 Varchar 型態。  

<!-- More -->

<br/>


Varchar 型態在工業標準上市可以儲存空字串的，在 Oracle 這邊並未遵循這樣的標準，會將空字串變為 null 值，但難保某天不會改變。  

{% codeblock lang:psql %}
DECLARE 
    v_str varchar(4000);
BEGIN 
    …
END;
{% endcodeblock %}

<Br/>


Oracle 這邊建議使用 Varchar2 型態，而不是使用 Varchar 型態。

{% codeblock lang:psql %}
DECLARE 
    v_str varchar2(4000); 
BEGIN 
    …
END;
{% endcodeblock %}
