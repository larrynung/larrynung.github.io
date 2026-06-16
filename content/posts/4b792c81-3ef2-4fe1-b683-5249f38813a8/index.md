---
title: "[C#]BigInteger"
slug: "[CSharp]BigInteger"
date: "2013-11-06 12:00:00"
tags: [CSharp]
description: "今天看書才知道原本.NET 3.5中偷藏了一個BinInteger類型，可用來顯示很長的整數。該類型在.NET Framework 3.5 Beta1中就已被加入,但是Release版中該類型被改為Internal類型，導致無法直接使用。"
---

今天看書才知道原本.NET 3.5中偷藏了一個BinInteger類型，可用來顯示很長的整數。該類型在.NET Framework 3.5 Beta1中就已被加入,但是Release版中該類型被改為Internal類型，導致無法直接使用。根據網路上的資料顯示，據說是微軟認為該類型還有很多問題，因此暫不開放。但我們仍可透過.NET反射機制去使用它。

簡易範例如下：

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Reflection;

namespace ConsoleApplication5
{
class Program
{
static void Main(string[] args)
{
Type type = Assembly.LoadWithPartialName("System.Core").GetType("System.Numeric.BigInteger");
Object o1 = Activator.CreateInstance(type, double.MaxValue);
Object o2 = Activator.CreateInstance(type, double.MaxValue);
MethodInfo m = type.GetMethod("Add", BindingFlags.Public | BindingFlags.Static);
Console.WriteLine(m.Invoke (null,new object []{o1,o2}));
}
}
}
```

執行結果如下：

![image_thumb.png](/images/posts/4b792c81-3ef2-4fe1-b683-5249f38813a8/image_thumb.png)

## Conclusion

上網搜了一下，好像直接這樣使用的人並不多。多半是使用自己寫的類別來達到此需求。像是Code Project上這篇。

## 相關連結

* Code Project-C# BigInteger Class
