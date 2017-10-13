---
title: SQLite - Install SQLite on Windows
date: 2017-10-12 22:21:29
tags:
---

要在 Windwos 下使用 SQLite，可至 [SQLite Home Page](https://www.sqlite.org/) 的下載頁面。  

<!-- More -->

{% asset_img 1.png %}

<br/>


下載 Windows 的 binary。  

{% asset_img 2.png %}

<br/>


將下載的壓縮包解壓縮。  

{% asset_img 3.png %}

<br/>


會看到幾個執行檔，我們主要要用的是 sqlite3.exe 這個執行檔。  

{% asset_img 4.png %}

<br/>


可以用 -help 查閱使用方式。

    sqlite3 -help

<br/>


可以用 -version 查閱版本。  

    sqlite3 -version

{% asset_img 5.png %}

<br/>


可以直接調用做一連串的 SQL 操作。  

    sqlite3

{% asset_img 6.png %}

<br/>


也可以直接對特定 SQLite DB 調用單一 SQL 操作。  

    sqlite3 [SQLiteDB] [SQL]

{% asset_img 7.png %}

<br/>


Link
----
* [SQLite Home Page](https://www.sqlite.org/)
* [SQLite Installation](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm)
