---
title: "PL/SQL - NUMTODSINTERVAL function"
date: "2015-07-12 13:55:00"
description: "PL/SQL - NUMTODSINTERVAL function"
tags: [PL/SQL]
---


NUMTODSINTERVAL function 會將帶入的值轉成特定單位的 Interval。  

<!-- More -->

<br/>


使用語法如下：

    NUMTODSINTERVAL( number, expression )


number 這邊帶入的是要轉換的值，expression 這邊帶入的是要轉換的單位，可以是 Day、 Hour、 Minute、 Second。  

<br/>


使用上可搭配日期使用，對日期做些增減處理。像是下面這樣：  

{% img /images/posts/NUMTODSINTERVALFunction/1.png %}

{% img /images/posts/NUMTODSINTERVALFunction/2.png %}

{% img /images/posts/NUMTODSINTERVALFunction/3.png %}

{% img /images/posts/NUMTODSINTERVALFunction/4.png %}

{% img /images/posts/NUMTODSINTERVALFunction/5.png %}

{% img /images/posts/NUMTODSINTERVALFunction/6.png %}

<br/>

Link
----
* [Oracle/PLSQL: NUMTODSINTERVAL Function](http://www.techonthenet.com/oracle/functions/numtodsinterval.php)
