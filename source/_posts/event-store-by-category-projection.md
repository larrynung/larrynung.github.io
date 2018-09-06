---
title: "Event Store - By category projection"
date: 2018-09-03 23:52:35
tags: [Event Store]
---

$by_category 是 Event Store 預設提供的 Projection，可以將 Event 依 Stream ID 去拆分成不同 Category 的 Stream。  

<!-- More -->

<br/>


使用前需先將 $by_category projection 開啟。  

{% asset_img 1.png %}
 
<br/>


{% asset_img 2.png %}
 
<br/>


開啟後切到 Stream Browser 頁面，點選 Add Event 按鈕發送 Event。  

{% asset_img 3.png %}
 
<br/>


Event 的 Stream ID 可依 [Category]-[ID] 這樣的格式下去定義。  

{% asset_img 4.png %}
 
<br/>


{% asset_img 5.png %}
 
<br/>


{% asset_img 6.png %}
 
<br/>


這邊可一次發送了多個 Event 做個測試。  

{% asset_img 7.png %}
 
<br/>


發送完切回 Stream Browser 頁面，會看到 $by_category projection 會幫我們產生 $ce-[Category] 這樣的 Stream。  

{% asset_img 8.png %}
 
<br/>


裡面都是相同 Category 的 Event 。  

{% asset_img 9.png %}
 
<br/>


$by_category projection 若有需要也可以做些調動，只要點選 Edit 按鈕。  

{% asset_img 10.png %}
 
<br/>


對 Source 部份做些調動，Source 中的 first 是指第一個分隔符號，- 是指用來分隔的符號，這邊可以試著把 first 改為 last。  

{% asset_img 11.png %}
 
<br/>


按下 Save 按鈕儲存。  

{% asset_img 12.png %}
 
<br/>


$by_category project 就會依最後一個分隔符號下去切割 Category。  

{% asset_img 13.png %}
 
<br/>


{% asset_img 14.png %}
 
<br/>


Link
---
* [System Projections | Event Store](https://eventstore.org/docs/projections/system-projections/index.html)
