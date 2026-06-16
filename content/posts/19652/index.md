---
title: ".NET 4.0 New Feature - String.Concat"
date: "2010-11-23 12:26:01"
description: ".NET Framework 4.0新增了兩個String.Concat的多載函式Concat (IEnumerable )、與Concat(IEnumerable )。"
tags: [CSharp]
---

.NET Framework 4.0新增了兩個String.Concat的多載函式Concat<T>(IEnumerable<T>)、與[Concat(IEnumerable<String>)。](http://msdn.microsoft.com/zh-tw/library/dd784338.aspx)

![image_thumb.png](/images/posts/19652/image_thumb.png)

這兩個新的多載函式跟String.Join的新多載函式類似，能幫我們串連IEnumerable集合中的元素，不必預先將元素轉換為字串後再處理，同時也支援更多的集合類型。

完整範例如下：

```csharp
using System;
using System.Collections.Generic;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            String[] stringCollection = { "123", "456", "789" };
            int[] intCollection = { 123, 456, 789 };
            Object[] objCollection = { 123, "456", 789.0f };
            float[] floatCollection = { 123.0f, 456.0f, 789.0f };

            ShowValue<String>("stringCollection", stringCollection);
            ShowValue<int>("intCollection", intCollection);
            ShowValue<Object>("objCollection", objCollection);
            ShowValue<float>("floatCollection", floatCollection);
        }

        static void ShowValue<T>(string title, IEnumerable<T> values)
        {
            Console.WriteLine("{0}: {1}", title, string.Concat<T>(values));
        }
    }
}
```

運行結果如下：

![image_thumb_1.png](/images/posts/19652/image_thumb_1.png)

## Link

* String.Concat 方法
