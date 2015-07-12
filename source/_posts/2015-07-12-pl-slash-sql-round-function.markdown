---
layout: post
title: "PL/SQL - Round function"
date: 2015-07-12 22:12
comments: true
categories: [PL/SQL]
keywords: "PL/SQL"
description: "PL/SQL - Round function"
---

Round function 可將帶入的值依指定的位數下去做四捨五入運算並回傳。  

<!-- More -->

<br/>


使用語法如下：  

    ROUND( number [, decimal_places] )


number 是要做四捨五入的值，decimal_places 是要做四捨五入的位數。  

<br/>


這邊的 decimal_places 可以是正值，也可以是負值。如果是正值表示的是小數點後的位數，如果是負值則表示小數點前的位數。  

<br/>


寫起來就像下面這樣：  

{% img /images/posts/RoundFunction/1.png %}

{% img /images/posts/RoundFunction/2.png %}

{% img /images/posts/RoundFunction/3.png %}

{% img /images/posts/RoundFunction/4.png %}

{% img /images/posts/RoundFunction/5.png %}

<br/>

Link
----
* [Oracle/PLSQL: ROUND Function \(with numbers\)](http://www.techonthenet.com/oracle/functions/round_nbr.php)
