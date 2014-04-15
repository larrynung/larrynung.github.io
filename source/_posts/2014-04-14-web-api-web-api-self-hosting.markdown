---
layout: post
title: "Web API - Web API Self Hosting"
date: 2014-04-14 23:24
comments: true
categories: [Web API] 
keywords: "Web API, Self Hosting"
description: "Web API - Web API Self Hosting"
---

要 Self Hosting Web API，首先需要安裝 Microsoft.AspNet.WebApi.SelfHost 套件。  

<!-- More -->

建立 HttpSelfHostConfiguration 並指定要監聽的位置。 

{% codeblock lang:c# %}
var config =new HttpSelfHostConfiguration("http://localhost:32767");
{% endcodeblock %}

設定 HttpSelfHostConfiguration，像是 URL Routing 資訊。 

{% codeblock lang:c# %}
config.Routes.MapHttpRoute("API","{controller}/{action}/{id}",
new{ id =RouteParameter.Optional });
{% endcodeblock %}

如果要被 Host 的 Web API 在其它的組件，這邊也可建立 SelfHostAssemblyResolve，然後取代 IAssembliesResolver 類型的服務。  

{% codeblock lang:c# %}
config.Services.Replace(typeof(IAssembliesResolver),newSelfHostAssemblyResolver("AgileSlot.API.dll"));
{% endcodeblock %}

接著建立 HttpSelfHostServer，建立時帶入前面所建立的 HttpSelfHostConfiguration

當開始要使用服務時，叫用 HttpSelfHostServer.OpenAsync 啟動 WCF 服務

{% codeblock lang:c# %}
httpServer.OpenAsync();
{% endcodeblock %}

當不在需要服務時，叫用 HttpSelfHostServer.CloseAsync 中止 WCF 服務

{% codeblock lang:c# %}
httpServer.CloseAsync();
{% endcodeblock %}

整個程式寫起來會像下面這樣：

{% codeblock lang:c# %}
var config =new HttpSelfHostConfiguration("http://localhost:32767");
config.Routes.MapHttpRoute("API","{controller}/{action}/{id}",
new{ id =RouteParameter.Optional });

config.Services.Replace(typeof(IAssembliesResolver),newSelfHostAssemblyResolver("AgileSlot.API.dll"));

using(var httpServer =new HttpSelfHostServer(config))
{
    httpServer.OpenAsync().Wait();
    Console.WriteLine("Web API host started...");
    string line =null;
    do
    {
        line =Console.ReadLine();
    }
    while(line !="exit");
    httpServer.CloseAsync().Wait();
}
{% endcodeblock %}

<br/>

Link
----
* [Self-Host Web API 1 (C#) : The Official Microsoft ASP.NET Site](http://www.asp.net/web-api/overview/hosting-aspnet-web-api/self-host-a-web-api)
