---
title: CAP theorem
date: 2019-05-30 07:36:11
tags:
---

CAP定理 (CAP theorem)，又稱作布魯爾定理 (Brewer's theorem)，指出對於一個分散式系統來說，不可能同時滿足 Consistency、Availability、Partition tolerance 三種特性。  

<!-- More -->

<br/>


Consistency 是一致性，這邊指的是強一致性，描述所有節點都是使用最新的資料副本。也就是說當資料寫入或是更新後，所有節點都是一致且最新的資料。  

</br>


像是如果系統在設計上在收到更新或是寫入的請求後，節點處理完後先進行同步再回應請求，確保資料同步完成，資料在所有節點資料一致，這就是一種符合一致性的設計。   

{% asset_img 1.png %}

</br>


Availability 是可用性，指的是每次發送請求都能在容許的時間內得到回應。但每個節點間的資料可能不是一致且最新的，因此回應的資料可能不是最新的。  

</br>


像是系統收到更新或是寫入的請求，節點處理完後立即回應請求。節點間的同步可能透過排程、訂閱、或是滾資料之類的方式在背後運行，節點間的資料難免有些落差。所以從節點讀取到的資料可能就不會是最新的。    

{% asset_img 2.png %}

</br>


Partition tolerance 是分區容錯，指的是無論網路斷線、節點當機、封包丟失造成系統被切分成不同區塊，系統仍應能繼續服務。  

{% asset_img 3.png %}

</br>


CAP 定理揭露了分散式系統最多只能擁有兩種特性。  

</br>


如果滿足 AP，則系統內的網路或是節點出狀況的情況下，會無法在容許時間內完成通知更新，無法滿足 C。  

{% asset_img 4.png %}

</br>


如果滿足 CP，在網路或是節點出狀況的情況下，為確保一致性，系統會嘗試等待重試，無法在容許時間內回應，無法滿足 A。

{% asset_img 5.png %}

</br>


如果滿足 CA，需要在容許時間內完成資料同步並回應，因此在網路與節點出狀況也要服務的話會無法做到，無法滿足 P。  

{% asset_img 6.png %}

</br>


因為分散式系統中網路與設備都是不可靠的，因此 CAP 中的 P 通常是一定要的，故 CAP 多半是在 CP 與 AP 間取捨，看系統適合往哪邊走。  

</br>


Link
----
* [CAP定理 - 維基百科](https://zh.m.wikipedia.org/zh-tw/CAP定理)
* [CAP 定理的含义](http://www.ruanyifeng.com/blog/2018/07/cap.html
* [分佈式系統理論基礎- CAP](https://www.cnblogs.com/GarfieldEr007/p/9950736.html))
* [Better explaining the CAP Theorem](https://dzone.com/articles/better-explaining-cap-theorem)
