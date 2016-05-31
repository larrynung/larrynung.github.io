---
layout: post
title: "T4MVC - Add Timestamp To Static Links"
date: 2014-07-24 22:55:00
comments: true
tags: [T4MVC, T4]
keywords: "T4MVC, T4"
description: "T4MVC - Add Timestamp To Static Links"
---

T4MVC 除了解決 ASP.NET MVC Magic String 的問題外，還能解決常見的網頁 Cache 問題。 

<!--More -->

只要在 T4MVC.tt.settings.xml 設定檔中將 AddTimestampToStaticLinks 設為 True 就可以了。

{% codeblock lang:xml %}
...
<AddTimestampToStaticLinks>True</AddTimestampToStaticLinks>
...
{% endcodeblock %}

這樣使用 T4MVC 去取用靜態檔案的位置時，T4MVC 就會幫我們在網址後面依照檔案的修改時間去附加雜湊值，避免前端快取。
