---
title: "SQLCop - Auditing Database for Best Practices"
date: "2014-02-23 21:37:00"
description: "SQLCop - Auditing Database for Best Practices"
---


SQLCop 是專門為 SQL Server 量身打造的分析工具。能針對現有的 SQL Server 進行分析，會從資料庫的 Stored Procedure、 Schema、Table View、 Index 等不同面向下去分析，看看是否有改善的空間。 

<!-- More -->

使用前請先連至 [Less Than Dot - SqlCop](http://sqlcop.lessthandot.com/) 這邊，將程式下載並安裝...  

{% img /images/posts/SQLCop/1.png %}

<br/>

安裝完成將 SQLCop 程式開啟，選取要分析的SQL Server與資料庫，帶入帳密並按下 'Connect' 按鈕，讓 SQLCop 與 SQL Server 資料庫進行連線。 

{% img /images/posts/SQLCop/2.png %}

<br/>

連線完成會看到下面這樣的畫面。 

{% img /images/posts/SQLCop/3.png %}

<br/>

SQLCop  會將偵測到的問題依型態與檢查的規則下去用階層分類，將之展開後可看到下面會列出我們違法規則的地方。若這邊不懂到底是哪裡有問題，可在規則節點上進行點擊，SQLCop 會帶出對應的說明。

{% img /images/posts/SQLCop/4.png %}

<br/>

Link
----
* [Less Than Dot - SqlCop](http://sqlcop.lessthandot.com/)
* [SQL Cop Review](https://www.simple-talk.com/sql/sql-tools/sql-cop-review/)
