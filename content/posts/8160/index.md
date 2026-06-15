---
title: "[Design Pattern]Template Method模式"
date: "2009-04-24 12:47:14"
description: "[Design Pattern]Template Method模式"
tags: [Design Pattern]
---

## ![image_thumb.png](/images/posts/8160/image_thumb.png)

## 字面意思

Template [ˈtɛmplɪt]

n. 樣板,模板,型板

## 意圖

* 定義一個演算法的架構，將一些步驟延遲到子類別。可不改變其演算法的架構而重新定義它的步驟。

## 口訣

實際處理就交給子類別。

## 問題

要完成一致過程或一系列步驟，但其個別步驟在實現上可能不同。

## 實現方法

1. 建立一個抽象類別，用抽象方法實現一個過程。
2. 在子類別中實現這些抽象方法。

## 示意圖

![image_thumb_1.png](/images/posts/8160/image_thumb_1.png)

![image_thumb_2.png](/images/posts/8160/image_thumb_2.png)
