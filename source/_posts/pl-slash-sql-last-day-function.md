---
layout: post
title: "PL/SQL - LAST_DAY function"
date: 2015-07-15 22:31:00
comments: true
tags: [PL/SQL]
keywords: "PL/SQL"
description: "PL/SQL - LAST_DAY function"
---

LAST_DAY function 會依帶入的日期回傳對應月份的最後一天。  

<!-- More -->

<br/>


使用語法如下：  

    LAST_DAY( date )

其中 date 為要處理的日期，帶入即會回傳對應月份的最後一天。  

<br/>


像是要取得當月的最後一天，可以像下面這樣叫用：  

    last_day(sysdate)


使用上會像下面這樣：  

{% img /images/posts/LastDayFunction/1.png %}
<br/>

Link
----
* [Oracle/PLSQL: LAST_DAY Function](http://www.techonthenet.com/oracle/functions/last_day.php)
