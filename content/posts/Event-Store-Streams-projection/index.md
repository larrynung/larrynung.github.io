---
title: "Event Store - Streams projection"
date: "2018-09-06 00:01:37"
tags: [Event Store]
---


$streams 是 Event Store 預設提供的 Projection，可以將 Event Link 到一個集中的 Stream。  

<!-- More -->

<br/>


使用前需先將 $streams projection 開啟。

![1.png](1.png)
 
<br/>


![2.png](2.png)
 
<br/>


開啟後切到 Stream Browser 頁面，點選 Add Event 按鈕發送 Event。  

![3.png](3.png)
 
<br/>


![4.png](4.png)
 
<br/>


這邊可一次發送了多個 Event 做個測試。  

![5.png](5.png)
 
<br/>


發送完切回 Stream Browser 頁面，會看到 $streams projection 會幫我們產生 $streams 這樣的 Stream。  

![6.png](6.png)
 
<br/>


點進去會看到剛所發送的 Event 都被 Link 在這個 Stream 內。  

![7.png](7.png)
 
<br/>


Link
----
* [System Projections | Event Store](https://eventstore.org/docs/projections/system-projections/index.html)
