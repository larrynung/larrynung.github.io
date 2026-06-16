---
title: "[Design Pattern]Singleton Pattern"
slug: "design-pattern-singleton-pattern"
aliases: ["/posts/8159/"]
date: "2009-04-24 12:41:59"
description: "字面意思 Singleton [ˈsɪŋgḷtən] n.獨生子，獨身，單件 意圖 保證一個類別只有一個物件實體。 希望所有物件使用該物件相同的物件參考，且無需將物件參考傳遞給他們。 口訣 單一的執行個體 問題 幾個不同的物件需要引用同一物件，且希望確保這類型的物件數不超過一個。"
tags: [Design Pattern]
---

## ![image_thumb_1.png](/images/posts/8159/image_thumb_1.png)

## 字面意思

Singleton [ˈsɪŋgḷtən]

n.獨生子，獨身，單件

## 意圖

* 保證一個類別只有一個物件實體。
* 希望所有物件使用該物件相同的物件參考，且無需將物件參考傳遞給他們。

## 口訣

單一的執行個體

## 問題

幾個不同的物件需要引用同一物件，且希望確保這類型的物件數不超過一個。

## 效果

使用上無需操心是否已存在Singleton物件實體。這是由Singleton自己控制的。

## 實現方法

1. 添加一個類別的私有靜態成員變數，初值為NULL。
2. 添加一個公有的靜態方法，當成員變數值為NULL時建立物件實體並回傳。
3. 將建構子設為保護或私有，防止直接建立該類別的物件實體。

## 示意圖

![image_thumb.png](/images/posts/8159/image_thumb.png)

![image_thumb_2.png](/images/posts/8159/image_thumb_2.png)
