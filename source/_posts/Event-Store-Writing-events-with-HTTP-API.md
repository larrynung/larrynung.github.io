---
title: Event Store - Writing events with HTTP API
date: 2018-08-29 23:19:10
tags: [Event Store]
---

要透過 HTTP API 去發送 event，可以朝以下位置發送 Post。   

<!-- More -->

    http://<URL>/streams/<STREAM_ID> 

<br/>


MediaType 可以是 JSON。

    application/vnd.eventstore.events+json

<br/>


也可以是 XML。  

    application/vnd.eventstore.events+xml

<br/>


Post 的內容需包含 eventId、eventType、data。  

<br/>


像是如果要發送個 Event 給 Event Store，就可以像下面這樣準備要發送的 Event 內容。  

```json  
[
  {
    "eventId": "fbf4a1a1-b4a3-4dfe-a01f-ec52c34e16e4",
    "eventType": "event-type",
    "data": {
      "a": "1"
    }
  }
]
```

{% asset_img 1.png %}
 
<br/>


然後使用 CURL 發送給 Event Store。  

    curl -i -d "@event.json" "http://127.0.0.1:2113/streams/newstream" -H "Content-Type:application/vnd.eventstore.events+json"

{% asset_img 2.png %}
 
<br/>


Event Store 就會接收到剛發送的 Event。  

{% asset_img 3.png %}
 
<br/>


{% asset_img 4.png %}
 
<br/>
