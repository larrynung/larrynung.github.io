---
title: "PL/SQL - Decode function"
date: "2015-07-11 20:33:00"
description: "PL/SQL - Decode function"
tags: [PL/SQL]
---

Decode function 可用於取代簡單的 If-Then-Else 陳述式。

使用語法如下：

DECODE( expression , search , result [, search , result]... [, default] )

簡單來說如果 expression 的值等同 search 值的話，則回傳對應的 result 值。

像是要將數值帶入，依其值決定要回傳 'true' 或是 'false'，可以像下面這樣撰寫：

![1.png](/images/posts/DecodeFunction/1.png)

![2.png](/images/posts/DecodeFunction/2.png)

Link
----
* [Oracle/PLSQL: DECODE Function](http://www.techonthenet.com/oracle/functions/decode.php)