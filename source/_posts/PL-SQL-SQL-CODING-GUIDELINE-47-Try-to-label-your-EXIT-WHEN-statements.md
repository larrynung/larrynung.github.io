---
title: PL/SQL & SQL CODING GUIDELINE 47 - Try to label your EXIT WHEN statements
date: 2017-06-07 13:20:01
tags: [PL/SQL and SQL Coding Guidelines]
---

條款四十七，嘗試將 EXIT WHEN 搭配 label 使用。  

<!-- More -->

<br/>


像是下面這樣的程式，雖然使用了 EXIT WHEN 跳離迴圈，但是未搭配 label 使用，因此在巢狀迴圈下得一層一層的跳離。  

```psql
BEGIN 
  ...
  <<outerloop>> 
  LOOP 
    ...
    <<innerloop>> 
    LOOP 
      ...
      EXIT WHEN l_innerlp = co_exit_value; 
    END LOOP innerloop; 
	EXIT WHEN l_innerlp = co_exit_value;
  END LOOP outerloop; 
END;
```

<br/>


如果將 EXIT WHEN 搭配 label 使用可以直接在巢狀迴圈下跳離，這樣程式會比較簡短、清晰、且易於維護。  

```psql
BEGIN 
  ...
  <<outerloop>> 
  LOOP 
    ...
    <<innerloop>> 
    LOOP 
      ...
      EXIT outerloop WHEN l_innerlp = 3; 
    END LOOP innerloop; 
  END LOOP outerloop; 
END;
```