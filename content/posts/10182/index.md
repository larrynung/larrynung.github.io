---
title: "[C#][VB.NET].NET 4.0 Barrier Class"
slug: "[CSharp][VB.NET].NET 4.0 Barrier Class"
date: "2009-08-22 05:32:32"
description: "[C#][VB.NET].NET 4.0 Barrier Class"
tags: [VB.NET, CSharp]
---

## Introduction

.NET 4.0後在System.Threading命名空間中新加入了Barrier類別，該類別的功能就如同字面意義一樣，可視為是一個關卡或是剪票口。透過Barrier Class我們可以管制執行緒的運作，做到執行緒同步的效果。

## 字面意思

Barrier [`bærIL]

n.剪票口;海關關卡;障礙物;路障,柵欄

## Support

* .NET Framework 4.0 (C# 4.0、VB.NET 10.0) or latter

## Assembly

System (in System.dll)

## Namespace

System.Threading

## Barrier Class

Barrier Class在使用上十分的簡單，只要宣告Barrier物件並在[建構函式](http://msdn.microsoft.com/en-us/library/system.threading.barrier.barrier(VS.100).aspx)帶入participantCount(簡單的說就是要等待的執行緒個數)，並在要同步的點叫用[SignalAndWait](http://msdn.microsoft.com/en-us/library/system.threading.barrier.signalandwait(VS.100).aspx)即可。

![image_thumb_3.png](/images/posts/10182/image_thumb_3.png)

執行緒會在叫用[SignalAndWait](http://msdn.microsoft.com/en-us/library/system.threading.barrier.signalandwait(VS.100).aspx)後會暫停運行，等待所有要參與的執行緒都到了同步點才繼續往下運行。

舉個例子來看，假設今天Charlie、Mac、Dennis三個人相約要去西雅圖喝咖啡。由於三個人的住的地區不盡相同，且車子都需要加油，因此他們約在途中會經過的加油站待會合後一同前往。

![image_thumb.png](/images/posts/10182/image_thumb.png)

這樣的情境我們可以透過Thread與Barrier用程式加以模擬出來

VB.NET

```vb
Imports System.Threading

Module Module1

    Private sync As Barrier

    Sub Main(ByVal args() As String)
        sync = New Barrier(3)

        Dim charlie = New Thread(Sub() DriveToBoston("Charlie", TimeSpan.FromSeconds(1)))
        charlie.Start()
        Dim mac = New Thread(Sub() DriveToBoston("Mac", TimeSpan.FromSeconds(2)))
        mac.Start()
        Dim dennis = New Thread(Sub() DriveToBoston("Dennis", TimeSpan.FromSeconds(3)))
        dennis.Start()

        charlie.Join()
        mac.Join()
        dennis.Join()

        Console.ReadKey()
    End Sub

    Sub DriveToBoston(ByVal name As String, ByVal timeToGasStation As TimeSpan)

        Console.WriteLine("[{0}] Leaving House", name)

        ' Perform some work
        Thread.Sleep(timeToGasStation)
        Console.WriteLine("[{0}] Arrived at Gas Station", name)

        ' Need to sync here
        sync.SignalAndWait()

        ' Perform some more work
        Console.WriteLine("[{0}] Leaving for Gas Station", name)

    End Sub

End Module
```

C#

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace BarrierDemo
{
    class Program
    {
        static Barrier sync;

        static void Main(string[] args)
        {
            sync = new Barrier(3);

            var charlie = new Thread(() => DriveToBoston("Charlie", TimeSpan.FromSeconds(1))); charlie.Start();
            var mac = new Thread(() => DriveToBoston("Mac", TimeSpan.FromSeconds(2))); mac.Start();
            var dennis = new Thread(() => DriveToBoston("Dennis", TimeSpan.FromSeconds(3))); dennis.Start();

            charlie.Join();
            mac.Join();
            dennis.Join();

            Console.ReadKey();
        }

        static void DriveToBoston(string name, TimeSpan timeToGasStation)
        {
            Console.WriteLine("[{0}] Leaving House", name);

            // Perform some work
            Thread.Sleep(timeToGasStation);
            Console.WriteLine("[{0}] Arrived at Gas Station", name);

            // Need to sync here
            sync.SignalAndWait();

            // Perform some more work
            Console.WriteLine("[{0}] Leaving for Gas Station", name);

        }
    }
}
```

運行結果
![image_thumb_1.png](/images/posts/10182/image_thumb_1.png)

若是不使用Barrier去同步，這邊我們可以拿掉sync.SignalAndWait()再做一次運行，則三個人就會變成各自前往西雅圖喝咖啡了。
![image_thumb_2.png](/images/posts/10182/image_thumb_2.png)

## Link

* [MSDN - Barrier Class](http://msdn.microsoft.com/en-us/library/system.threading.barrier(VS.100).aspx)
* [StackOverFlow - Difference between Barrier in C# 4.0 and WaitHandle in C# 3.0?](http://stackoverflow.com/questions/990970/difference-between-barrier-in-c-4-0-and-waithandle-in-c-3-0)
* [Managed World - An Intro to Barrier](http://www.managed-world.com/archive/2009/02/09/an-intro-to-barrier.aspx)
