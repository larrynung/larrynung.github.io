---
title: "[C#]HashSet 集合型別"
slug: "csharp-hashset-集合型別"
aliases: ["/posts/csharphashset-集合型別/"]
date: "2009-05-02 04:39:12"
description: "Namespace System.Collections.Generic Assemble System.Core (在 System.Core.dll 中) 需求 .NET Framework 3.5(含)以上 功能 以數學集合 (Set) 模型為基礎，並提供高效能的集合 (Set) 運算，"
tags: [CSharp]
---

## ![image_thumb_1.png](/images/posts/8271/image_thumb_1.png)

## Namespace

System.Collections.Generic

## Assemble

System.Core (在 System.Core.dll 中)

## 需求

.NET Framework 3.5(含)以上

## 功能

* 以數學集合 (Set) 模型為基礎，並**提供高效能的集合 (Set) 運算**，類似存取 Dictionary<(Of <(TKey, TValue>)>) 或 [Hashtable](http://msdn.microsoft.com/zh-tw/library/system.collections.hashtable.aspx) 集合 (Collection) 的索引鍵。簡而言之，您可以將 [HashSet<(Of <(T>)>)](http://msdn.microsoft.com/zh-tw/library/bb359438.aspx) 類別視為沒有值的 [Dictionary<(Of <(TKey, TValue>)>) 集合 (Collection)。](http://msdn.microsoft.com/zh-tw/library/xfhwa508.aspx)
* **不會排序，也無法包含重複的項目**。如果對應用程式來說，排序和項目重複比效能更重要，請使用 List<(Of <(T>)>) 類別配合 [Sort 方法。](http://msdn.microsoft.com/zh-tw/library/3da4abas.aspx)
* **提供許多數學集合 (Set) 運算**，例如集合 (Set) 相加 (結合) 以及集合 (Set) 相減。

## 簡易範例

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication5
{
class Program
{
static void Main(string[] args)
{
HashSet<Encoding> encodingHashset = new HashSet<Encoding>();
encodingHashset.Add(Encoding.ASCII);
encodingHashset.Add(Encoding.Unicode);
encodingHashset.Add(Encoding.UTF32);
encodingHashset.Add(Encoding.ASCII);
foreach (Encoding e in encodingHashset)
{
Console.WriteLine(e.WebName);
}
}
}
}
```

執行結果如下：

![image_thumb.png](/images/posts/8271/image_thumb.png)

由此範例可看到Hashset會自動忽略重覆的資料。

## Reference

* .NET Framework 開發人員手冊-HashSet 集合型別
* .NET Framework 類別庫-HashSet(T) 類別

![image_thumb_2.png](/images/posts/8271/image_thumb_2.png)
