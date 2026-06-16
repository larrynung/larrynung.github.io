---
title: ".NET 4.0 New Feature - String.Join"
date: "2010-11-22 08:08:33"
description: ".NET Framework 4.0新增了三個String.Join的多載函式Join(String, IEnumerable )、Join (String, IEnumerable )、與[Join(String,…"
tags: [CSharp]
---

.NET Framework 4.0新增了三個String.Join的多載函式Join(String, IEnumerable<String>)、[Join<T>(String, IEnumerable<T>)](http://msdn.microsoft.com/zh-tw/library/dd992421.aspx)、與[Join(String, Object[])](http://msdn.microsoft.com/zh-tw/library/dd988350.aspx)。

![image_thumb.png](/images/posts/19630/image_thumb.png)

這三個多載函式可以看出，我們可傳入Object[]、IEnumerable<T>這三種新的型態，不需再將List<String>、StringCollection等型態的資料塞成String[]就可以使用，也能在陣列中放入不同的型態，不需先將集合元素轉成字串，這部份在4.0(含)以後.NET Framework會幫我們做掉了。

完整的使用範例如下：

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
            Console.WriteLine("{0}: {1}", title, string.Join(",", values));
        }
    }
}
```

運行結果如下：

![image_thumb_1.png](/images/posts/19630/image_thumb_1.png)

也可以整理成IEnumerable<T>的擴充方法使用。

```csharp
public static class IEnumerableExtension
{
    public static string Join<T>(this IEnumerable<T> obj, string seperator)
    {
        return string.Join(seperator, obj);
    }
}
```

這邊將上面的範例改為擴充方法的版本：

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

            Console.WriteLine("{0}: {1}", "stringCollection", stringCollection.Join(","));
            Console.WriteLine("{0}: {1}", "intCollection", intCollection.Join(","));
            Console.WriteLine("{0}: {1}", "objCollection", objCollection.Join(","));
            Console.WriteLine("{0}: {1}", "floatCollection", floatCollection.Join(","));
        }
    }

    public static class IEnumerableExtension
    {
        public static string Join<T>(this IEnumerable<T> obj, string seperator)
        {
            return string.Join(seperator, obj);
        }
    }
}
```

## Link

* String.Join 方法
