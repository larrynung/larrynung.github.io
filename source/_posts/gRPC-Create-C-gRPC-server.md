---
title: 'gRPC - Create C# gRPC server'
date: 2019-04-18 05:39:37
tags: [gRPC, CSharp]
---

要建立 gRPC 的 Server，先要用 proto 檔產生對應的 Service 類別。  

<!-- More -->

<br/>


像是這邊筆者用 proto 定義了一個 Service。  

```
syntax = "proto3";

import "message.proto";

package GRPC.Message;

service HelloService {
    rpc SayHello (HelloRequest) returns (HelloResponse) {}
}
```

<br/>


該 Service 會使用到的 Message 定義如下。  

```
syntax = "proto3";

package GRPC.Message;


message HelloRequest {  
    string name = 1;
}

message HelloResponse {  
    string name = 1;
}
```

<br/>


在產生完程式碼後在 Server 的專案將它加入參考使用。  

{% asset_img 1.png %}

<br/>


然後開始實作 Service。

<br/>


繼承產出的 Service 基底類別。  

```C#
...
public class HelloServiceImpl:HelloService.HelloServiceBase
...
```

並覆寫該服務的方法即可。  

```C#
...
public override Task<HelloResponse> SayHello(HelloRequest request, ServerCallContext context)
{
    ...
}
...
```

<br/>


程式寫起來會像下面這樣 (這邊筆者只是簡單的將調用時送進來的人名做些加工回傳而已)：    

```C#
using System.Threading.Tasks;
using Grpc.Core;
using GRPC.Message;

public class HelloServiceImpl:HelloService.HelloServiceBase
{
    public override Task<HelloResponse> SayHello(HelloRequest request, ServerCallContext context)
    {
        return Task.FromResult(new HelloResponse
        {
            Name = "Hello~" + request.Name
        });
    }
}
```

<br/>


Service 實作完接著要實作 Server 的部分。  

<br/>


建立 Grpc.Core.Server 實體。

```C#
...
var server = new Grpc.Core.Server();
...
```

<br/>


指定 Service 要用哪個類別去處理。  

```C#
...
server.Services.Add(Message.HelloService.BindService(new HelloServiceImpl()));
...
```

<br/>


指定 Server 的位置與 Port。  

```C#
...
server.Ports.Add(new ServerPort(host, port, ServerCredentials.Insecure));
...
```

啟動 Server。  

```C#
...
server.Start();
...
```

等待終止訊號，最後停止 Server 即可。

```C#
...
server.ShutdownAsync();
...
```  

<br/>


程式寫起來會像下面這樣：  

```C#
using System;
using Grpc.Core;

namespace GRPC.Server
{
    class Program
    {
        static void Main(string[] args)
        {
            var host = "127.0.0.1";
            var port = 8888;

            var server = new Grpc.Core.Server
            {
                Services = {  Message.HelloService.BindService(new HelloServiceImpl())},
                Ports =
                {
                    new ServerPort(host, port, ServerCredentials.Insecure)
                }
            };

            server.Start();

            Console.WriteLine("GRPC server listening on port " + port);
            Console.WriteLine("Press any key to stop the server...");
            
            Console.ReadKey();

            server.ShutdownAsync().Wait();
        }
    }
}
```

<br/>


運行起來就可以提供 gRPC 的服務了。  

{% asset_img 2.png %}
