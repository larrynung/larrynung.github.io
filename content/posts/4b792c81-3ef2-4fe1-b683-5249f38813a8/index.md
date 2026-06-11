---
title: "[C#]BigInteger"
slug: "[CSharp]BigInteger"
date: "2013-11-06 12:00:00"
description: "[C#]BigInteger"
---

今天看書才知道原本.NET 3.5中偷藏了一個BinInteger類型，可用來顯示很長的整數。該類型在.NET Framework 3.5 Beta1中就已被加入,但是Release版中該類型被改為Internal類型，導致無法直接使用。根據網路上的資料顯示，據說是微軟認為該類型還有很多問題，因此暫不開放。但我們仍可透過.NET反射機制去使用它。

簡易範例如下：

執行結果如下：

## Conclusion


上網搜了一下，好像直接這樣使用的人並不多。多半是使用自己寫的類別來達到此需求。像是Code Project上這篇。

## 相關連結


Code Project-C# BigInteger Class