---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 24 -Try to use boolean data type for values with dual meaning"
date: 2015-12-17 05:52
comments: true
categories: 
keywords: 
description: "PL/SQL &amp; SQL CODING GUIDELINE 24 -Try to use boolean data type for values with dual meaning"
---

條款二十四，當值只有兩種狀態時，試著使用 Boolean 型態。  

<!-- More -->

<br/>


像是如果要表達的是是否為較大的數值，如果沒有特別的理由，那就不該使用數值表示，因為數值代表的意義沒有 Boolean 型態來的明確。  

{% codeblock lang:psql %}
DECLARE 
    v_IsBigger number(1) := 1; 
BEGIN 
    DBMS_OUTPUT.PUT_LINE(CASE WHEN v_IsBigger = 1 THEN 'True' ELSE 'False' END); 
END;
{% endcodeblock %}

<br/>


若用 Boolean 型態表達會比較清楚。  

{% codeblock lang:psql %}
DECLARE 
    v_IsBigger BOOLEAN := true; 
BEGIN 
    DBMS_OUTPUT.PUT_LINE(CASE WHEN v_IsBigger THEN 'True' ELSE 'False' END); 
END;
{% endcodeblock %}
