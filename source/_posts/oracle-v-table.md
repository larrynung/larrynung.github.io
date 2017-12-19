---
title: "Oracle - v table"
date: 2017-12-19 21:47:54
tags: [Oracle]
---

v$version 資料表主要存放著 Oracle 核心元件的版本資訊，要查閱版本資訊的話可直接查閱該表。  

<!-- More -->  

    SELECT * FROM v$version;


 {% asset_img 1.png %}

<br/>


Link
----
* [V$VERSION](https://docs.oracle.com/cd/B28359_01/server.111/b28320/dynviews_3112.htm#REFRN30296)
* [Oracle / PLSQL: Retrieve Oracle version information](https://www.techonthenet.com/oracle/questions/version.php)
