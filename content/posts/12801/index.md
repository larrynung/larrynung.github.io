---
title: "[C#]Give Different Random Objects Different Seeds"
slug: "csharp-give-different-random-objects-different-seeds"
aliases: ["/posts/csharp不同的random物件給予不同的亂數種子/"]
date: "2010-01-04 10:41:36"
description: ".NET Framework中，Random類別的建構函式有兩個。一個是不需帶參數的建構函式，使用其建構函式會使用時間相依預設種子值來初始化 Random 類別的新執行個體。其亂數種子是依系統時鐘衍生而來，解析度有限。"
tags: [CSharp]
---

.NET Framework中，Random類別的建構函式有兩個。一個是不需帶參數的建構函式，使用其建構函式會使用時間相依預設種子值來初始化 Random 類別的新執行個體。其亂數種子是依系統時鐘衍生而來，解析度有限。若在極短的時間內頻繁叫用，會使得Random物件的亂數種子皆相同，因此得到完全相同的亂數組。另一個則是帶有一個參數的建構函式，可讓使用者自行帶入亂數種子。

要讓不同的Random物件產生不同的亂數組，我們必須要做的是給予不同的Random物件不同的亂數種子。以往像這樣的需求我會這摸寫：

```csharp
Random r = new Random(DateTime.Now.Millisecond);
```

但在回應網友問題時才發現，使用這種寫法並無法有效的解決亂數重複問題。

後來再度嚐試MSDN的方法

```csharp
Random Counter = new Random(unchecked((int)(DateTime.Now.Ticks >> ctr)));
```

在極短的時間內一樣是無法有效的取得不同的亂數種子。最後想到用GUID的HashCode來當亂數種子帶入才能有效解決這問題。

```csharp
Random Counter = new Random(Guid.NewGuid().GetHashCode());
```

之所以能這樣寫是因為亂數種子必須要在極短的時間內帶入不同的值，而GUID剛好能有效的產生不重複的識別值，HashCode又是用來當作雜湊的Key，相同物件才會有相同的HashCode，因此GUID的HashCode剛好就能有效的產生不同的整數值作為亂數種子。Google了一下，這方法在對岸及國外都有在用，所以應該是沒有問題。

除此之外，我們也可以自行設計其它的演算法來取得不同的亂數種子，就像這篇討論所探討的。

## Link

* Random 建構函式
* 關於亂數 Random 問題
* C#概念釐清，我的問題出在哪裡 ?
