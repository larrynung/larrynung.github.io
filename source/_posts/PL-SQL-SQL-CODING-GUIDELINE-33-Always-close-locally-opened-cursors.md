---
title: PL/SQL & SQL CODING GUIDELINE 33 - Always close locally opened cursors
date: 2016-08-13 07:42:55
tags:
---

條款三十三，總是關閉開啟的游標。  

<!-- More -->

<br/>


像是下面這樣將游標開啟後並未揪游標關閉，使用的資源不會自動釋放。  

{% codeblock lang:sql %}
CREATE PROCEDURE not_close_cursor (out_count OUT INTEGER) 
AS 
    CURSOR c1 
        IS 
            SELECT COUNT (*) 
                FROM all_users; 
BEGIN 
    out_count := 0; 
    OPEN c1; 
    FETCH c1 
        INTO out_count; 
END not_close_cursor; 
...
{% endcodeblock %}

<br/>


應該要自己將游標在適當的時機點關閉，使用的資源才會被釋放。  

{% codeblock lang:sql %}
CREATE PROCEDURE close_cursor (out_count OUT INTEGER) 
AS 
    CURSOR c1 
    IS 
        SELECT COUNT (*) 
            FROM all_users; 
BEGIN 
    out_count := 0; 
    OPEN c1; 
    FETCH c1 
        INTO out_count; 
    CLOSE c1 
END close_cursor;
{% endcodeblock %}

