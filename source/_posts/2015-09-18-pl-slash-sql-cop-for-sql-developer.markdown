---
layout: post
title: "PL/SQL Cop for SQL Developer"
date: 2015-09-18 23:37
comments: true
categories: 
keywords: 
description: "PL/SQL Cop for SQL Developer"
---

PL/SQL Cop for SQL Developer 是 SQL Developer 的外掛元件，能幫靜態分析 PL/SQL 程式碼中哪些地方是寫的不好的。  

<!-- More -->

<br/>


PL/SQL Cop for SQL Developer 的檢查遵照的是 [Trivadis PL/SQL &  SQL Coding Guidelines Version 2.0](http://www.trivadis.com/sites/default/files/downloads/PLSQL_and_SQL_Coding_Guidelines_2_0_HiRes.pdf) 內的規則，若有規則不清之處可參閱這份文件，內有詳細的說明。  

<br/>


首先進行安裝。開啟 SQL Developer，選取 [ Help | Check for Updates... ]。  

{% img /images/posts/PLSQLCopForSQLDeveloper/1.png %}

<br/>


這邊可以用 Update Centers 下去找尋套件， Update Center 的位置為 http://www.salvis.com/update/tvdcc。  

也可以從本地檔案安裝，但要先至 [PL/SQL Cop for SQL Developer 1.0.11 | Philipp Salvisberg's Blog](https://www.salvis.com/blog/downloads/tvdcc-trivadis-plsql-sql-codechecker-for-sql-developer/) 這邊將套件下載下來。  

{% img /images/posts/PLSQLCopForSQLDeveloper/2.png %}

<br/>


設好後按下 Finish 按鈕進行安裝。  

{% img /images/posts/PLSQLCopForSQLDeveloper/3.png %}

<br/>


重啟 SQL Developer。  

{% img /images/posts/PLSQLCopForSQLDeveloper/4.png %}

<br/>


這時套件已經被安裝並複製至 SQL Developer 內。  

{% img /images/posts/PLSQLCopForSQLDeveloper/5.png %}

<br/>


安裝完後要分析程式碼只要在程式碼上按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中，選取 Check 選單選項。  

{% img /images/posts/PLSQLCopForSQLDeveloper/6.png %}

<br/>


PL/SQL Cop for SQL Developer 會將違背規則的地方給列出。  

{% img /images/posts/PLSQLCopForSQLDeveloper/7.png %}

<br/>


除了違背的規則列表外，PL/SQL Cop for SQL Developer 也提共了詳細的報表。  

{% img /images/posts/PLSQLCopForSQLDeveloper/8.png %}

<br/>


按下 Open 按鈕用瀏覽器來看，我們可以看到上半部這邊會列出複雜度、可維護性之類的指標。  

{% img /images/posts/PLSQLCopForSQLDeveloper/9.png %}

<br/>


下半部這邊會列出程式碼中違背的規則，以及違背的規則分布狀態。  

{% img /images/posts/PLSQLCopForSQLDeveloper/10.png %}

<br/>


最後一提，PL/SQL Cop for SQL Developer 安裝完後，SQL Developer 的 Perferences 視窗會多個 Trivadis PL/SQL Cop 的頁籤，如果要自訂哪些規則要檢查或是忽略，可以透過這邊設定。  

{% img /images/posts/PLSQLCopForSQLDeveloper/11.png %}

<br/>


Link
----
* [PL/SQL Cop for SQL Developer 1.0.11 | Philipp Salvisberg's Blog](https://www.salvis.com/blog/downloads/tvdcc-trivadis-plsql-sql-codechecker-for-sql-developer/)
