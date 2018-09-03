---
title: "Event Store - By category projection"
date: 2018-09-03 23:52:35
tags: [Event Store]
---

$by_category 是 Event Store 預設提供的 Projection，可以將 Stream 依 Category 拆分成到對應的 Stream。  

<!-- More -->

<br/>


使用前需先將 $by_category projection 開啟。  

{% asset_img 1.png %}
 
<br/>


{% asset_img 2.png %}
 
<br/>


開啟後可以切到 Stream Browser 頁面，點選 Add Event 按鈕發送 Event 試試。  

{% asset_img 3.png %}
 
<br/>


Event 的 Stream ID 可依 [Category]-[ID] 這樣的格式下去定義。  

{% asset_img 4.png %}
 
<br/>


{% asset_img 5.png %}
 
<br/>


{% asset_img 6.png %}
 
<br/>


這邊可一次發送了多個 Event 做測試。  

{% asset_img 7.png %}
 
<br/>


發送完切回 Stream Browser 頁面，可看到 $by_category projection 會幫我們產生 $ce-[Category] 這樣的 Stream。  

{% asset_img 8.png %}
 
<br/>


{% asset_img 9.png %}
 
<br/>


Link
---
* [System Projections | Event Store](https://eventstore.org/docs/projections/system-projections/index.html)
