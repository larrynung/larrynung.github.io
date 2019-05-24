---
title: Redis - Reliable queue pattern
date: 2019-05-23 22:50:34
tags: [Redis]
---

系統中如果有使用到 Redis，有時會碰到要將 Redis 內資料落地的情境。這時可能會用 Redis 的 List 做一個簡單的 Queue，將資料以先進先出的方式處理。    

<!-- More -->

{% asset_img 1.png %}

<br/>


這樣的做法看似運作良好，但隱藏著一個潛在的問題。如果今天從 Redid 取出資料還未處理就發生錯誤，可能是機器當機重啟那種錯誤，就會有丟失資料的現象發生。  

<br/>


為了解決這樣的問題，可以套用 Reliable queue pattern，當資料確實被處理完才從 Redis 內移除。  

{% asset_img 2.png %}

<br/>


實作方式會變得稍微複雜了一點，簡單的說就是把資料的 Id 放在 List 之類的結構，實際的資料放在 Value，當你 Deque 時將 Id 從 Pendding 放到 Working，處理完才從 Working 清掉，順帶將 Value 對應的資料刪掉。  

<br/>


實作上通常 Pending 與 Working 會用 List 結構去實作，Value 會用 Hash 結構。  

{% asset_img 3.png %}

<br/>


當資料要從 Redis 取出處理時，會先查看 Working 是否已經有資料，如果 Working 已經有資料，可能代表之前處理到一半之類的，這時資料直接由 Working 反查 Value 後吐回。  

<br/>


如果 Working 沒資料，會從 Pending 將需要處理的 Id 透過 rpoplpush 命令轉到 Working，然後反查 Value 吐回。

<br/>


資料處理完要將資料從 Redis 移除時，會將 Working 與 Value 中對應的資料移除。  

<br/>


需注意到套用 Reliable queue pattern 時，可能會依情境、需求、產品特性可能會有不同的變體，使用的資料結構也可視需要調動。    

<br/>


像是如果資料處理失敗走一定次數是否從 Working 轉到 Fail，避免處理一直卡住。  

{% asset_img 4.png %}

</br>


若是考慮到 Sharding 的話 Working 還需要 by Worker 散開，
且還需要有當 worker 死掉的接手機制。  

{% asset_img 5.png %}
