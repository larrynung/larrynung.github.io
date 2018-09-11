---
title: Event Store - Connect with .NET API
date: 2018-09-11 23:43:10
tags: [Event Store]
---

要使用 Event Store .NET API 連接 Event Store，先要安裝 EventStore.Client 套件。  

<!-- More -->


{% asset_img 1.png %}

<br/>


加入 EventStore.ClientAPI 命名空間。  

    using EventStore.ClientAPI;

<br/>


接著調用 EventStoreConnection.Create 取得 Connection 物件。  

```C#
...
using (var conn = EventStoreConnection.Create(...))
{
    ...
}
```

<br/>


調用 Connection 物件的 ConnectAsync 方法建立與 EventStore 的連線。  

```C#
...
conn.ConnectAsync();
...
```

<br/>


像是下面這樣，指定 Connection name 與 uri 建立出對應的連線物件，然後進行連線。  

```C#
var connectionName = "MyConsole";
var uri = new Uri("tcp://admin:changeit@localhost:1113");

using (var conn = EventStoreConnection.Create(uri, connectionName))
{
     conn.ConnectAsync().Wait();

     Console.ReadKey();
}
```

{% asset_img 2.png %}
 
<br/>


連線的建立可從 Web interface 的 Dashboard 頁面查閱，像是這邊 Connections 下就有剛所建立的 MyConsole connection。  

{% asset_img 3.png %}
 
<br/>


建立 Event Store 連線時也可以帶入 ConnectionSettings 做些細部的設定。  

<br/>


像是下面這邊就透過 ConnectionSettings 建立出設定物件，透過設定物件做些設定，像是使用 Verbose 層級的 Log 可以調用 EnableVerboseLogging()，要將 Log 導到主控台可調用 UseConsoleLogger()。  																						
```C#
var connectionName = "MyConsole";
var uri = new Uri("tcp://admin:changeit@localhost:1113");
var settings = ConnectionSettings.Create();

settings.EnableVerboseLogging();
settings.UseConsoleLogger();
            
using (var conn = EventStoreConnection.Create(settings, uri, connectionName))
{
    conn.ConnectAsync().Wait();
    Console.ReadKey();
}
```

{% asset_img 4.png %}
 
<br/>


{% asset_img 5.png %}

<br/>


此外也支援連線字串的設定，

```C#
var connectionName = "MyConsole";
var connectionString = "ConnectTo=tcp://admin:changeit@localhost:1113; HeartBeatTimeout=500";

using (var conn = EventStoreConnection.Create(connectionString, connectionName))
{
        conn.ConnectAsync().Wait();

        Console.ReadKey();
}
```

{% asset_img 6.png %}

<br/>


Link
----
* [Connecting to a Server | Event Store](https://eventstore.org/docs/dotnet-api/connecting-to-a-server/index.html)
