---
title: Oracle - Generating HTML Reports from SQL*Plus
date: 2019-01-03 00:03:42
tags: [Oracle]
---

要用 SQL*Plus 將查詢的資料輸出成 HTML 報表，可以準備像下面這樣的 SQL 檔。  

<!-- More -->

{% asset_img 1.png %}

<br/>


開啟 MARKUP HTML 與 SPOOL。  

    SET MARKUP HTML ON SPOOL ON

<br/>


然後指定 SPOOL 要輸出的檔案。 

    SPOOL <File>

<br/>


接著撈出要產出的資料。  

<br/>


然後將 MARKUP HTML 與 SPOOL 關掉即可。  

    SET MARKUP HTML OFF SPOOL OFF

<br/>


用 SQL*Plus 運行剛撰寫的 SQL 檔。  

{% asset_img 2.png %}

<br/>


{% asset_img 3.png %}

<br/>


HTML 報表即會被輸出到指定的輸出檔案。  

{% asset_img 4.png %}

<br/>


Link
----
* [Generating HTML Reports from SQL*Plus](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_seven.htm#SQPUG017)
