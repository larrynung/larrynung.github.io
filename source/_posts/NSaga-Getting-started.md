---
title: NSaga - Getting started
date: 2019-04-12 14:22:45
tags: [Saga, NSaga]
---

使用 NSaga 來做 Saga pattern，需先透過 NuGet 安裝 NSaga 套件。  

<!-- More -->

    PM> Install-Package NSaga

<br/>


接著要定義 Transaction 中的每一個動作，也就是 NSaga 中的 Message。  

<br/>


這邊要注意 NSaga 必須特別定義 Transaction 中的第一個 Message，定義的方式就是造一個專屬的 Message Class，並實作 IInitiatingSagaMessage 介面。  

```C#
public class StartSagaMessage: IInitiatingSagaMessage
{
    public Guid CorrelationId { get; set; }
}
```

<br/>

IInitiatingSagaMessage 介面只有一個屬性 CorrelationId，用來接 Transaction Id 用，可用來識別這次觸發的 Transaction。除了介面定義的屬性外，若是需要額外的資料也可以自己附加。  

<br/>   


第一個 Message 定義完其它後面的 Message 定義方式就一樣了，只要造專屬的 Message Class，並實作 ISagaMessage 介面即可。   

```C#
public class SagaMessage: ISagaMessage
{
    public Guid CorrelationId { get; set; }
}
```

<br/>


接著要定義 Transaction 要儲存的資訊，簡單造個 Model 類別即可。  

```C#
public class SagaData
{
    public List<string> Executed { get; } = new List<string>();
}
```

<br/>


再來要定義 Transaction，也就是 NSaga 中的 Saga。造一個專屬的 Saga Class，實作 ISaga<T>、InitatedBy<T>、ConsumerOf<T> 介面。  

```C#
public class Saga: ISaga<SagaData>, InitiatedBy<StartSagaMessage>, ConsumerOf<SagaMessage>
{
    ...
}
```

<br/>


Transaction 的 Message 由 InitatedBy<T>、ConsumerOf<T> 介面實作去定義，Transaction的第一個 Message 用 InitatedBy<T> 去實作，其他的 Message 都用 ConsumerOf<T> 介面去實作，對應的實作方法用來定義執行對應 Message 時所要做的動作。  

```C#
...
public OperationResult Initiate(StartSagaMessage message)
{
    Console.WriteLine(message.GetType().Name);
    SagaData.Executed.Add(message.GetType().Name);

    return new OperationResult();
}
...
```

<br/>


像是下面這樣：  

```C#
public class Saga: ISaga<SagaData>, InitiatedBy<StartSagaMessage>, ConsumerOf<SagaMessage>
{
    public Guid CorrelationId { get; set; }
    public Dictionary<string, string> Headers { get; set; }
    public SagaData SagaData { get; set; }
    public OperationResult Initiate(StartSagaMessage message)
    {
        Console.WriteLine(message.GetType().Name);
        SagaData.Executed.Add(message.GetType().Name);

        return new OperationResult(); 
    }

    public OperationResult Consume(SagaMessage message)
    {
        Console.WriteLine(message.GetType().Name);
        SagaData.Executed.Add(message.GetType().Name);
        
        return new OperationResult(); 
    }
}
```

<br/>


最後開始實際運行，取得 mediator 與 repository。  

```C#
...
var builder = Wireup.UseInternalContainer();
var mediator = builder.ResolveMediator();
var repository = builder.ResolveRepository();
...
```

<br/>


透過 mediator 依序調用 Message 即可。  

```C#
...
mediator.Consume(new StartSagaMessage()
{
    CorrelationId = correlationId,
});
...
```

<br/>


若有需要可從 repository 取出儲存的資料。  

```C#
...
var saga = repository.Find<Saga>(correlationId);
...
```

<br/>


像是下面這樣：  

```C#
using System;

namespace NSaga.Demo
{
    class Program
    {
        static void Main(string[] args)
        {
            var builder = Wireup.UseInternalContainer();
            var mediator = builder.ResolveMediator();
            var repository = builder.ResolveRepository();
            
            var correlationId = Guid.NewGuid();

            mediator.Consume(new StartSagaMessage()
            {
                CorrelationId = correlationId,
            });

            mediator.Consume(new SagaMessage()
            {
                CorrelationId = correlationId
            });

            var saga = repository.Find<Saga>(correlationId);

            Console.WriteLine(string.Join(", ", saga.SagaData.Executed.ToArray()));
        }
    }
}
```

{% asset_img 1.png %}

<br/>


Link
----
* [Quick Start · AMVSoftware/NSaga Wiki](https://github.com/AMVSoftware/NSaga/wiki/Quick-Start)
