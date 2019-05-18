---
title: "gRPC - Setup service options with ASP.NET Core"
date: 2019-05-18 03:04:45
tags: [gRPC]
---

在 ASP.NET Core 支援設定的 gRPC service option 有:  

<!-- More -->

| Option | Default | Description |
|:------:|:-------:|:-----------:|
| SendMaxMessageSize | null | 最大訊息大小可以從伺服器傳送的位元組數。 嘗試傳送的訊息長度超過設定的最大訊息大小會導致例外狀況。 |
| ReceiveMaxMessageSize | 4 MB | 最大訊息大小可以由伺服器接收的位元組數。 如果伺服器收到的訊息超過此限制，它會擲回例外狀況。 增加此值可讓伺服器接收較大的訊息，但可能會造成負面影響記憶體耗用量。 |
| EnableDetailedErrors | false | 如果true詳細服務方法擲回例外狀況時，將會傳回給用戶端的例外狀況訊息。 預設為 false。 這個設定設為true可能會導致洩漏機密資訊。 |

<br/>


可在 Startup 的 ConfigureServices 內透過 services.AddGrpc 針對所有 Service 下去設定。  

```C#
...
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        ...
        services.AddGrpc(options =>
        {
            options.ReceiveMaxMessageSize = receiveMsgLimit;
            options.SendMaxMessageSize = sendMsgLimit;
        });
        ...
    }
   ...
}
```

{% asset_img 1.png %}

<br/>


也可以透過 services.AddGrpc().AddServiceOptions<T> 針對特定 Service 下去設定。  

```C#
...
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        ...
        services.AddGrpc().AddServiceOptions<GreeterService>(options =>
        {
            options.ReceiveMaxMessageSize = receiveMsgLimit;
            options.SendMaxMessageSize = sendMsgLimit;
        });
        ...
    }
   ...
}
```

{% asset_img 2.png %}

<br/>


這邊筆者為了測試效果特定將設定值調的極端的低，實際使用上請依使用情境下去調整。  

<br/>


Link
----
* [從 C 核心移轉的 gRPC 服務，ASP.NET core | Microsoft Docs](https://docs.microsoft.com/zh-tw/aspnet/core/grpc/migration?view=aspnetcore-3.0)
* [ASP.NET Core 組態 gRPC | Microsoft Docs](https://docs.microsoft.com/zh-tw/aspnet/core/grpc/configuration?view=aspnetcore-3.0)
