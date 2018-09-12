---
title: "Event Store - Appending to a stream in a single write with .NET API"
date: 2018-09-12 23:45:47
tags: [Event Store]
---

要使用 Event Store .NET API 發送 Event 給 Event Store，可以先進行 Event Store 的連線。  

<!-- More -->

<br/>


連線後設定 EventData。  

```C#
...
var typeName = "MyType";
var data = new {
    Msg="Hello world!"
};
var jsonData = Encoding.UTF8.GetBytes(JsonConvert.SerializeObject(data));
var eventData = new EventData(Guid.NewGuid(), typeName, true, jsonData, null);
...
```

<br/>


呼叫 Connection.AppendToStreamAsync 將 EventData 送入 Event Store 指定的 Stream (ExpectedVersion 可用來決定是否要判斷 Stream 是否存在)。  

```C#
...
conn.AppendToStreamAsync(streamName, ExpectedVersion.Any, eventData);
...
```

<br/>


程式寫起來會像下面這樣：

```C#
using EventStore.ClientAPI;
using Newtonsoft.Json;
using System;
using System.Text;
...
var connectionName = "MyConsole";
var connectionString = "ConnectTo=tcp://admin:changeit@localhost:1113; HeartBeatTimeout=500";

using (var conn = EventStoreConnection.Create(connectionString, connectionName))
{
    conn.ConnectAsync().Wait();

    var streamName = "MyStream";
    var typeName = "MyType";
    var data = new {
        Msg="Hello world!"
    };
    var jsonData = Encoding.UTF8.GetBytes(JsonConvert.SerializeObject(data));
    var eventData = new EventData(Guid.NewGuid(), typeName, true, jsonData, null);
    conn.AppendToStreamAsync(streamName, ExpectedVersion.Any, eventData).Wait();
}
...
```

{% asset_img 1.png %}
 
<br/>


運行起來後可透過 Web interface 找到對應的 Stream。  

{% asset_img 2.png %}
 
<br/>


對應的 Event。  

{% asset_img 3.png %}
 
<br/>


{% asset_img 4.png %}
 
<br/>


Link
----
* [Writing to a Stream | Event Store](https://eventstore.org/docs/dotnet-api/writing-to-a-stream/index.html)
