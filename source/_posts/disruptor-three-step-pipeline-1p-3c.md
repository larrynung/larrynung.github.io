---
layout: post
title: "Disruptor - Three Step Pipeline: 1P – 3C"
date: 2016-03-15 05:11:00
comments: true
tags: [Disruptor]
keywords: "Disruptor"
description: "Disruptor - Three Step Pipeline: 1P – 3C"
---

使用 Disruptor 時我們必須決定資料要怎樣在 Consumer 間流動，這有些常用的 Pattern 可供參考，只要熟悉這些 Pattern 那 Consumer 間有多複雜的協作應該都不是問題。  

<!-- More -->

<br/>


這邊要介紹的是 Three Step Pipeline: 1P – 3C，一個 Producer 負責生產資料，三個 Consumer 接續消費資料。簡單說，這就是多執行緒程式常見的流水線 Pattern。其依賴關係圖會像這樣：  

{% img /images/posts/DisruptorStepPipeline1P3C/1.png %}

<br/>


透過 DSL 的方式撰寫，就是用 Then 去串接後續的 EventHandler，像是下面這樣：  

```c#
... 
var disruptor = new Disruptor.Dsl.Disruptor<Data>(() => new Data(), (int)Math.Pow(2,4), TaskScheduler.Default); 

disruptor.HandleEventsWith(new DataEventHandler("Handler1"))
.Then(new DataEventHandler("Handler2"))
.Then(new DataEventHandler("Handler3")); 

var ringBuffer = disruptor.Start(); 
...
disruptor.Shutdown(); 
…
```

<br/>


若是改用 Non-DSL 撰寫的話，本來的依賴關係圖形就會變成下面這樣：

{% img /images/posts/DisruptorStepPipeline1P3C/2.png %}

<br/>


用程式來寫，就是要建立一個 Barrier 將之帶入並建立 EventProcessor，接著將第一個 EventProcessor 的 Sequence 帶入建立出第二個 Barrier，再用第二個 Barrier 建立第二個 EventProcessor，最後用第二個 EventProcessor 的 Sequence 建立出第三個 Barrier，用第三個 Barrier 去建立第三個 EventProcessor 即可。  

```c#
... 
var ringBuffer = RingBuffer<Data>.CreateSingleProducer(() => new Data(), (int)Math.Pow(2, 4)); 
var eventProcessor1 = new BatchEventProcessor<Data>(ringBuffer, ringBuffer.NewBarrier(), new DataEventHandler("Handler1")); 
var eventProcessor2 = new BatchEventProcessor<Data>(ringBuffer, ringBuffer.NewBarrier(eventProcessor1.Sequence), new DataEventHandler("Handler2")); 
var eventProcessor3 = new BatchEventProcessor<Data>(ringBuffer, ringBuffer.NewBarrier(eventProcessor2.Sequence), new DataEventHandler("Handler3")); 

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


程式運行起來可以看到有三個 Handler，分別在不同的執行緒上運作，Producer 產生的每一筆資料都會循序的經過這三個 Handler 做處理。   

{% img /images/posts/DisruptorStepPipeline1P3C/3.png %}

<br/>


注意到這邊，這結果跟跟一般認知的多執行緒流水線 Pattern 有所出入，若是流水線 Pattern 的話，顯示的 Handler 應該不會是 123123123... 這樣有規律的循環，資料在送到 Consumer2 處理時，Consumer1 應該可以接著處理後面的資料。之所以會這樣，其實是因為筆者的測試案例太過單純所導致，如果把 Consumer 的處理時間拉長，就會回到流水線 Pattern 該有的樣子，像是 121233..。  
