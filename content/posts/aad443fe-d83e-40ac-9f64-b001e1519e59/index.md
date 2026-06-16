---
title: "[C#][CodePlex]LevelUp Serializer"
slug: "csharp-codeplex-levelup-serializer"
aliases: ["/posts/csharpcodeplexlevelup-serializer/"]
date: "2013-11-06 12:00:00"
description: "因為網路上的函式庫都不太合手，想整理個自己用的序列化函式庫已經有兩三年了，不是想做多大的函式庫，但卻也遲遲沒有毅力將這完成。直到這幾天才將寫到一半的函式庫打開來繼續撰寫、調整、測試，終於擠出了第一版本，目前已經可在CodePlex的LevelUp Serializer頁面中看到。"
tags: [CSharp]
---

因為網路上的函式庫都不太合手，想整理個自己用的序列化函式庫已經有兩三年了，不是想做多大的函式庫，但卻也遲遲沒有毅力將這完成。直到這幾天才將寫到一半的函式庫打開來繼續撰寫、調整、測試，終於擠出了第一版本，目前已經可在CodePlex的LevelUp Serializer頁面中看到。

![image_thumb.png](/images/posts/aad443fe-d83e-40ac-9f64-b001e1519e59/image_thumb.png)

以這函式庫來說大概有以下幾個特點

1. Ease of use
2. Supports almost all serializer, like Binary、Xml、Soap、Json、DataContract.
3. Support serialize to file、serialize to stream、deserialize from file、deserialize from stream.
4. Support Xml encryption.
5. Support serialize accelerate through the XML serialization assemble.

簡單的說它就是使用簡單(對筆者而言)、支援大部份的序列化格式、支援序列化到檔案或是串流、從檔案或串流解序列化回物件、支援XML序列化後加密、以及會自動偵測XML序列化組件來加速等功能。

架構上也十分簡單，沒有什麼特別的設計。除了可以直接建出需要的Serializer來用外，也可以直接透過Serializer這個輔助類別去動作。

![2012-06-03_130715_thumb.png](/images/posts/aad443fe-d83e-40ac-9f64-b001e1519e59/2012-06-03_130715_thumb.png)

使用方式就不多做說明，方案裡面的資料應該很齊全，除了類別圖外，也附有一些簡單的單元測試，看一下應該就OK了。簡單的帶一下，大概就是先取得對應的Serializer，這邊可以透過Serializer.GetSerializer取得。

```c
ISerializer serializer = Serializer.GetSerializer(SerializerType.Xml);
```

或是直接New出對應的Serializer。

```csharp
ISerializer serializer = New XmlSerializer();
```

然後透過對應的Serializer去做序列化或解序列化的動作。

```csharp
serializer.Serialize(obj, "Data.dat");
...
var deserializedObj = serializer.DeSerialize<OBJECT_TYPE>("Data.dat");
```

除此之外也可以直接透過Serializer輔助類別去做序列化或解序列化。

```csharp
Serializer.Serialize(obj, "Data.dat", SerializerType.Xml);
...
var deSerializedObj = Serializer.DeSerialize<OBJECT_TYPE>("Data.dat", SerializerType.Xml);
```

## Link

* LevelUp Serializer
