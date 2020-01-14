---
title: gRPC - Custom error over RpcException
date: 2020-01-14 07:57:17
tags: [gRPC]
---

在做系統時，免不了可能會要定義自己的狀態碼供判斷系統的問題。在 gRPC 下，我們可能會為 Message 增加 StatusCode 這樣的欄位做傳遞與判讀。

<!-- More -->

</br>

這樣的做法在一般的呼叫方式並無問題，但是在用 Streaming 傳達多個小 Message 時，使用上就會有點奇怪。  

</br>


這邊筆者試著透過 gRPC 本身的例外機制嘗試解決這樣的問題。  

</br>


先造一個自定義的例外，支援帶入 StatusCode，這邊筆者先簡單的用字串型態來做 StatusCode 的定義，實際運用時改用列舉會比較好。  

</br>


Server 端透過自定義的例外拋出例外。  

```c#
using System.Threading.Tasks;
using Greet;
using Grpc.Core;


namespace GrpcService_CSharp1
{
    public class GreeterService : Greeter.GreeterBase
    {
        public override Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
        {
          throw new MyException("ERROR2020");
        }
    }
}
```

{% asset_img 1.png %}

</br>


Server 端掛載攔截器處理例外，將例外轉為 RpcException 拋出，gRPC 支援的狀態碼較少所以筆者拿 StatusCode.Internal 狀態碼來用，Detail 這邊就帶我們自定義的狀態碼，若有額外資訊要帶入可放在 MetaData。  

```c#
using System;
using System.Threading.Tasks;
using Grpc.Core;
using Grpc.Core.Interceptors;


namespace GrpcService_CSharp1
{
    public class ExceptionInterceptor: Interceptor
    {
        public override async Task<TResponse> UnaryServerHandler<TRequest, TResponse>(TRequest request,
            ServerCallContext context,
            UnaryServerMethod<TRequest, TResponse> continuation)
        {
            try
            {
                return await base.UnaryServerHandler(request, context, continuation);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());


                if (e is RpcException)
                    throw;


                var myException = e as MyException ?? new MyException("ERROR9999");

                var rpcException = new RpcException(new Status(StatusCode.Internal, myException.StatusCode), new Metadata
                {
                    {nameof(request), request.ToString()}
                });

                throw rpcException;
            }
        }
    }
}
```

{% asset_img 2.png %}

</br>


實際運行，Client 會確實拋出例外，Trailers 內也會收到 Server 端透過 MetaData 帶來的額外資訊。  

{% asset_img 3.png %}

</br>


Link
====
* [Enum StatusCode](csharp/api/Grpc.Core.StatusCode.html)
