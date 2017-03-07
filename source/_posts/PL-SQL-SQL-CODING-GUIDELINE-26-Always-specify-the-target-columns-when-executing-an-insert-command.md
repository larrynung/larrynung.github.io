---
title: >-
  PL/SQL & SQL CODING GUIDELINE 26 - Always specify the target columns when
  executing an insert command
date: 2016-06-07 00:07:30
tags: [PL/SQL, PL/SQL and SQL Coding Guidelines]
keywords: "PL/SQL"
---

條款二十六，運行插入命令時總是指定塞入的欄位。  

<!-- More -->

<br/>


像是下面這樣不指定要塞入欄位的寫法，塞入的動作會對資料表欄位的順序有所依賴，當欄位順序一有變動就會產生不如預期的結果，而且問題發生時不是很容易可以被偵測出來。   

{% codeblock lang:sql %}
INSERT INTO 
    messages 
VALUES 
    (l_mess_no ,l_mess_typ ,l_mess_text );
{% endcodeblock %}

<br/>


如果在塞入時明確的指定塞入的欄位，就能避開這樣的問題。  

{% codeblock lang:sql %}
INSERT INTO 
    messages 
    (mess_no ,mess_typ ,mess_text ) 
VALUES 
    (l_mess_no ,l_mess_typ ,l_mess_text );
{% endcodeblock %}
