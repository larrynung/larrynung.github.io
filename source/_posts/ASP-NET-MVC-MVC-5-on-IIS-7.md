---
title: ASP.NET MVC - MVC 5 on IIS 7
date: 2016-07-29 23:39:54
tags: [ASP.NET MVC]
---

在 IIS 7 使用 ASP.NET MVC 5，Routing 功能會無法正常運作，會看到 403 或是 404 頁面。  

<!-- More -->

{% asset_img 1.png %}

<br/>


這邊可以在 Web.Config 的 modules 這邊加上 `runAllManagedModulesForAllRequests="true"` 設定，並為網站加上 `UrlRoutingModule-4.0` 模組。  

{% codeblock lang:objc %}
...
  <system.webServer>
    <modules runAllManagedModulesForAllRequests="true">
      ...
      <remove name="UrlRoutingModule-4.0"></remove>
      <add name="UrlRoutingModule-4.0" type="System.Web.Routing.UrlRoutingModule" preCondition=""></add>
    </modules>
...
```

<br/>


沒意外的話就會運作正常了。  

{% asset_img 2.png %}

<br/>


Link
----
* [MVC 5 on Windows Server 2008/IIS 7](http://cdonner.com/mvc-5-on-windows-server-2008iis-7.htm)
