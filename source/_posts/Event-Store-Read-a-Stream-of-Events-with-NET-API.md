---
title: Event Store - Read a Stream of Events with .NET API
date: 2018-09-16 23:56:40
tags: [Event Store]
---

要使用 Event Store .NET API 讀取 Event Store 特定 Stream 內的 Event，可以帶入 Stream 的名稱、起始的 Event 編號、以及預計要讀取的 Event 數，去調用 Connetction.ReadStreamEventsForwardAsync 方法。  

<!-- More -->

```C#
...
var readEvents = conn.ReadStreamEventsForwardAsync(streamName, start, count, true).Result;
...
```

<br/>

然後再去讀取需要的 Event 資料即可。  

```C#
...
foreach (var evt in readEvents.Events)
    Console.WriteLine("{0} {1}", evt.Event.EventNumber, Encoding.UTF8.GetString(evt.Event.Data));
...
```

<br/>


像是這邊筆者有個 Stream 內含有 100 個相同資料的 Event。  

{% asset_img 1.png %}
 
<br/>


就可以像下面這樣讀取特定範圍的 Event。  

```C#
using EventStore.ClientAPI;
...
using (var conn = EventStoreConnection.Create(connectionString, connectionName))
{
    conn.ConnectAsync().Wait();

    var streamName = "MyStream";
    var readEvents = conn.ReadStreamEventsForwardAsync(streamName, 10, 10, true).Result;
    foreach (var evt in readEvents.Events)
        Console.WriteLine("{0} {1}", evt.Event.EventNumber, Encoding.UTF8.GetString(evt.Event.Data));
}
...
```

{% asset_img 2.png %}
 
<br/>


{% asset_img 3.png %}
 
<br/>


Link
----
* [Step 2 - Read events from a stream and subscribe to changes | Event Store](https://eventstore.org/docs/getting-started/reading-subscribing-events/index.html?tabs=tabid-6%2Ctabid-dotnet-client%2Ctabid-8%2Ctabid-dotnet-read-event%2Ctabid-create-sub-dotnet)
