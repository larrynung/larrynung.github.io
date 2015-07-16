---
layout: post
title: "PL/SQL - MONTHS_BETWEEN Function"
date: 2015-07-16 22:13
comments: true
categories: [PL/SQL]
keywords: "PL/SQL"
description: "PL/SQL - MONTHS_BETWEEN Function"
---

MONTHS_BETWEEN function 可計算兩個日期相差多少月份。  

<!-- More -->

<br/>


使用語法如下：  

    MONTHS_BETWEEN( date1, date2 )


帶入的兩個日期，若第一個日期大過第二個日期，則回傳正值的月份差。反之則回傳負值月份差。  

<br/>

像是下面這樣叫用就會傳回 2：  

    MONTHS_BETWEEN(ADD_MONTHS(sysdate, 2), sysdate)


像下面這樣叫用就會傳回 -2：  

    MONTHS_BETWEEN(sysdate, ADD_MONTHS(sysdate, 2))


使用上會像下面這樣：  

{% img /images/posts/MonthsBetweenFunction/1.png %}

<br/>

Link
----
* [Oracle/PLSQL: MONTHS_BETWEEN Function](http://www.techonthenet.com/oracle/functions/months_between.php)
