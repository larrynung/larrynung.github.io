---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 23 - Always define your VARCHAR2 variables using CHAR SEMANTIC"
date: 2015-12-16 05:40:00
comments: true
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
description: "PL/SQL &amp; SQL CODING GUIDELINE 23 - Always define your VARCHAR2 variables using CHAR SEMANTIC"
---

條款二十三，使用 Varchar2 時總是定義 Char Semantic。  

<!-- More -->

<br/>


預設未定義時有可能指定的是 Byte，也有可能是 Char，端看 NLS_LENGTH_SEMANTICS 參數的設定，預設是 Byte。  

{% codeblock lang:psql %}
DECLARE 
    v_str varchar(200); 
BEGIN 
    ... 
END;
```

<br/>


但通常我們指定字串應該看的是字元數，建議是將其指定用 Char。  

{% codeblock lang:psql %}
DECLARE 
    v_str varchar(200 char); 
BEGIN 
    ... 
END;
```
