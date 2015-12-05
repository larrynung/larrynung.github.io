---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 19 - Try to use PLS_INTEGER instead of NUMBER for arithmetic operations with integer values (no decimal point)"
date: 2015-12-05 19:12
comments: true
categories: 
keywords: 
description: "PL/SQL &amp; SQL CODING GUIDELINE 19 - Try to use PLS_INTEGER instead of NUMBER for arithmetic operations with integer values (no decimal point)"
---

條款十九，用 PLS_INTEGER 去表示整數。  

<!-- More -->

<br/>


如果要宣告整數，不要用 Number 型態去宣告。

{% codeblock lang:psql %}
DECLARE
    v_number number(38, 0);
BEGIN 
    ... 
END;
{% endcodeblock %}

<br/>



建議使用 PLS_INTEGER，因為使用 PLS_INTEGER 型態使用的記憶體會比較少，且效能上會快上三倍。  

{% codeblock lang:psql %}
DECLARE
    v_number PLS_INTEGER;
BEGIN
    ...
END;
{% endcodeblock %}
