---
title: "[Design Pattern]Strategy模式"
date: "2009-04-07 12:50:05"
description: "[Design Pattern]Strategy模式"
tags: [Design Pattern]
---

## ![image_thumb.png](/images/posts/7899/image_thumb.png)

## 字面意思

strategy [ˈstrætidʒi]

n.戰略，策略

## 意圖

* 根據情況的不同，採用不同的演算法則。
* 使演算法可獨立於使用它的客戶而變化。
* 定義一系列的演算法，把它們一個個封裝起來，並使它們可相互替換。

## 口訣

把演算法則整個換掉。

## 問題

需要依客戶或是數據的不同採用不同的演算法則。

## 效果

* 定義了一系列的演算法則。
* 可不使用Switch或判斷陳述式。
* 必須以相同的方式叫用所有的演算法。
* 必須擁有相同的接口。

## 實現方法

1. 定義一個抽象類。
2. 每個繼承該抽象類的子類別需按需求實現演算法。

## 相關連結

* Wiki-Strategy Pattern

![image_thumb_1.png](/images/posts/7899/image_thumb_1.png)
