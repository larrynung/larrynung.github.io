---
title: "[C#]C# 4.0 具名參數 (Named Parameters)"
slug: "[CSharp]C# 4.0 具名參數 (Named Parameters)"
date: "2009-07-30 09:05:43"
description: "Introduction 具名參數是C# 4.0的特色之一，可搭配選擇性參數使用，主要功能是讓使用者可在呼叫函數時指定傳入的值要帶入哪個參數。 Support C# 4.0 or latter 使用方式 當我們想指定傳入的值要帶入的參數時，我們可以透過\":\"關鍵字來使用具名參數。"
tags: [CSharp]
---

## Introduction

具名參數是C# 4.0的特色之一，可搭配選擇性參數使用，主要功能是讓使用者可在呼叫函數時指定傳入的值要帶入哪個參數。

## Support

* C# 4.0  or latter

## 使用方式

當我們想指定傳入的值要帶入的參數時，我們可以透過":"關鍵字來使用具名參數。

舉個例子來說，當我們有道函式其函式原型如下：

```csharp
public Person(string name, SexType sex = SexType.Boy, int year = 18)
```

若只想輸入名字與年紀，我們可以像這樣寫：

```csharp
Person larry = new Person("Larry", year:29);
```

或是

```csharp
Person larry = new Person(name:"Larry", year:29);
```

也可以不照順序輸入參數

```c
Person larry = new Person(year:29, name:"Larry");
```

> 在VB.NET 8.0中也有提供對應的用法，使用的關鍵字為":="。

####

## Video

下面列出一些網路上的示範影片，有興趣的可以順便看一下。

![video3329c488da15.jpg](/images/posts/9732/video3329c488da15.jpg)

![video7e6ac25a3a9d.jpg](/images/posts/9732/video7e6ac25a3a9d.jpg)

![videoaade64e08bd3.jpg](/images/posts/9732/videoaade64e08bd3.jpg)

## Link

* C# 4.0 新特性：動態型別、選用參數、具名參數
* C# 4.0 Named Parameters for better code quality
* New Features in C# 4.0
* C# 4.0's New Features Explained
