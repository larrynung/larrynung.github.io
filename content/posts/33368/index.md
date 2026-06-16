---
title: "[C#]RaiseEvent Extension Method (Part 2)"
slug: "csharp-raiseevent-extension-method-part-2"
aliases: ["/posts/csharpraiseevent-extension-method-二/"]
date: "2011-08-17 06:52:51"
description: "前面[C#]RaiseEvent Extension Method (一)這篇介紹了如何用擴充方法來簡化C#事件的觸發動作，最近在做觸發事件時，又看到了一個引起我關注的重點，那就是有時候我們在初始化事件的參數時費了很大的耗費，準備觸發事件時，透過OnXXX去觸發事件，結果發現事件並未被繫上，"
tags: [CSharp]
---

前面[C#]RaiseEvent Extension Method (一)這篇介紹了如何用擴充方法來簡化C#事件的觸發動作，最近在做觸發事件時，又看到了一個引起我關注的重點，那就是有時候我們在初始化事件的參數時費了很大的耗費，準備觸發事件時，透過OnXXX去觸發事件，結果發現事件並未被繫上，整個事件觸發的動作就不做了，那麼前面所作的參數準備不就是不必要的耗費?

```csharp
...
Var e = new MyEventArgs() {...};
...
OnMyEvent(e);
...
```

當然這樣的問題可以在觸發事件的地方用if判別去避開，但這樣就會讓程式在維護與閱讀上的困難度上升，筆者在[.Net Concept]理解事件的宣告方式與用法這篇有對此做詳細的描述，這邊不多做解釋。

因為有上面的原因，筆者又花了一點時間將擴充方法做了些改進，增加兩個多載版本，使其能帶入初始化事件參數的方法，如此在事件未繫上時就不會做初始的動作。

```csharp
public static class ObjectExtension
{
    public static void RaiseEvent(this object obj, EventHandler handler, EventArgs e)
    {
        RaiseEvent(obj, handler, () => e);
    }

    public static void RaiseEvent(this object obj, EventHandler handler, Func<EventArgs> func)
    {
        if (handler == null)
            return;
        handler(obj, func());
    }

    public static void RaiseEvent<TEventArgs>(this object obj, EventHandler<TEventArgs> handler, TEventArgs e) where TEventArgs : EventArgs
    {
        RaiseEvent(obj, handler, () => e);
    }

    public static void RaiseEvent<TEventArgs>(this object obj, EventHandler<TEventArgs> handler,Func<TEventArgs> func) where TEventArgs : EventArgs
    {
        if (handler == null)
            return;
        handler(obj, func());
    }
}
```

使用上透過Lambda的輔助也十分的好上手。

```csharp
this.RaiseEvent(MyEvent, () => new MyEventArgs()
{
	//Init EventArgs
	...
 });
```

完整的範例程式如下：

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication14
{
    class Program
    {
        static void Main(string[] args)
        {
            Person Larry = new Person();
            Larry.NameChanged += new EventHandler<NameEventArgs>(Larry_NameChanged);
            Larry.Name = "Larry";
        }
        static void Larry_NameChanged(object sender, NameEventArgs e)
        {
            Console.WriteLine(string.Format("NameChanged to {0}", e.Name));
        }
    }
    public static class ObjectExtension
    {
        public static void RaiseEvent(this object obj, EventHandler handler, EventArgs e)
        {
            RaiseEvent(obj, handler, () => e);
        }

        public static void RaiseEvent(this object obj, EventHandler handler, Func<EventArgs> func)
        {
            if (handler == null)
                return;
            handler(obj, func());
        }

        public static void RaiseEvent<TEventArgs>(this object obj, EventHandler<TEventArgs> handler, TEventArgs e) where TEventArgs : EventArgs
        {
            RaiseEvent(obj, handler, () => e);
        }

        public static void RaiseEvent<TEventArgs>(this object obj, EventHandler<TEventArgs> handler,Func<TEventArgs> func) where TEventArgs : EventArgs
        {
            if (handler == null)
                return;
            handler(obj, func());
        }
    }

    class NameEventArgs : EventArgs
    {
        public string Name { get; set; }
    }

    class Person
    {
        private string _name;
        public string Name
        {
            get
            {
                if (_name == null)
                    return string.Empty;
                return _name;
            }
            set
            {
                if (_name != value)
                {
                    _name = value;
                    this.RaiseEvent(NameChanged, () => new NameEventArgs() { Name = value });
                }
            }
        }
        public event EventHandler<NameEventArgs> NameChanged;
    }

}
```

運行的結果如下：

![image_thumb.png](/images/posts/33368/image_thumb.png)
