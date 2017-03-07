---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 2 - Always have a matching loop or block label"
date: 2015-09-20 23:51:00
comments: true
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
description: "PL/SQL &amp; SQL CODING GUIDELINE 2 - Always have a matching loop or block label"
---

條款二，如果程式中有迴圈區塊，為其加上 label 讓他的區塊範圍更為清楚。

<!-- More -->

<br/>


像是下面這樣的程式：  

{% codeblock lang:psql %}
SET SERVEROUTPUT ON
DECLARE
    i PLS_INTEGER;
Begin
    FOR i IN 1..10
    LOOP
        DBMS_OUTPUT.put_line('i =' || i);
    End LOOP;
End;
{% endcodeblock %}

<br/>


可以像下面這樣改寫，在 For...Loop  前面加上 Label，然後在 End 後加上 Label Name。

{% codeblock lang:psql %}
SET SERVEROUTPUT ON
DECLARE
    i PLS_INTEGER;
Begin
    <<Print1To10>>
    FOR i IN 1..10
    LOOP
        DBMS_OUTPUT.put_line('i =' || i);
    End LOOP Print1To10;
End;
{% endcodeblock %}

改完程式碼的區塊範圍清楚了許多。
