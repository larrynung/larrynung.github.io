---
layout: post
title: "Web API - Adding Request.IsLocal to ASP.NET Web API"
date: 2015-02-14 11:03:00
comments: true
tags: [Web API]
keywords: "Web API, IsLocal"
description: "Web API - Adding Request.IsLocal to ASP.NET Web API"
---

要判斷 Request 是否為本地 Request，在 ASP.NET 那邊因為 Request 是 HttpRequest 型態，內建有 IsLocal 方法，可以直接叫用判斷。  

<!-- More -->

<br/>


但在 Web API 就沒辦法那麼直接判斷，因為 APIController.Request 是 HttpRequestMessage 型態，沒有 IsLocal 方法可以直接叫用。要自行處理這樣的判斷可以查閱 Request 內的 MS_IsLocal Property 值，這邊國外的網友已經有現成寫好的擴充方法：  

{% codeblock lang:c# %} 
public static class HttpRequestMessageExtensions
{
   public static bool IsLocal(this HttpRequestMessage request)
   {
      var localFlag = request.Properties["MS_IsLocal"] as Lazy<bool>;
      return localFlag != null && localFlag.Value;
   }
}
{% endcodeblock %}

<br/>


放進專案中直接使用即可：  

{% codeblock lang:c# %} 
public HttpResponseMessage Get()
{
    if (Request.IsLocal()) {
        //do stuff
    }
}
{% endcodeblock %}

<br/>


Link
----
* [Adding Request.IsLocal to ASP.NET Web API StrathWeb](http://www.strathweb.com/2013/01/adding-request-islocal-to-asp-net-web-api/)
* [How to filter local requests in asp.net web api? - Stack Overflow](http://stackoverflow.com/questions/11849501/how-to-filter-local-requests-in-asp-net-web-api)
