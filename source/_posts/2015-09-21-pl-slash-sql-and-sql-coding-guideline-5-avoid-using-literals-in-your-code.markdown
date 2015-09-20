---
layout: post
title: "PL/SQL &amp; SQL CODING GUIDELINE 5 - Avoid using literals in your code"
date: 2015-09-21 00:17
comments: true
categories: 
keywords: 
description: "PL/SQL &amp; SQL CODING GUIDELINE 5 - Avoid using literals in your code"
---

條款五，避免在程式中直接使用字串。  

<!-- More -->

<br/>


像是下面這樣的程式：

{% codeblock lang:psql %}
SET SERVEROUTPUT ON
Begin
    DBMS_OUTPUT.put_line('Root Account:' || 'Admin');
End;
{% endcodeblock %}

<br/>


可以像下面這樣改寫，建立一個 Package 統一存放常數字串，呼叫端改透過 Package 叫用。  

{% codeblock lang:psql %}
SET SERVEROUTPUT ON
CREATE OR REPLACE PACKAGE CONST
IS
    ROOT_ACCOUNT CONSTANT varchar(50) := 'Admin';
END CONST;
/

Begin
    DBMS_OUTPUT.put_line('Root Account:' || CONST.ROOT_ACCOUNT);
End;
{% endcodeblock %}

這樣常數字串的宣告會集中在 Package 內，修改上也比較方便。  
