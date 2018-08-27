---
title: Event Store - Install with docker
date: 2018-08-27 23:13:22
tags: [Event Store]
---

要透過 Docker 使用 Event Store，可以調用下列命令：  

<!-- More -->

    docker run --name eventstore-node -it -p 2113:2113 -p 1113:1113 eventstore/eventstore

<br/>


Docker 會下載 eventstore-node image。  

{% asset_img 1.png %}
 
<br/>


然後會運行 Event Store 服務。  

{% asset_img 2.png %}
 
<br/>


訪問 http://127.0.0.1:2113 即可看到 Event Store 的 Web 介面，若要登入可用帳號 admin 密碼 changeit 登入。

{% asset_img 3.png %}
 
<br/>


Link
----
* [eventstore/eventstore - Docker Hub](https://hub.docker.com/r/eventstore/eventstore/)
* [Step 1 - Install, run, and write your first event | Event Store](https://eventstore.org/docs/getting-started/?tabs=tabid-1%2Ctabid-4)
