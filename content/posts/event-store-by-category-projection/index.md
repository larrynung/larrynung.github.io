---
title: "Event Store - By category projection"
date: "2018-09-03 23:52:35"
tags: [Event Store]
---


$by_category 是 Event Store 預設提供的 Projection，可以將 Event 依 Stream ID 去拆分成不同 Category 的 Stream。  

<!-- More -->

<br/>


使用前需先將 $by_category projection 開啟。  

![1.png](1.png)
 
<br/>


![2.png](2.png)
 
<br/>


開啟後切到 Stream Browser 頁面，點選 Add Event 按鈕發送 Event。  

![3.png](3.png)
 
<br/>


Event 的 Stream ID 可依 [Category]-[ID] 這樣的格式下去定義。  

![4.png](4.png)
 
<br/>


![5.png](5.png)
 
<br/>


![6.png](6.png)
 
<br/>


這邊可一次發送了多個 Event 做個測試。  

![7.png](7.png)
 
<br/>


發送完切回 Stream Browser 頁面，會看到 $by_category projection 會幫我們產生 $ce-[Category] 這樣的 Stream。  

![8.png](8.png)
 
<br/>


裡面都是相同 Category 的 Event 。  

![9.png](9.png)
 
<br/>


$by_category projection 若有需要也可以做些調動，只要點選 Edit 按鈕。  

![10.png](10.png)
 
<br/>


對 Source 部份做些調動，Source 中的 first 是指第一個分隔符號，- 是指用來分隔的符號，這邊可以試著把 first 改為 last。  

![11.png](11.png)
 
<br/>


按下 Save 按鈕儲存。  

![12.png](12.png)
 
<br/>


$by_category project 就會依最後一個分隔符號下去切割 Category。  

![13.png](13.png)
 
<br/>


![14.png](14.png)
 
<br/>


Link
