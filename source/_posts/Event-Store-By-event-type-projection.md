---
title: Event Store - By event type projection
date: 2018-09-04 23:18:49
tags: [Event Store]
---

$by_event_type 是 Event Store 預設提供的 Projection，可以將 Event 依 Event Type 拆分成到對應的 Stream。

<!-- More -->

<br/>


使用前需先將 $by_event_type projection 開啟。  

{% asset_img 1.png %}
 
<br/>


{% asset_img 2.png %}
 
<br/>


開啟後切到 Stream Browser 頁面，點選 Add Event 按鈕發送 Event。  

{% asset_img 3.png %}
 
<br/>


這邊可一次發送了多個 Event 做個測試。  

{% asset_img 4.png %}
 
<br/>


發送完切回 Stream Browser 頁面，會看到 $by_event_type projection 會幫我們產生 $et-[EventType] 這樣的 Stream。  

{% asset_img 5.png %}
 
<br/>


{% asset_img 6.png %}
 
<br/>


Link
---
* [System Projections | Event Store](https://eventstore.org/docs/projections/system-projections/index.html)
