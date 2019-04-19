---
title: gRPC - gRPC on ASP.NET Core 3.0
date: 2019-04-19 16:18:04
tags: [gRPC]
---

在 .NET Core 3.0 後，我們可透過 gRPC Service 範本建立方案或是專案。  

<!-- More -->

<br/>


像是筆者這邊直接透過範本建立一個 gRPC 方案。  

{% asset_img 1.png %}

<br/>


{% asset_img 2.png %}

<br/>


方案建立完會看到內含 Server 與 Client 兩個專案，需參考的套件以及 Proto 檔的編譯設定都已經設好了。  

{% asset_img 3.png %}

<br/>


{% asset_img 4.png %}

<br/>


另外是 .NET Core 3.0 的 gRPC Service 已經被整進去了，只要在 Startup.cs 中的 ConfigServices 將 gRPC 服務開啟。  

```C#
...
public void ConfigureServices(IServiceCollection services)
{
    services.AddGrpc();
}
...
```

<br/>


並設定 gRPC 服務對應的處理類別。

```C#
...
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    ...
    app.UseRouting(routes => { routes.MapGrpcService<GreeterService>(); });
}
...
```

<br/>


這邊範本也都幫我們設定好了。  

{% asset_img 5.png %}

<br/>


只要運行起來就可以看到 gRPC 正常的在運作。  

{% asset_img 6.png %}

<br/>


{% asset_img 7.png %}

<br/>


{% asset_img 8.png %}

<br/>


{% asset_img 9.png %}

<br/>


Link
----
* [gRPC services with ASP.NET Core | Microsoft Docs](https://docs.microsoft.com/en-us/aspnet/core/grpc/aspnetcore?view=aspnetcore-3.0&tabs=visual-studio)
* [Tutorial: Get started with gRPC in ASP.NET Core | Microsoft Docs](https://docs.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-3.0&tabs=visual-studio)
* [Tutorial: Create a .NET Core gRPC client | Microsoft Docs](https://docs.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-client?view=aspnetcore-3.0&tabs=visual-studio)
