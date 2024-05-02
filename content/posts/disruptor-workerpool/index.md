---
title: "Disruptor - WorkerPool"
date: "2016-03-30 23:45:00"
description: "Disruptor - WorkerPool"
tags: [Disruptor]
---


Disruptor 的 EventHandler，Consumer 間會相互合作，會依序消費收到所有的資料。但有的場景我們可能會需要多個 Consumer 分攤處理收到的資料，這時可以採用 WorkerHandler。    

<!-- More -->

<br/>


像是我們可以撰寫下面這樣的 WorkerHandler：  

```c#
...
public class Data
{
    public string Value { get; set; }
}

public class DataWorkHandler : IWorkHandler<Data >
{
    public string Name { get; private set; }
    public DataWorkHandler( string name)
    {
        this.Name = name;
    }
    public void OnEvent( Data @event)
    {
        Console.WriteLine( "Thread = {0}, Handler = {1}, Value = {2} ", Thread.CurrentThread.ManagedThreadId.ToString(), this.Name, @event.Value);
    }
}
...
```

<br/>


這邊建造多個 WorkerHandler，帶入 Disruptor 的 HandleEventsWithWorkerPool 方法。  
```c#
...
var disruptor = new Disruptor.Dsl. Disruptor< Data>(() => new Data(), (int)Math .Pow(2, 10), TaskScheduler.Default, ProducerType.SINGLE, new YieldingWaitStrategy());

var workers = new IWorkHandler<Data>[]{
    new DataWorkHandler("Handler1"),
    new DataWorkHandler("Handler2"),
    new DataWorkHandler("Handler3")};

disruptor.HandleEventsWithWorkerPool(workers);

var ringBuffer = disruptor.Start();
            
while (true)
{
    var sequenceNo = ringBuffer.Next();
    var data = ringBuffer[sequenceNo];
    data.Value = sequenceNo.ToString();
    ringBuffer.Publish(sequenceNo);
    Thread.Sleep(250);
}

disruptor.Shutdown();
...
```

<br/>


運作時可以看到收到的資料是被分攤處理的。  

{% img /images/posts/DisruptorWorkerPool/1.png %}
