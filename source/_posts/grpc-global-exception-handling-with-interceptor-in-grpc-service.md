---
title: "gRPC - Global exception handling with interceptor in gRPC service"
date: 2019-11-27 07:26:13
tags: [gRPC]
---

要做 gRPC 的全域攔截，可以使用 gRPC interceptor 來做。  

<!-- More -->

</br>


建立一個 Interceptor 類別繼承自 gRPC 的 Interceptor，覆寫掉會用到的方法，像是 UnaryServerHandler，然後在內部調用基底的方法並用 try/catch 去攔截錯誤做對應的處理即可。  

</br>


像是下面這邊筆者實作了一個 Interceptor，希望能在錯誤發生時顯示錯誤，並回傳錯誤訊息。

```c#
using System;
using System.Threading.Tasks;
using Grpc.Core;
using Grpc.Core.Interceptors;
using Microsoft.Extensions.Logging;


namespace GrpcServiceInterceptor
{
    public class ExceptionInterceptor : Interceptor
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


                var obj = (TResponse) Activator.CreateInstance(typeof(TResponse));
                var prop = typeof(TResponse).GetProperty("Message");

                prop.SetValue(obj, e.Message, null);


                return obj;
            }
        }
    }
}
```

{% asset_img 1.png %}

</br>


Interceptor 寫好後要掛載進去。  

```c#
public class Startup
{
    // This method gets called by the runtime. Use this method to add services to the container.
    // For more information on how to configure your application, visit https://go.microsoft.com/fwlink/?LinkID=398940
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddGrpc(options =>
        {
            options.Interceptors.Add<ExceptionInterceptor>();
        });
    }
    …
}
```

{% asset_img 2.png %}

</br>


運行起來實際去調用 gRPC，當錯誤發生時會可看到 gRPC 仍舊正常回應，只是回應的內容是 Interceptor 攔截錯誤後回傳出去的。  

{% asset_img 3.png %}

</br>


攔截到的錯誤資訊也會正常的顯示。  

{% asset_img 4.png %}

</br>


透過 gRPC interceptor 我們可將錯誤集中處理，可以紀錄發生的錯誤，也可以轉成自訂的錯誤回應格式。
