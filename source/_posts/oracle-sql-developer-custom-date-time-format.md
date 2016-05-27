---
layout: post
title: "Oracle SQL Developer - Custom date time format"
date: 2016-05-13 23:37:00
comments: true
categories: [Oracle SQL Developer]
keywords: "Oracle"
description: "Oracle SQL Developer - Custom date time format"
---

Oracle SQL Developer 預設 Date Format 設定為 DD-MON-RR，顯示上是不含時間的部分。  
<!-- More -->

{% img /images/posts/OracleSQLDeveloperCustomDateFormat/1.png %}

<br/>


若要顯示時間的部分，我們需點選 [Tools | Preference] 主選單選項，將開啟的 Preferences 對話框切至 [Database | NLS] 頁面，在 Date Format 這邊將時間的部分設定上去。  
{% img /images/posts/OracleSQLDeveloperCustomDateFormat/2.png %}

<br/>


像是這邊筆者是將之設定成 YYYY-MM-DD HH24:MI:SS 這樣。  

<br/>

Link
----
* [How can I set a custom date time format in Oracle SQL Developer? - Stack Overflow](http://stackoverflow.com/questions/8134493/how-can-i-set-a-custom-date-time-format-in-oracle-sql-developer)
