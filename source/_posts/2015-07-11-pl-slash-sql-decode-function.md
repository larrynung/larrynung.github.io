---
layout: post
title: "PL/SQL - Decode function"
date: 2015-07-11 20:33:00
comments: true
categories: [PL/SQL]
keywords: "PL/SQL, Decode"
description: "PL/SQL - Decode function"
---

Decode function 可用於取代簡單的 If-Then-Else 陳述式。

<!-- More -->

<br/>


使用語法如下：  

    DECODE( expression , search , result [, search , result]... [, default] )

<br/>

簡單來說如果 expression 的值等同 search 值的話，則回傳對應的 result 值。   

<br/>


像是要將數值帶入，依其值決定要回傳 'true' 或是 'false'，可以像下面這樣撰寫：  

{% img /images/posts/DecodeFunction/1.png %}

<br/>


{% img /images/posts/DecodeFunction/2.png %}

<br/>

Link
----
* [Oracle/PLSQL: DECODE Function](http://www.techonthenet.com/oracle/functions/decode.php)
