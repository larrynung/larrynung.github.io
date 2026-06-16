---
title: "[C++]The Purpose of the event_source Attribute"
slug: "cpp-the-purpose-of-the-event-source-attribute"
aliases: ["/posts/63041/"]
date: "2011-12-22 12:12:28"
description: "根據event_source attribute在MSDN上的說明~除了能指定是native還是com的event與一些細部設定外。只有如下的描述： The event_source C++ attribute specifies that the class or structure to…"
tags: [C++]
---

根據event_source attribute在MSDN上的說明~除了能指定是native還是com的event與一些細部設定外。只有如下的描述：

The **event_source** C++ attribute specifies that the class or structure to which it is applied will be an event source

描述中只有提到說這是用來指定類別或是結構是事件的來源，也就是含有事件的類別或結構。

但在實際使用Event時，若是使用的是native的event，沒有加上event_source attribute多半也都能正常的運作，就像筆者在VC.NET Natived Event這篇所帶出的範例：

```c
class TestObj
{
public:
    __event void Executed();
protected:
    void OnExecuted()
    {
        printf("Executed\n");
    }
public:
    void Execute()
    {
        __raise Executed();
    }

    void BindingEvent(){
        __hook(&TestObj::Executed,this,&TestObj::OnExecuted);
    }

    void UnBindingEvent(){
        __hook(&TestObj::Executed,this,&TestObj::OnExecuted);
    }
};
```

在這樣的狀況下，event_source attribute的功用真的不是很好釐清，要說起來就是加上event_source attribute時，編譯器會強迫帶上此attribute的類別或是結構必須要含有event宣告，若是類別或是結構裡面無event的存在，編譯器會發出error告知程式開發人員。

![image_thumb.png](/images/posts/63041/image_thumb.png)

除此之外，在event_source attribute不加的狀態，程式可能本來都好好的可以建置，當為類別或是結構新增一個事件時，編譯突然會發生問題，且編譯器顯示的錯誤都不是目前在改的類別或結構，而是一些沒動到且看起來都沒錯誤的地方時，可嚐試為類別或結構加上event_source attribute再編譯看看。

```c
[event_source]
class TestObj
{
	...
};
```

## Link

* event_source
* VC.NET Natived Event
