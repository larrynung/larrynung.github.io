---
layout: post
title: "Disruptor - Ringbuffer"
date: 2016-03-12 08:06
comments: true
categories: [Disruptor]
keywords: "Disruptor"
description: "Disruptor - Ringbuffer"
---

Ringbuffer 是 Disruptor 的核心部分，使用 Disruptor 一定會圍繞著 Ringbuffer，Producer 會往 Ringbuffer 塞資料，Consumer 會從 RingBuffer 消費資料，我必須要觀察 Ringbuffer 的使用狀況並視情況調整架構或是其大小。所以使用 Disruptor 必須要對 Ringbuffer 有一定的認知。  

<!-- More -->

{% img /images/posts/DisruptorRingbuffer/1.png %}

<br/>


Ringbuffer 是一頭尾串接的環形陣列，資料一邊循序的存放，一邊循序的消耗。就像下面這樣：  

{% img /images/posts/DisruptorRingbuffer/2.gif %}

<br/>


存放在內部的資料都會有一個對應的編號，用 sequence % buffer size 就可以知道資料存放在陣列的哪個位置，但 Disruptor Ringbuffer 這邊是用 Sequence & (buffer size - 1) 的方式去做，以取得較佳的效能，但 buffer size 必須為 2 ^ n。  

<br/>


這邊簡單的做個測試...  

{% codeblock lang:c# %}
usingSystem;
usingSystem.Diagnostics;

namespaceConsoleApplication25 {
    classProgram {
        staticvoidMain(string[] args) {
            varcounts = newint[] {
                10,
                100,
                1000,
                10000,
                100000,
                1000000,
                10000000,
                100000000,
                1000000000
            };

            foreach(varcountincounts) {
                Console.WriteLine("{0}count", count);
                Console.WriteLine("10 % 2:{0}ms", DoTest(count, () => {
                    varvalue = 10 % 2;
                }));

                Console.WriteLine("10 & (2 - 1):{0}ms", DoTest(count, () => {
                    varvalue = 10 & (2 - 1);
                }));
                Console.WriteLine();
            }
        }

        staticlongDoTest(intcount, Actionaction) {
            varsw = Stopwatch.StartNew();
            for (inti = 0; i < count; ++i) {
                action();
            }

            returnsw.ElapsedMilliseconds;
        }
    }
}
{% endcodeblock %}

<br/>


{% img /images/posts/DisruptorRingbuffer/3.png %}

<br/>


{% img /images/posts/DisruptorRingbuffer/4.png %}

<br/>


可以看到這樣的設計的確有著較佳的效能，雖然不多，但是因為 Ringbuffer 使用頻繁，累積起來也很可觀。  

<br/>


除了演算法上改進帶來的效益外，Disrptor 的 Ringbuffer 之所以高效，是因為底層是用陣列下去實作，在記憶體中會被連續存放，有利於 CPU 的快取，不會頻繁的去主記憶體撈取資料。另外就是 Disruptor Ringbuffer 與其每個位置的元素都是預先配置記憶體的，整個運作過程不會再另行配置，只重複使用已經配置好的，不會讓 GC 忙於回收。  

<br/>


Link
----
* [環形緩衝區 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E7%92%B0%E5%BD%A2%E7%B7%A9%E8%A1%9D%E5%8D%80)
* [剖析Disruptor:为什么会这么快？（一）Ringbuffer的特别之处 | 并发编程网 - ifeve.com](http://ifeve.com/dissecting-disruptor-whats-so-special/)
