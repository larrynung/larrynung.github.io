---
layout: post
title: "PL/SQL - ADD_MONTHS function"
date: 2015-07-14 21:47:00
comments: true
tags: [PL/SQL]
keywords: "PL/SQL"
description: "PL/SQL - ADD_MONTHS function"
---

ADD_MONTHS function 可將帶入的日期月份做加減處理後回傳。  

<!-- More -->

<br/>


使用語法如下：  

    ADD_MONTHS( date1, number_months )


其中 data1 為要做處理的日期，number_months 為要加減的月份。  

<br/>


number_months 帶入的值為正值，表示是要加上指定的月份，反之表示要減上指定的月份。  

<br/>

像是要將當前的日期加三個月，可這樣叫用：  

    add_months(sysdate, 3)


要將當前日期減三個月，可這樣叫用：  

    add_months(sysdate, -3)


使用上會像下面這樣：

{% img /images/posts/AddMonthsFunction/1.png %}

<br/>

Link
----
* [Oracle/PLSQL: ADD_MONTHS Function](http://www.techonthenet.com/oracle/functions/add_months.php)
