---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 14 - Never overload data structure usages"
date: 2015-11-27 05:47:00
comments: true
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
description: "PL/SQL &amp; SQL CODING GUIDELINE 14 - Never overload data structure usages"
---

條款十四是說不要去覆寫變數。

<!-- More -->

<br/>


像是下面這樣外層與內層宣告了一樣名稱的變數，是不建議的寫法。 

```psql
<<main>> 
DECLARE 
	 v_str VARCHAR2(30); 
BEGIN 
	<<sub>> 
	DECLARE 
		 v_str VARCHAR2(4000) ; 
	BEGIN 
		…
	END sub; 
END main;
```

<br/>


建議使用上還是應該要將變數名稱錯開。  
