---
title: "PL/SQL - NUMTODSINTERVAL function"
date: "2015-07-12 13:55:00"
description: "NUMTODSINTERVAL function 會將帶入的值轉成特定單位的 Interval。 使用語法如下： NUMTODSINTERVAL( number, expression ) number 這邊帶入的是要轉換的值，expression 這邊帶入的是要轉換的單位，"
tags: [PL/SQL]
---

NUMTODSINTERVAL function 會將帶入的值轉成特定單位的 Interval。

使用語法如下：

NUMTODSINTERVAL( number, expression )

number 這邊帶入的是要轉換的值，expression 這邊帶入的是要轉換的單位，可以是 Day、 Hour、 Minute、 Second。

使用上可搭配日期使用，對日期做些增減處理。像是下面這樣：

![1.png](/images/posts/NUMTODSINTERVALFunction/1.png)

![2.png](/images/posts/NUMTODSINTERVALFunction/2.png)

![3.png](/images/posts/NUMTODSINTERVALFunction/3.png)

![4.png](/images/posts/NUMTODSINTERVALFunction/4.png)

![5.png](/images/posts/NUMTODSINTERVALFunction/5.png)

![6.png](/images/posts/NUMTODSINTERVALFunction/6.png)

Link
----
* [Oracle/PLSQL: NUMTODSINTERVAL Function](http://www.techonthenet.com/oracle/functions/numtodsinterval.php)