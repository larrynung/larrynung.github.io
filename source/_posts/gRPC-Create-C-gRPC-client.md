---
title: 'gRPC - Create C# gRPC client'
date: 2019-04-18 14:24:33
tags: [gRPC]
---

要建立 gRPC 的 client，要先將 proto 檔產生對應的程式碼，建置成組件後在 Client 的專案將它加入參考使用。  

<!-- More -->

{% asset_img 1.png %}

<br/>


然後帶入 Server 位置建立 Channel 物件。

```C#
...
var channel = new Channel($"{host}:{port}", ChannelCredentials.Insecure);
...
```

<br/>


接著帶入 Channel 建立 Service 的 Client 物件。  

```C#
...
var client = new HelloService.HelloServiceClient(channel);
...
```

<br/>


透過 Service 的 Client 物件調用對應的方法。  

```C#
...
Console.WriteLine(client.SayHello(new HelloRequest()
{
    ...
}));
...
```

<br/>


最後在不使用時將 Channel 關閉即可。  

```C#
...
channel.ShutdownAsync();
...
```

<br/>


程式寫起來會像下面這樣：  

```C#
using System;
using Grpc.Core;
using GRPC.Message;

namespace GRPC.Client
{
    class Program
    {
        static void Main(string[] args)
        {
            var channel = new Channel("127.0.0.1:8888", ChannelCredentials.Insecure);
            var client = new HelloService.HelloServiceClient(channel);

            Console.WriteLine(client.SayHello(new HelloRequest()
            {
                Name = "Larry"
            }));
            
            channel.ShutdownAsync().Wait();
        }
    }
}
```

<br/>


運行起來 Client 就會透過 rpc 去跟 Server 調用，並將訊息回傳。  

{% asset_img 2.png %}
