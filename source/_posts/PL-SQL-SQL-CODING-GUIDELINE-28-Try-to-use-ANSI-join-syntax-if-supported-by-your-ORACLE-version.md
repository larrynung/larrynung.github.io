---
title: >-
  PL/SQL & SQL CODING GUIDELINE 28 - Try to use ANSI-join syntax, if supported
  by your ORACLE version
date: 2016-06-07 23:58:35
tags: [PL/SQL]
keywords: "PL/SQL"
---

條款二十八，如果 Oracle 版本支援，請使用 ANSI-Join。  

<!-- More -->

<br/>


因為 ANSI-Join 使用上比較沒有那麼多限制，支援 outer join，且能將 join 條件與 query 條件分開。


使用上會像是下面這樣：  

{% codeblock lang:sql %}
SELECT 
    a.pid ,a.name ,a.birthday ,b.country 
FROM person a JOIN country b ON (a.cid = b.cid) 
WHERE …
{% endcodeblock %}
