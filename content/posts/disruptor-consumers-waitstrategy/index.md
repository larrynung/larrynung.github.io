---
title: "Disruptor - Consumer's WaitStrategy"
date: "2016-03-20 12:17:00"
description: "Disruptor - Consumer's WaitStrategy"
tags: [Disruptor]
---


Disruptor 內建幾種等待策略，可用以設定消費者怎樣等待生產者的資料。在實務上，我們可能要針對不同的產品特性下去調整等待的策略。    

<!-- More -->

<br/>


預設的等待策略為 BlockingWaitStrategy，內部是用 Lock 與條件變數下去實作，用於對低延遲與高產能不是那麼重視的情境。雖然產能不高，但能確保在不同的環境下有一致的性能表現。  

<br/>


這邊筆者做了簡單的測試，在 Unicast 1p-1c 的狀況下瘋狂寫入，每秒約處理 145 筆資料。    

{% img /images/posts/DisruptorWaitStrategy/1.png %}

<br/>


如果讓 Producer 不要那麼頻繁的產生資料，那會看到消費者在等待的同時 CPU 會忙於等待。  

{% img /images/posts/DisruptorWaitStrategy/2.png %}

<br/>


SleepingWaitStrategy 策略則是用迴圈下去睡眠等待。可以看到這邊的實驗，每秒處理可達到約 18xxxx 筆資料。  

{% img /images/posts/DisruptorWaitStrategy/3.png %}

<br/>


且等待生產者資料時 CPU 耗費也不高。  

{% img /images/posts/DisruptorWaitStrategy/4.png %}

<br/>


BusySpinWaitStrategy 策略套到同樣的實驗，每秒處理約 144 筆資料。  

{% img /images/posts/DisruptorWaitStrategy/5.png %}

<br/>


等待資料時 CPU 也是飆高狀態。  

{% img /images/posts/DisruptorWaitStrategy/6.png %}

<br/>


YieldingWaitStrategy 策略套到同樣的實驗，每秒處理約 24xxxx 筆資料.
  

{% img /images/posts/DisruptorWaitStrategy/7.png %}

<br/>


等待資料時 CPU 依舊飆高。

{% img /images/posts/DisruptorWaitStrategy/8.png %}

<br/>

Link
----
* [BlockingWaitStrategy (Disruptor API)](https://lmax-exchange.github.io/disruptor/docs/com/lmax/disruptor/BlockingWaitStrategy.html)
* [SleepingWaitStrategy (Disruptor API)](https://lmax-exchange.github.io/disruptor/docs/com/lmax/disruptor/SleepingWaitStrategy.html)
* [BusySpinWaitStrategy (Disruptor API)](https://lmax-exchange.github.io/disruptor/docs/com/lmax/disruptor/BusySpinWaitStrategy.html)
* [YieldingWaitStrategy (Disruptor API)](https://lmax-exchange.github.io/disruptor/docs/com/lmax/disruptor/YieldingWaitStrategy.html)
