---
layout: post
title: "ASP.NET - Config session timeout"
date: 2014-03-21 23:49:00
comments: true
tags: 
keywords: "ASP.NET, Session, Timeout, Web.Config"
description: "ASP.NET - Config session timeout"
---

ASP.Net Website 若未做任何的設定，預設的 Timeout 時間為 20 分鐘。有時我們需要對此做些調整，可能是設定短ㄧ點的值方便做些測試，或是系統本身就是需要設定不一樣的 Timeout 值。  

<!-- More -->

若有調整的需要，可開啟 Web.config ， 在 system.web element 內加入 sessionState tag ，並指定 timeout 的值。像是下面這樣：  

{% codeblock lang:xml %}
<configuration>
    <system.web>
        <sessionState mode="InProc" cookieless="true" timeout="１" /> 
    </system.web>
</configuration>
{% endcodeblock %}

timeout 值的設定以分鐘為單位，最大上限值為 525,600 分鐘 (1 年) 。

<br/>

Link
----
* [sessionState 項目 (ASP.NET 設定結構描述)](http://msdn.microsoft.com/zh-tw/library/h6bb9cz9(v=vs.85).aspx)
