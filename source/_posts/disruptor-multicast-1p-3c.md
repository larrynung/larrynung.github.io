---
layout: post
title: "Disruptor - Multicast: 1P – 3C"
date: 2016-03-16 05:23:00
comments: true
tags: [Disruptor]
keywords: "Disruptor"
description: "Disruptor - Multicast: 1P – 3C"
---

使用 Disruptor 時我們必須決定資料要怎樣在 Consumer 間流動，這有些常用的 Pattern 可供參考，只要熟悉這些 Pattern 那 Consumer 間有多複雜的協作應該都不是問題。

<!-- More -->

<br/>


這邊要介紹的是 Multicast: 1P – 3C，一個 Producer 負責生產資料，三個 Consumer 同時消費資料。其依賴關係圖會像這樣：  

{% img /images/posts/DisruptorMulticast1P3C/1.png %}

<br/>


可進一步簡化成下面這樣：  

{% img /images/posts/DisruptorMulticast1P3C/2.png %}

<br/>


透過 DSL 的方式撰寫，只要同時將三個 EventHandler 帶入 HandleEventWith 即可，像是下面這樣：  

```c#
... 
var disruptor = new Disruptor.Dsl.Disruptor<Data>(() => new Data(), (int)Math.Pow(2,4), TaskScheduler.Default); 
disruptor.HandleEventsWith(new DataEventHandler("Handler1"), new DataEventHandler("Handler2"), new DataEventHandler("Handler3")); 

var ringBuffer = disruptor.Start(); 
...
disruptor.Shutdown(); 
…
```

<br/>


是改用 Non-DSL 撰寫的話，本來的依賴關係圖形就會變成下面這樣：

{% img /images/posts/DisruptorMulticast1P3C/3.png %}

<br/>


用程式來寫，就是三個 EventProcessor 共用同一個 Barrier。  

```c#
... 
var ringBuffer = RingBuffer<Data>.CreateSingleProducer(() => new Data(), (int)Math.Pow(2, 4)); 
var barrier = ringBuffer.NewBarrier(); 
var eventProcessor1 = new BatchEventProcessor<Data>(ringBuffer, barrier, new DataEventHandler("Handler1")); 
var eventProcessor2 = new BatchEventProcessor<Data>(ringBuffer, barrier, new DataEventHandler("Handler2")); 
var eventProcessor3 = new BatchEventProcessor<Data>(ringBuffer, barrier, new DataEventHandler("Handler3")); 

Task.Factory.StartNew(() => eventProcessor1.Run()); 
Task.Factory.StartNew(() => eventProcessor2.Run()); 
Task.Factory.StartNew(() => eventProcessor3.Run()); 

... 
eventProcessor1.Halt(); 
eventProcessor2.Halt(); 
eventProcessor3.Halt(); 
...
```

<br/>


運行起來可以看到有三個 Handler，分別在不同的執行緒上運作，Producer 產生的每一筆資料都會同時經過這三個 Handler 做處理。所以這邊可以看到每個 Sequence 資料都有經過三個 Handler，但是 Handler 執行的順序並不固定。   

{% img /images/posts/DisruptorMulticast1P3C/4.png %}
