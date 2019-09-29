---
title: gRPC - Streaming
date: 2019-09-27 07:22:36
tags: [gRPC]
---

gRPC 的 Streaming 可用來做大量資料的傳輸，不論是 Client 傳到 Service，或是 Service 回給 Client。  

<!-- More -->

</br>


使用上就是在 proto 檔用 stream 去定義要使用 Streaming 的地方，看是用在傳入還是回傳。  

```
...
service Greeter {
  ...
  rpc SayHellos (stream HelloRequest) returns (stream HelloReply) {}
}
...
```

</br>


然後 Service 與 Client 透過 IServerStreamWriter 寫資料、透過 IAsyncStreamReader 讀取資即可。  

</br>

以寫入來說，可透過迴圈搭配 WriteAsync() 將資料逐筆寫入，最後透過 CompleteAsync() 告知寫入完成。  

 ```c#
foreach (var item in data)                 
{
    await stream.WriteAsync(item);
}                                          
await stream.CompleteAsync();             
```

</br>


或是引用 Grpc.Core.Utils，直接透過 WriteAllAsync() 將所有資料寫入。  

```c#
...
await stream.WriteAllAsync(data);
...
```

</br>


以讀取來說，可用迴圈搭配 MoveNext() 移至下筆可用的資料，再用 Current 取出資料做處理。

```c#
using Grpc.Core;
...
while (await stream.MoveNext())      
{                                
    var data = stream.Current; 
    ...
}
...
```

</br>


或是引用 Grpc.Core.Utils，然後透過 ForEachAsync 直接用 Lambda 指定每筆資料所要做的處理。

```c#
using Grpc.Core;                            
using Grpc.Core.Utils;
...
await stream.ForEachAsync(item => ...);
...
```

</br>


抑或是直接透過 ToListAsync() 取得全部資料。

```c#
using Grpc.Core;                           
using Grpc.Core.Utils;
...
var data = await stream.ToListAsync<...>();
...
```

</br>


所以假設我們有個 proto 如下:  

```
syntax = "proto3";

package Greet;

// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
  rpc SayHellos (stream HelloRequest) returns (stream HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings.
message HelloReply {
  string message = 1;
}
```

{% asset_img 1.png %}

</br>


Service 這邊我們就可以像這樣實作:  

```c#
using System.Threading.Tasks;
using Greet;
using Grpc.Core;

namespace GrpcService_CSharp1
{
    public class GreeterService : Greeter.GreeterBase
    {
        public override async Task SayHellos(IAsyncStreamReader<HelloRequest> requestStream, IServerStreamWriter<HelloReply> responseStream, ServerCallContext context)
        {
            while (await requestStream.MoveNext())
            {
                var request = requestStream.Current;
                await responseStream.WriteAsync(new HelloReply
                {
                    Message = "Hello " + request.Name
                };
            }
        }

        public override Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
        {
            return Task.FromResult(new HelloReply
            {
                Message = "Hello " + request.Name
            });
        }
    }
}
```

{% asset_img 2.png %}

</br>


Client 這邊會像這樣:  

```c#
using System;
using System.Threading.Tasks;
using Greet;
using Grpc.Core;
using Grpc.Core.Utils;

namespace GrpcService_CSharp1
{
    public class Program
    {
        static async Task Main(string[] args)
        {
            // Include port of the gRPC server as an application argument
            var port = args.Length > 0 ? args[0] : "50051";

            var channel = new Channel("localhost:" + port, ChannelCredentials.Insecure);
            var client = new Greeter.GreeterClient(channel);

            var reply = await client.SayHelloAsync(new HelloRequest {Name = "GreeterClient"});
            Console.WriteLine("Greeting: " + reply.Message);

            var requests = new[]
            {
                new HelloRequest {Name = "Larry1"},
                new HelloRequest {Name = "Larry2"}
            };

            using (var call = client.SayHellos())
            {
                await call.RequestStream.WriteAllAsync(requests);

                await call.ResponseStream.ForEachAsync(item =>
                    Task.Run(() => Console.WriteLine("Greeting: " + item.Message)));
            }

            await channel.ShutdownAsync();

            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}
```

{% asset_img 3.png %}

</br>


Client 與 Service 就可以透過 Streaming 進行通訊。  

{% asset_img 4.png %}
