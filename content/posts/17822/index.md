---
title: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (四) Contract.ForAll & Contract.Exists"
date: "2010-09-20 05:32:47"
description: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (四) Contract.ForAll & Contract.Exists"
tags: [CSharp]
---

為了方便處理集合類型變數的合約驗證，Code Contracts貼心的提供了Contract.ForAll與Contract.Exists兩個輔助用的合約方法，可與前置條件或後置條件搭配使用。

## Contract.ForAll

Contract.ForAll合約方法可用來判斷集合內部的所有項目是否皆滿足所要驗證的條件，其運作規則如下：

- 集合內任何元素帶入運算為False=>ForAll動作停止，回傳False
- 集合內所有元素帶入運算皆為True=>回傳True

撰寫時可用Contract.ForAll方法表示，主要有下列兩個多載函式：

![clip_image001_thumb.png](/images/posts/17822/clip_image001_thumb.png)

使用上可直接對其帶入集合物件與要驗證的條件，像是要驗證集合內部所內含的項目是否皆不為空，我們就可以撰寫如下驗證程式：

```csharp
public int Foo(IEnumerable xs){
Contract.Requires(Contract. ForAll (xs , x => x != null) );
}
```

而若只想驗證集合內的某一區間，不想驗證集合內所有項目時，可考慮利用另一多載方法帶入所要驗證的區間範圍，像是：

```csharp
public int Foo(T[] xs){
Contract. Requires ( Contract. ForAll (0,xs.Length,
index => xs[index] != null));
}
```

## Contract.Exists

Contract.Exists合約方法是用來判斷集合內的項目是否有符合驗證條件的項目，其運作規則如下：

- 集合內任何元素帶入運算為True=>Exists動作停止，回傳True
- 集合內所有元素帶入運算皆為False=>回傳False

撰寫時可用 Contract.Exists方法表示，該方法與Contract.ForAll合約一樣有兩個多載函式：

![clip_image002_thumb.png](/images/posts/17822/clip_image002_thumb.png)

使用上也十分的類似

```csharp
public int Foo(IEnumerable xs){
Contract.Requires(Contract. Exists(xs , x => x != null) );
}
```

## Link

- Contract.ForAll 方法
- Contract.Exists 方法
