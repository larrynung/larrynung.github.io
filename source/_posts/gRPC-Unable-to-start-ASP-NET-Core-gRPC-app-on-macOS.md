---
title: gRPC - Unable to start ASP.NET Core gRPC app on macOS
date: 2019-12-01 12:36:18
tags: [gRPC]
---

使用 ASP.NET Core 3.0 範本建立 gPRC 程式，
在 MAC 的環境下直接運行起來會發生 HTTP/2 over TLS is not supported on macOS due to mis sing ALPN support 錯誤。  

<!-- More -->

```
System.IO.IOException: Failed to bind to address https://localhost:5001.
 ---> System.AggregateException: One or more errors occurred. (HTTP/2 over TLS is not supported on macOS due to missing ALPN support.) (HTTP/2 over TLS is not supported on macOS due to missing ALPN support.)
 ---> System.NotSupportedException: HTTP/2 over TLS is not supported on macOS due to missing ALPN support.
```

{% asset_img 1.png %}

</br>


這是因為 MAC 作業系統不支援 ALPN，所以不能使用 HTTP/2 with TLS，需要設定 Kestrel 改走 HTTP/2 without TLS 才可以正常運行。  

```c#
...
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.ConfigureKestrel(options =>
            {
                // Setup a HTTP/2 endpoint without TLS.
                options.ListenLocalhost(5000, o => o.Protocols =
                    HttpProtocols.Http2);
            });
            webBuilder.UseStartup<Startup>();
        });
...
```

{% asset_img 2.png %}
