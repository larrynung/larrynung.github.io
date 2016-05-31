---
layout: post
title: "PL/SQL - NEXT_DAY function"
date: 2015-07-15 21:49:00
comments: true
tags: [PL/SQL]
keywords: "PL/SQL"
description: "PL/SQL - NEXT_DAY function"
---

NEXT_DAY function returns the first weekday that is greater than a date。  

<!-- More -->

<br/>


使用語法如下：  

    NEXT_DAY( date, weekday )

其中 date 為基準日，weekday 指定要回傳的日期為星期幾。  

<br/>


weekday 可為 SUNDAY、MONDAY、TUESDAY、WEDNESDAY、THURSDAY、FRIDAY、SATURDAY。  

<br/>


像是要找尋下一個星期日，可這樣叫用：  

    next_day(sysdate, 'SUNDAY')


使用上會像下面這樣：

{% img /images/posts/NextDayFunction/1.png %}

<br/>

Link
----
* [Oracle/PLSQL: NEXT_DAY Function](http://www.techonthenet.com/oracle/functions/next_day.php)
