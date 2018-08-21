---
title: "Event Store - Install on Windows"
date: 2018-08-21 23:31:05
tags: [Event Store]
---

要在 Windows 下使用 Event Store，可透過 Chocolatey 安裝 eventstore-oss 套件。   

<!-- More -->

    choco install eventstore-oss

<br/>


也可以至下載頁下載壓縮檔，將之解壓縮。  

{% asset_img 1.png %}
 
<br/>


{% asset_img 2.png %}
 
<br/>


然後調用下列命令啟用 Event Store 服務。  

    EventStore.ClusterNode.exe --db ./db --log ./logs


{% asset_img 3.png %}
 
<br/>


{% asset_img 4.png %}
 
<br/>


服務啟用後訪問 http://127.0.0.1:2113，即可看到 Event Store 的 Web 介面，若要登入可用帳號 admin 密碼 changeit 登入。  

{% asset_img 5.png %}
 
<br/>


{% asset_img 6.png %}
 
<br/>


Link
----
* [Event Store](https://eventstore.org/)
