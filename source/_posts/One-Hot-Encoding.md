---
title: One-Hot Encoding
date: 2018-06-26 23:06:00
tags: [Machine Learning]
---

One-Hot Encoding 是一編碼方式，使用 N 位狀態寄存器來對 N 個狀態進行編碼，常被用於機器學習中的資料前處理，特別是無序的類別資料。  

<!-- More -->

<br/>


像是性別資料 Male 與 Female，雖然可以用數值編碼將之編成 0 與 1 之類的數值。  

    Male   => 0
    Female => 1

<br/>


但是這樣會讓這些無序資料距離原點的距離有所差異。  

<br/>


如果改用 One-Hot Encoding，假設維度 1 用來表示是否為 Female，維度 2 用來表示是否為 Male，那這些無序資料距離原點的距離就都會是 1。  

    Male   => 01
    Female => 10

<br/>


Link
----
* [特徵提取方法: one-hot 和 IF-IDF - 掃文資訊](https://hk.saowen.com/a/d6fe218d0c77aeb141977301f03845d3f49a8bc29792f9a1f0ff6dbc40a9f32f)
* [One-hot - Wikipedia](https://en.wikipedia.org/wiki/One-hot)
* [Why One-Hot Encode Data in Machine Learning?](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/)
* [[資料分析&機器學習] 第2.4講：資料前處理(Msssing data, One-hot encoding, Feature Scaling)](https://medium.com/@yehjames/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-4%E8%AC%9B-%E8%B3%87%E6%96%99%E5%89%8D%E8%99%95%E7%90%86-missing-data-one-hot-encoding-feature-scaling-3b70a7839b4a)
