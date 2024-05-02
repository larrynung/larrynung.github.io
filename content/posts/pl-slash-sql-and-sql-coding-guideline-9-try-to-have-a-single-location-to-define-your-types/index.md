---
title: "PL/SQL amp; SQL CODING GUIDELINE 9 - Try to have a single location to define your types"
date: "2015-11-23 05:45:00"
description: "PL/SQL &amp; SQL CODING GUIDELINE 9 - Try to have a single location to define your types"
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
---


條款九主要是在描述型態的定義要集中一處放置，以 Oracle 來說型態的定義可以放置在 DB 的 Types 下。  

<!-- More -->

{% img /images/posts/PLSQLCopRule9/1.png %}

<br/>



也可以建造個 Package 集中放置，這邊建議是挑選一個地方放置即可，避免有些型態的宣告放置在 Types 下，而有的在 Package 下。  

<br/>


選用上要注意 Oracle 內的型態有的只能在 Database 下使用，無法在 Package 下使用，像是 Object 型態。  
