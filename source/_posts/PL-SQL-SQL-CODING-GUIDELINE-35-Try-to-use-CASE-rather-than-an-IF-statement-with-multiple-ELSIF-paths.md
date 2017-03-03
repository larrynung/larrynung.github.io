---
title: >-
  PL/SQL & SQL CODING GUIDELINE 35 - Try to use CASE rather than an IF statement
  with multiple ELSIF paths
date: 2016-08-24 13:31:51
tags: [PL/SQL]
keywords: "PL/SQL"
---

條款三十五，嘗試使用 CASE 語句取代多行 ELSIF 語句。  

<!-- More -->

<br/>


像是下面這樣的語法，使用了過多的 ELSIF，可讀性沒有那麼好。  

{% codeblock lang:sql %}
IF l_color = 'red' 
THEN 
    ... 
ELSIF l_color = 'blue' 
THEN 
    ... 
ELSIF l_color = 'black' 
THEN 
    ...
{% endcodeblock %}

<br/>


若換用 CASE 來撰寫，可讀性會好很多。  

{% codeblock lang:sql %}	
CASE l_color 
    WHEN 'red' THEN ... 
    WHEN 'blue' THEN ... 
    WHEN 'black' THEN ... 
END
{% endcodeblock %}