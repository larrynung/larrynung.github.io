---
layout: post
title: "Disruptor - High Performance Inter-Thread Messaging Library"
date: 2016-03-19 15:32
comments: true
categories: [Disruptor]
keywords: "Disruptor"
description: "Disruptor - High Performance Inter-Thread Messaging Library"
---

Disruptor 是 LMAX 提出的高效線程通信套件，能夠以很低的延遲產生很大量的吞吐量，實務上 LMAX 藉此得以在一個線程裡每秒處理6百萬訂單。  

<!-- More -->

<br/>


高效線程通信套件這個詞彙如果太抽象，我們也可以將之視為高效低延遲的生產者與消費者模式框架，使用這個框架可以很容易的套用生產者與消費者模式，且整個模式的工作流程可輕易的設定與調動。  

<br/>


Disruptor 之所以能有如此優異的效能，是因為裡面運用了很多技術在。像是使用 Compare and swap (CAS) 去避開鎖的開銷，使用 mory barrier 去控制執行緒間的運行順序，使用‸Cache line padding 避免 false sharing 的問題，以及預先將記憶體配置並重用以避免不必要的 GC 回收。  

<br/>


Disruptor 最經典的使用架構就是 LMAX 所提出的架構，分為三個部分，一個是輸入的 Disruptor，一個是商業邏輯處理的部份，最後是輸出的 Disruptor。  

{% img /images/posts/Disruptor/1.png %}

<br/>


輸入的 Disruptor 這邊，會先將進來的事件存起來，如果發生什麼問題，可以讓他重新運轉。接著會將事件傳送給其他 Slave 節點(LMAX 這邊是用 IP Multicasting 去同步所有 Slave 節點)，以實現 HA 架構。最後是拆解任務與資料，讓後續商業邏輯的處理比較容易。  

{% img /images/posts/Disruptor/2.png %}

<br/>


商業邏輯處理這邊要注意的就是要盡可能的快速，所以需要的資料都放置在記憶體中是最好的，且要避免 IO 的處理。  

<br/>


輸出 Disruptor 這邊，則負責將資料合併，導到該去的地方。  

<br/>


整個架構就像下面這樣：  

{% img /images/posts/Disruptor/3.png %}

<br/>


Link
----
* [Disruptor by LMAX-Exchange](https://lmax-exchange.github.io/disruptor/)
