---
layout: post
title: "Web cache"
date: 2014-12-01 23:02:00
comments: true
categories: 
keywords: "Cache"
description: "Web cache"
---

Web Cache 是 ASP.NET 內建的 Cache 機制，這邊簡單的隨手紀錄一下。 

<!--More-->

<br/>
 

Cache 物件的可從 HttpContext 取得。  

{% codeblock lang:c# %}
var httpContext = HttpContext.Current ;
var cache = httpContext.Cache ;
{% endcodeblock %}

<br/>


Cache 物件取得後，我們可以透過 Add 或 Insert 將要快取的資料存入。這邊在帶入資料的同時，我們可以透過參數決定資料的存活週期，以及快取被清除時所要運行的 Callback。  

{% codeblock lang:c# %}
cache.Add (key, value, null , DateTime.Now.AddMilliseconds(cacheInterval), TimeSpan.Zero, CacheItemPriority.Normal, null);
{% endcodeblock %}

<br/>


取出時也只要帶入 Key 值即可。  

{% codeblock lang:c# %}
if (cache[key] != null )
    value = cache[key];
{% endcodeblock %}
              

Link
----
* [Cache 類別 (System.Web.Caching)](http://msdn.microsoft.com/zh-tw/library/System.Web.Caching.Cache(v=vs.80).aspx)
* [TIPS-ASP.NET Cache Mini Guide - 黑暗執行緒](http://blog.darkthread.net/post-2007-08-29-tips-asp-net-cache-mini-guide.aspx)
