---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 18 - Avoid declaring NUMBER variables or subtypes with no precision"
date: 2015-12-05 18:48:00
comments: true
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
description: "PL/SQL &amp; SQL CODING GUIDELINE 18 - Avoid declaring NUMBER variables or subtypes with no precision"
---

條款十八，避免在宣告 Number 型態的變數或是 SubType 時未設定整數位數。  

<!-- More -->

<br/>


像是下面這樣，變數宣告時未指定整數位數，預設精確度為 38 位。  

{% codeblock lang:psql %}
DECLARE
    v_number number; 
BEGIN 
    ... 
END;
```

<br/>


如果使用上已經知道明確位數，那建議在宣告時還是明確的指定。  

{% codeblock lang:psql %}
DECLARE
    v_number number(9, 2); 
BEGIN 
    ... 
END;
```
