---
title: "Event Store - Install on Windows"
date: 2018-08-21 23:31:05
tags: [Event Store]
---

要在 Windows 下使用 Event Store，首先需確定環境已安裝：

<!-- More -->

- NET Framework 4.0+
- Windows platform SDK with compilers (v7.1) or Visual C++ installed (Only required for a full build)

<br/>


若環境已備妥，我們可選擇透過 Chocolatey 安裝 eventstore-oss 套件。   

    choco install eventstore-oss

<br/>


或是至下載頁下載壓縮檔。  

{% asset_img 1.png %}
 
<br/>


將之解壓縮也可以。  

{% asset_img 2.png %}
 
<br/>


安裝完可調用下列命令將 Event Store 服務啟動。  

    EventStore.ClusterNode.exe --db ./db --log ./logs


{% asset_img 3.png %}
 
<br/>


{% asset_img 4.png %}
 
<br/>


服務啟動後訪問 http://127.0.0.1:2113，沒意外的話可以看到 Event Store 的 Web 介面，若要登入可用帳號 admin 密碼 changeit 登入。  

{% asset_img 5.png %}
 
<br/>


透過這 Web 介面可以觀察到服務的狀況、發送 Event、管理帳號...等。  

{% asset_img 6.png %}
 
<br/>


Link
----
* [Event Store](https://eventstore.org/)
