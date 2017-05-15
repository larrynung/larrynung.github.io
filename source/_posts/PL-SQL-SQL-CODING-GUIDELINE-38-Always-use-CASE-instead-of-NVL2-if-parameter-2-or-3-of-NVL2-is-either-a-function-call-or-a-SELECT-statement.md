---
title: >-
  PL/SQL & SQL CODING GUIDELINE 38 - Always use CASE instead of NVL2 if
  parameter 2 or 3 of NVL2 is either a function call or a SELECT statement
date: 2016-09-05 13:46:16
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
---

條款三十八，如果 NVL 第二或第三個參數是 function 呼叫或是 select 語句，使用 CASE 取代 NVL2。

<!-- More -->

<br/>


這是因為 NVL2 會先把每個可能的結果都先取出，儘管是根本不會出的結果，所以這樣會有不必要的 overhead。  

```psql
SELECT NVL2(dummy, function_call(), function_call()) 
FROM dual;
```

<br/>


建議的做法是用 CASE 取代 NVL2，以避開這樣的問題。  

```psql
SELECT CASE 
    WHEN dummy IS NULL THEN function_call() 
    ELSE function_call()
END 
FROM dual;
```