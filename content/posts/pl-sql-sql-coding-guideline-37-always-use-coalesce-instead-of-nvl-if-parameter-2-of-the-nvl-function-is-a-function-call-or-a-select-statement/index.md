---
title: ">-"
date: "2016-08-28 00:07:58"
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
---


條款三十七，如果 NVL 第二個參數是 function 呼叫或是 select 語句，使用 COALESCE 取代 NVL。  

<!-- More -->

<br/>


這是因為 NVL 會先把每個可能的結果都先取出，儘管是根本不會出的結果，所以這樣會有不必要的 overhead。  

```psql
SELECT NVL(dummy, function_call()) 
FROM dual;
```

<br/>


建議的做法是用 COALESCE 取代 NVL，以避開這樣的問題。  

```psql
SELECT COALESCE(dummy, function_call()) 
FROM dual;
```
