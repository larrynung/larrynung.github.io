---
title: Event Store - Scavenging events
date: 2018-09-29 23:46:06
tags: [Event Store]
---

當刪除 Event 或是 Stream 時， Event Store 不會立即刪除，硬碟空間也並未被回收，若要讓 Event Store 立即做刪除的處理，可以使用 Event Store 的 Scavenge。   

<!-- More -->

<br/>


像是筆者這邊將大量的 Event 寫入 Event Store，並將 Event 設為一秒後自動刪除。  

{% asset_img 1.png %}
 
<br/>


當 Event 被刪除後，雖然 Event Store 看不到這些 Event，但是 Event Store 其實必為真的將之刪除。  

{% asset_img 2.png %}
 
<br/>


這時我們可以打 Event Store 的 Scavenge API。  

    curl -i -d {} -X POST http://localhost:2113/admin/scavenge -u "admin:changeit"

<br/>


或是透過 Web interface Admin 頁面的 Scavenge 按鈕觸發 Scavenge。  

{% asset_img 3.png %}
 
<br/>


處理完後點選 Scavenge 紀錄查看。  

{% asset_img 4.png %}
 
<br/>


可以看到 Scavenge 處理的細部資訊，像是節省了多少硬碟空間等。  

{% asset_img 5.png %}
 
<br/>


Link
----
* [Scavenging events | Event Store](https://eventstore.org/docs/server/scavenging/index.html?tabs=tabid-8)
