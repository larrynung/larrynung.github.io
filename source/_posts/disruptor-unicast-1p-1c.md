---
layout: post
title: "Disruptor - Unicast: 1P - 1C"
date: 2016-03-14 23:05:00
comments: true
tags: [Disruptor]
keywords: "Disruptor"
description: "Disruptor - Unicast: 1P - 1C"
---

使用 Disruptor 時我們必須決定資料要怎樣在 Consumer 間流動，這有些常用的 Pattern 可供參考，只要熟悉這些 Pattern 那 Consumer 間有多複雜的協作應該都不是問題。  

<!-- More -->

<br/>


最簡單的 Pattern 就是 Unicast: 1P - 1C，一個 Producer 負責生產資料，一個 Consumer 負責消費資料。依賴關係圖會像這樣：    

{% img /images/posts/DisruptorUnicast1P1C/1.png %}

<br/>


這透過 DSL 的方式撰寫會像下面這樣：  

{% codeblock lang:c# %}
...
using Disruptor; 
namespace ConsoleApplication29 { 
    …
    class Program { 
        static void Main( string[] args) { 
            var disruptor = new Disruptor.Dsl. Disruptor<Data>(() => new Data(), (int)Math .Pow(2,4), TaskScheduler.Default); 
            disruptor.HandleEventsWith(new DataEventHandler("Handler1”)); 
            var ringBuffer = disruptor.Start(); 
            var idx = 0; 
            while ( true) { 
                var sequenceNo = ringBuffer.Next(); 
                var data = ringBuffer[sequenceNo]; 
                data.Value = idx++.ToString(); 
                ringBuffer.Publish(sequenceNo); 
                Thread.Sleep(250); 
             } 
            disruptor.Shutdown(); 
        } 
    } 
} 
{% endcodeblock %}

<br/>


若是改用 Non-DSL 撰寫的話，本來的依賴關係圖形就會變成下面這樣：    

{% img /images/posts/DisruptorUnicast1P1C/2.png %}

<br/>


程式寫起來會像下面這樣：  

{% codeblock lang:c# %}
... 
var ringBuffer = RingBuffer<Data>.CreateSingleProducer(() => new Data(), (int)Math.Pow(2, 4)); 
var barrier = ringBuffer.NewBarrier(); 
var eventProcessor = new BatchEventProcessor<Data>(ringBuffer, barrier, new DataEventHandler("Handler1")); 

Task.Factory.StartNew(() => eventProcessor.Run()); 
... 
eventProcessor.Halt(); 
... 
{% endcodeblock %}

<br/>


程式運行起來可以看到我們只有一個 Handler，這個 Handler 會在一個執行緒上循序地消費 Producer 產生的資料。	
{% img /images/posts/DisruptorUnicast1P1C/3.png %}
