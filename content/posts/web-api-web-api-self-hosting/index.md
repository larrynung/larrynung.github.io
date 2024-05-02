---
title: "Web API - Web API Self Hosting"
date: "2014-04-14 23:24:00"
description: "Web API - Web API Self Hosting"
tags: [Web API ]
---


要 Self Hosting Web API，首先需要安裝 Microsoft.AspNet.WebApi.SelfHost 套件。  

<!-- More -->

建立 HttpSelfHostConfiguration 並指定要監聽的位置。 

```c#
var config =new HttpSelfHostConfiguration("http://localhost:32767");
```

<br/>


設定 HttpSelfHostConfiguration，像是 URL Routing 資訊。 

```c#
config.Routes.MapHttpRoute("API","{controller}/{action}/{id}",
new{ id =RouteParameter.Optional });
```

<Br/>


如果要被 Host 的 Web API 在其它的組件，這邊也可建立一個實作 IAssembliesResolver 的 SelfHostAssemblyResolve 類型。  

```c#
    public class SelfHostAssemblyResolver : IAssembliesResolver
    {
        #region  Properties
        /// <summary>
        /// Gets the path.
        /// </summary>
        /// <value>
        /// The path.
        /// </value>
        public string Path { get; private set ; }
        #endregion  Properties


        #region  Constructors
        /// <summary>
        /// Initializes a new instance of the <see cref="SelfHostAssemblyResolver"/> class.
        /// </summary>
        /// <param name="path"> The path.</param>
        public SelfHostAssemblyResolver(string path)
        {
            this.Path = path;
        }
        #endregion  Constructors


        #region  Methods
        /// <summary>
        /// Returns a list of assemblies available for the application.
        /// </summary>
        /// <returns>
        /// An &lt;see cref="T:System.Collections.Generic.ICollection`1" /&gt; of assemblies.
        /// </returns>
        public ICollection <Assembly> GetAssemblies()
        {
            List<Assembly > assemblies = new List<Assembly >();


            assemblies.Add( Assembly.LoadFrom(Path));


            return assemblies;
        }
        #endregion  Methods
    }
```

<br/>


帶入外部組件位置建立對應的物件，然後將服務中的 IAssembliesResolver 用該物件取代即可。

```c#
config.Services.Replace(typeof(IAssembliesResolver),new SelfHostAssemblyResolver("AgileSlot.API.dll"));
```

<br/>


接著建立 HttpSelfHostServer，建立時帶入前面所建立的 HttpSelfHostConfiguration

<br/>


當開始要使用服務時，叫用 HttpSelfHostServer.OpenAsync 啟動 Web API 服務

```c#
httpServer.OpenAsync();
```

<br/>


當不在需要服務時，叫用 HttpSelfHostServer.CloseAsync 中止 Web API 服務

```c#
httpServer.CloseAsync();
```

<br/>


整個程式寫起來會像下面這樣：

```c#
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
```

<br/>


Link
----
* [Self-Host Web API 1 (C#) : The Official Microsoft ASP.NET Site](http://www.asp.net/web-api/overview/hosting-aspnet-web-api/self-host-a-web-api)
