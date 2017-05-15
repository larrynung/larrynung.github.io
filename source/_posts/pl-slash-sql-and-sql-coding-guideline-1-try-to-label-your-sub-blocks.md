---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 1 - Try to label your sub blocks"
date: 2015-09-20 23:21:00
comments: true
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
description: "PL/SQL &amp; SQL CODING GUIDELINE 1 - Try to label your sub blocks"
---

條款一，如果程式中有子 block，嘗試使用 label 讓他的區塊範圍更為清楚。  

<!-- More -->

<br/>


像是下面這樣的程式：  

{% codeblock lang:psql %}
SET SERVEROUTPUT ON
Begin
    DBMS_OUTPUT.put_line('Start');
    Begin
        DBMS_OUTPUT.put_line('Processing...');
    End;
    DBMS_OUTPUT.put_line('End');
End;
```

<br/>


可以像下面這樣改寫，在子 Block 的 Begin 前面加上 Label，然後在 End 後加上 Label Name。  

{% codeblock lang:psql %}
SET SERVEROUTPUT ON
Begin
    DBMS_OUTPUT.put_line('Start');
    <<Processing>>
    Begin 
        DBMS_OUTPUT.put_line('Processing...');
    End Processing;
    DBMS_OUTPUT.put_line('End');
End;
```

改完程式碼的區塊範圍清楚了許多。  


