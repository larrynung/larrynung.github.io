---
layout: post
title: "StackExchange.Redis - A high performance general purpose redis client for .NET languages"
date: 2016-05-22 23:18:00
comments: true
tags: [StackExchange.Redis]
keywords: "StackExchange.Redis"
description: "StackExchange.Redis - A high performance general purpose redis client for .NET languages"
---

StackExchange.Redis 是 StackExchange 提供的 redis client 實作。  

<!-- More -->

<br/>


該套件具有以下特點：  

* High performance multiplexed design, allowing for efficient use of shared connections from multiple calling threads  
* Abstraction over redis node configuration: the client can silently negotiate multiple redis servers for robustness and availability  
* Convenient access to the full redis feature-set  
* Full dual programming model both synchronous and asynchronous usage, without requiring "sync over async" usage of the TPL  
* Support for redis "cluster"  

<br/>


使用上需先透過 NuGet 套件管理視窗安裝套件，他有提供兩種套件，一種是不含強命名簽章的套件 StackExchange.Redis，一種是有強命名簽章的套件 StackExchange.Redis.StrongName。  

{% img /images/posts/StackExchange.Redis/1.png %}

<br/>


或是透過 Package Manager Console 輸入下列命令安裝套件。  

    Install-Package StackExchange.Redis
    Install-Package StackExchange.Redis.StrongName

<br/>


套件安裝完後，就可進行 Redis 存取部分的撰寫，程式撰寫起來會像下面這樣：  

```c#
using StackExchange.Redis; 
... 
var configuration = GetConfiguration(); 
using (var conn = ConnectionMultiplexer.Connect(configuration)) 
{ 
    ... 
} 
...
```

<br/>


程式一開始會先設定 Configuration，相當於一般我們在用的 DB 連線字串，用以指定 Redis 位置等資訊。 再來會用 ConnectionMultiplexer.Connect 將 Configuration 帶入開啟連線，連線開啟後可對 Server 進行操作，像是取得 Server 的資訊，或是運行 Server 的命令。  

```c#
using StackExchange.Redis; 
... 
var configuration = GetConfiguration(); 
using (var conn = ConnectionMultiplexer.Connect(configuration)) 
{ 
    var endPoint = conn.GetEndPoints().First(); 
    var server = conn.GetServer(endPoint); 
    //var host = GetHost(); 
    //var port = GetPort(); 
    //var server = conn.GetServer(host, port); 
    ...
} 
...
```

<br/>


可以對指定的 DB 進行操作。  

```c#
using StackExchange.Redis; 
... 
var configuration = GetConfiguration(); 
using (var conn = ConnectionMultiplexer.Connect(configuration)) 
{ 
    var db = conn.GetDatabase(); 
    ... 
} 
...
```

<br/>


抑或是處理訂閱都可以。  

```c#
using StackExchange.Redis; 
... 
var configuration = GetConfiguration(); 
using (var conn = ConnectionMultiplexer.Connect(configuration)) 
{ 
    var sub = conn.GetSubscriber(); 
    var channelName = GetChannelName(); 
    var handler = GetChannelHandler(); 

    //conn.PreserveAsyncOrder = false;
    sub.Subscribe(channelName, handler); 
    ... 

    var message = GetMessage(); 
    sub.Publish(channelName, message);
    ...
} 
...
```

<br/>


最後記得要將當初開啟的連線關閉就可以了(用 using 讓它自動處理也可以)。  

<br/>


Link
----
* [NuGet Gallery | StackExchange.Redis](https://www.nuget.org/packages/StackExchange.Redis/)
* [GitHub - StackExchange/StackExchange.Redis: General purpose redis client](https://github.com/StackExchange/StackExchange.Redis)
