---
title: "PL/SQL - Round function"
date: "2015-07-12 22:12:00"
description: "PL/SQL - Round function"
tags: [PL/SQL]
---

Round function 可將帶入的值依指定的位數下去做四捨五入運算並回傳。

使用語法如下：

ROUND( number [, decimal_places] )

number 是要做四捨五入的值，decimal_places 是要做四捨五入的位數。

這邊的 decimal_places 可以是正值，也可以是負值。如果是正值表示的是小數點後的位數，如果是負值則表示小數點前的位數。

寫起來就像下面這樣：

![/images/posts/RoundFunction/1.png](/images/posts/RoundFunction/1.png)

![/images/posts/RoundFunction/2.png](/images/posts/RoundFunction/2.png)

![/images/posts/RoundFunction/3.png](/images/posts/RoundFunction/3.png)

![/images/posts/RoundFunction/4.png](/images/posts/RoundFunction/4.png)

![/images/posts/RoundFunction/5.png](/images/posts/RoundFunction/5.png)

Link
----
* [Oracle/PLSQL: ROUND Function \(with numbers\)](http://www.techonthenet.com/oracle/functions/round_nbr.php)