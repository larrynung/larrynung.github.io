---
title: Event Store - Read a Single Event with .NET API
date: 2018-09-17 22:32:13
tags: [Event Store]
---

要使用 Event Store .NET API 讀取 Event Store 特定 Stream 內特定的 Event，可以帶入 Stream 的名稱、Event 的編號，調用 Connection.ReadEventAsync 方法。  

<!-- More -->

```C#
...
var readResult = conn.ReadEventAsync(streamName, 0, true).Result;
...
```

<br/>


然後再去讀取需要的 Event 資料即可。  

```C#
...
Console.WriteLine("{0} {1}", readResult.EventNumber, Encoding.UTF8.GetString(readResult.Event.Value.Event.Data));
...
```

<br/>


像是筆者這邊有個 Event 如下：   

{% asset_img 1.png %}
 
<br/>


就可以像下面這樣讀取指定的 Event。  

```C#
using EventStore.ClientAPI;
...
using (var conn = EventStoreConnection.Create(connectionString, connectionName))
{
    conn.ConnectAsync().Wait();

    var streamName = "MyStream";
    var readResult = conn.ReadEventAsync(streamName, 0, true).Result;
    Console.WriteLine("{0} {1}", readResult.EventNumber, Encoding.UTF8.GetString(readResult.Event.Value.Event.Data));
}
...
```

{% asset_img 2.png %}
 
<br/>


{% asset_img 3.png %}
 
<br/>


Link
----
* [Step 2 - Read events from a stream and subscribe to changes | Event Store](https://eventstore.org/docs/getting-started/reading-subscribing-events/index.html?tabs=tabid-6%2Ctabid-dotnet-client%2Ctabid-8%2Ctabid-dotnet-read-event%2Ctabid-create-sub-http)
