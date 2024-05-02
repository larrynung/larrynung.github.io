---
title: "PL/SQL - EXTRACT Function"
date: "2015-07-16 22:57:00"
description: "PL/SQL - EXTRACT Function"
tags: [PL/SQL]
---



EXTRACT function 可擷取日期或時間中指定部分的資料。  

<!-- More -->

<br/>


使用語法如下：  

    EXTRACT (
    { YEAR | MONTH | DAY | HOUR | MINUTE | SECOND }
    | { TIMEZONE_HOUR | TIMEZONE_MINUTE }
    | { TIMEZONE_REGION | TIMEZONE_ABBR }
    FROM { date_value | interval_value } )


我們可以帶入日期並指定擷取 年、月、日，或是帶入時間並指定擷取 時、分、秒。  

<br/>


像是要擷取現在是西元幾年，可以像下面這樣叫用：  

    EXTRACT(year from sysdate)


要擷取現在是幾點，可以像下面這樣叫用：  

    EXTRACT(hour from systimestamp)


使用上會像下面這樣：  

{% img /images/posts/ExtractFunction/1.png %}

<br/>

Link
----
* [Oracle/PLSQL: EXTRACT Function](http://www.techonthenet.com/oracle/functions/extract.php)
