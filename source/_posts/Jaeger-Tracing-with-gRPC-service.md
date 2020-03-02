---
title: Jaeger - Tracing with gRPC service
date: 2020-02-24 08:32:03
tags: [Jaeger, gRPC]
---

要使用 Jaeger 追蹤 gRPC service 程式，可先加入 Jaeger 與 OpenTracing.Contrib.Grpc 套件。  

<!-- More -->

```xml
...
    <PackageReference Include="Jaeger" Version="0.3.6" />
    <PackageReference Include="OpenTracing.Contrib.Grpc" Version="0.2.0" />
  </ItemGroup>
...
```

{% asset_img 1.png %}

<br>


修改 Startup.ConfigureServices，加入 Jaeger tracer、註冊 GlobalTracer、設定 gRPC 攔截器。  

```c#
...
services.AddGrpc(options =>
{
    var serviceName = AppDomain.CurrentDomain.FriendlyName;
    var tracer = new Tracer.Builder(serviceName)
        .WithSampler(new ConstSampler(true))
        .Build();

    GlobalTracer.Register(tracer);

    services.AddSingleton<ITracer>(tracer);

    var interceptors = options.Interceptors;
    interceptors.Add<ServerTracingInterceptor>(tracer);

    ...
});
...
```

<br>


實際運行程式。  

{% asset_img 2.png %}

<br>


選取 Service 與 Operator 下去查詢。  

{% asset_img 3.png %}

<br>


可看到找到的 Trace，上半部可看到時間與耗時的分佈，下半部就是簡易的列表，可看出 Trace 名稱、識別碼、是什麼時間點觸發的、耗時多久、有多少 Span。  

{% asset_img 4.png %}

<br>


點選感興趣的 Trace，會進入 Trace 細部資訊頁面，會將 Trace 及其組成的 Span 以圖形的方式呈現，便於找到相對耗時的操作。  

{% asset_img 5.png %}

<br>


展開 Span 可看到 Span 的 Tag 這些細部的資訊。  

{% asset_img 6.png %}
