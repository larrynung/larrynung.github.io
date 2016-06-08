---
title: >-
  PL/SQL & SQL CODING GUIDELINE 29 - Try to use anchored records as targets for
  your cursors
date: 2016-06-08 23:33:51
tags:
---

條款二十九，Try to use anchored records as targets for your cursors。   

<!-- More -->

<br/>


像是下面這邊的程式就宣告了幾個變數，開啟 Cursor 後遍巡，將資料塞到變數後再進一步處理。  

{% codeblock lang:c# %}
DECLARE 
    CURSOR c_user IS 
        SELECT user_id, firstname, lastname 
        FROM user; 
    l_user_id user.user_id%TYPE; 
    l_firstname user.firstname%TYPE; 
    l_lastname user.lastname%TYPE; 
BEGIN 
    OPEN c_user; 
    FETCH c_user INTO l_user_id, l_firstname, l_lastname; 
    WHILE c_user%FOUND 
    LOOP 
        FETCH c_user INTO l_user_id, l_firstname, l_lastname; 
    END LOOP; 
    CLOSE c_user; 
END;
{% endcodeblock %}

<br/>


如果改用 cursor-anchored records 去實作，就可以省去一些不必要的變數宣告。  

{% codeblock lang:sql %}
DECLARE 
    CURSOR c_user IS 
        SELECT user_id, firstname, lastname 
        FROM user; 
    r_user c_user%ROWTYPE; 
BEGIN 
    OPEN c_user; 
    FETCH c_user INTO r_user; 
    <<process_user>> 
    WHILE c_user%FOUND 
    LOOP 
        FETCH c_user INTO r_user; 
    END LOOP process_user; 
    CLOSE c_user; 
END;
{% endcodeblock %}
