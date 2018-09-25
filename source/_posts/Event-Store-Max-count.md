---
title: Event Store - Max count
date: 2018-09-25 23:20:40
tags: [Event Store]
---

要設定 Event Store 的 Stream 只存放指定個數的 Event，可以設定 StreamMetadata。  

<!-- More -->

<br/>


透過 StreamMetadata 的 MaxCount 指定 Stream 最大存放的 Event 數，然後透過 Connection.SetStreamMetadataAsync，帶入 Stream 的名稱、ExpectedVersion、以及剛設定好的 StreamMetadata。  

```C#
...
var streamMetaData = StreamMetadata.Create(maxCount: maxCount);
    
conn.SetStreamMetadataAsync(streamName, ExpectedVersion.StreamExists, streamMetaData).Wait();
```

<br/>


像是筆者這邊設定了 Stream 的 Metadata，指定 Stream 只存放 10 筆 Event，然後接著嘗試塞入 100 的 Event。  

```C#
using EventStore.ClientAPI;
...
using (var conn = EventStoreConnection.Create(connectionString, connectionName))
{
    conn.ConnectAsync().Wait();

    var streamName = "MyStream";
    var typeName = "MyType";
    var streamMetaData = StreamMetadata.Create(maxCount: 10);

    conn.SetStreamMetadataAsync(streamName, ExpectedVersion.StreamExists, streamMetaData).Wait();

    var data = new
    {
        Msg = "Hello world!"
    };
    var jsonData = Encoding.UTF8.GetBytes(JsonConvert.SerializeObject(data));
    var eventData = new EventData(Guid.NewGuid(), typeName, true, jsonData, null);
    var eventDataCollection = Enumerable.Repeat(eventData, 100);
    conn.AppendToStreamAsync(streamName, ExpectedVersion.Any, eventDataCollection).Wait();
}
```

{% asset_img 1.png %}
 
<br/>


可以看到 Stream 只會留下 10 筆 Event。  

{% asset_img 2.png %}
 
<br/>


Link
----
* [Deleting streams and events | Event Store](https://eventstore.org/docs/server/deleting-streams-and-events/index.html)
