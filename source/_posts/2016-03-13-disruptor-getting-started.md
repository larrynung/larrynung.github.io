---
layout: post
title: "Disruptor - Getting started"
date: 2016-03-13 17:51:00
comments: true
categories: [Disruptor]
keywords: "Disruptor"
description: "Disruptor - Getting started"
---

要使用 Disruptor 必須先將套件加入專案中，透過 NuGet 將之載入即可：  

<!-- More -->

{% img /images/posts/DisruptorGettingStarted/1.png %}

<br/>


套件載入後我們就可以開始來使用 Disruptor 了。首先，必須要撰寫 EventHandler，用來消費生產者所生產的資料。撰寫上很簡單，只要實作 IEventHandler 泛型介面即可，泛型介面要指定預期的資料型態，並在 OnEvent 方法中進行資料的處理。  

<br/>


像是如果要在收到資料時顯示一些相關的訊息在主控台上，我們就可像下面這樣撰寫 EventHandler：  

{% codeblock lang:c# %}
... 
public class Data { 
    public string Value { get; set; } 
} 
public class DataEventHandler : IEventHandler<Data> 
{ 
    public string Name { get; private set; } 
    public DataEventHandler(string name) { 
        this.Name = name; 
    } 
    public void OnEvent(Data data, long sequence, bool endOfBatch) { 
        Console.WriteLine("Thread = {0}, Handler = {1}, Sequence = {2}, Value = {3}", Thread.CurrentThread.ManagedThreadId.ToString(), this.Name, sequence, data.Value); 
    } 
} 
...
{% endcodeblock %}

<br/>


EventHandler 好了，接著就是撰寫 Producer 生產資料的部分以及資料怎樣在 Consumer 間流動。  

<br/>


這邊我們必須要了解到 Disruptor 有兩種不同的撰寫方式，一種是 DSL 寫法，一種是 Non-DSL 寫法。  

<br/>


DSL 的寫法比較簡潔，首先要告訴 Disruptor 怎樣初始 Ringbuffer 的每個元素，以及 Ringbuffer 的大小，建立出 Disruptor 的物件實體。接著要決定資料怎樣在 Consumer 間流動。再來要 Start Disruptor，取得 Ringbuffer，然後產生資料往 Ringbuffer 上塞。  

{% img /images/posts/DisruptorGettingStarted/2.png %}

<br/>


程式寫起來就像下面這樣：  

{% codeblock lang:c# %}
... 
var disruptor = new Disruptor.Dsl.Disruptor<Data>(() => new Data(), (int)Math.Pow(2,4), TaskScheduler.Default); 

disruptor.HandleEventsWith(new DataEventHandler("Handler1")); 

var ringBuffer = disruptor.Start(); 
var sequenceNo = ringBuffer.Next(); 
var data = ringBuffer[sequenceNo]; 

data.Value = "Hello"; 
ringBuffer.Publish(sequenceNo); 
sequenceNo = ringBuffer.Next(); 

data = ringBuffer[sequenceNo]; 
data.Value = "World"; 
ringBuffer.Publish(sequenceNo); 

disruptor.Shutdown(); 
...
{% endcodeblock %}

<br/>


{% img /images/posts/DisruptorGettingStarted/3.png %}

<br/>


Non-DSL 寫起來相對複雜些，一樣要告訴 Disruptor 怎樣初始 Ringbuffer 的每個元素，以及 Ringbuffer 的大小，但是這邊改建立出 Ringbuffer，接著要用 EventProcessor 與 Barrier 去設定資料怎樣在 Consumer 間流動，然後要用非同步的方式調用 EventProcessor 的 Run 方法，再來就一樣是產生資料往 Ringbuffer 上塞。  

{% img /images/posts/DisruptorGettingStarted/4.png %}

<br/>


程式寫起來就像下面這樣：  

{% codeblock lang:c# %}
... 
var ringBuffer = RingBuffer<Data>.CreateSingleProducer(() => new Data(), (int)Math.Pow(2, 4)); 
var barrier = ringBuffer.NewBarrier(); 
var eventProcessor = new BatchEventProcessor<Data>(ringBuffer, barrier, new DataEventHandler("Handler1")); 

Task.Factory.StartNew(() => eventProcessor.Run()); 

var sequenceNo = ringBuffer.Next(); 
var data = ringBuffer[sequenceNo]; 
data.Value = "Hello"; 
ringBuffer.Publish(sequenceNo); 

sequenceNo = ringBuffer.Next(); 
data = ringBuffer[sequenceNo]; 
data.Value = "World"; 
ringBuffer.Publish(sequenceNo); 

eventProcessor.Halt(); 

Application.DoEvents(); 
...
{% endcodeblock %}

<br/>


{% img /images/posts/DisruptorGettingStarted/5.png %}

<br/>
