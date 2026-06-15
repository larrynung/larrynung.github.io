---
title: ".NET 4.0 New Feature - String.IsNullOrWhiteSpace"
date: "2010-11-22 12:49:32"
description: ".NET 4.0 New Feature - String.IsNullOrWhiteSpace"
tags: [CSharp]
---

.NET 4.0在String類別中新增了IsNullOrWhiteSpace方法，該方法可幫助我們判別指定的字串是否為null、空白、或由空白字元所組成的字串。

MSDN中有提到IsNullOrWhiteSpace方法其實就等同於下面這樣的寫法：

```csharp
return String.IsNullOrEmpty(value) || value.Trim().Length == 0;
```

簡單的說它跟IsNullOrEmpty方法的差異只在於是否為空的字元所組成，在很多的情況下，我們會把空白字元組成的字串視為是空值，故多了IsNullOrEmpty方法可讓我們省去需先撰寫Trim掉前後空白字元的動作，另外一提據MSDN的說法，使用IsNullOrEmpty方法替換這樣的作法也能得到稍許的效能改善。

不過這邊因為MSDN的value.Trim().Length == 0動作有包含String.IsNullOrEmpty(value)部份的動作，個人是覺得IsNullOrEmpty方法應該是比較像是下面這樣：

```csharp
return value == null || value.Trim().Length == 0;
```

最後來看個比較完整的範例：

```csharp
using System;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] values = { null,
                                String.Empty,
                                "ABCDE",
                                new String(' ', 20),
                                "\t\r\n\v\f",
                                new String('\u2000', 10),
                              };

            Console.WriteLine(new String('=', 50));
            Console.WriteLine("IsNullOrWhiteSpaceDemo...");
            IsNullOrWhiteSpaceDemo(values);

            Console.WriteLine(new String('=', 50));
            Console.WriteLine("MSDNCustomIsNullOrWhiteSpaceDemo...");
            MSDNCustomIsNullOrWhiteSpaceDemo(values);

            Console.WriteLine(new String('=', 50));
            Console.WriteLine("CustomIsNullOrWhiteSpaceDemo...");
            CustomIsNullOrWhiteSpaceDemo(values);
        }
        public static void IsNullOrWhiteSpaceDemo(string[] values)
        {
            foreach (string value in values)
                Console.WriteLine("String.IsNullOrWhiteSpace({0}): {1}", value, String.IsNullOrWhiteSpace(value));
        }

        public static void MSDNCustomIsNullOrWhiteSpaceDemo(string[] values)
        {
            foreach (string value in values)
                Console.WriteLine("MSDNCustomIsNullOrWhiteSpace({0}): {1}", value, MSDNCustomIsNullOrWhiteSpace(value));
        }

        public static bool MSDNCustomIsNullOrWhiteSpace(string value)
        {
            return String.IsNullOrEmpty(value) || value.Trim().Length == 0;
        }

        public static void CustomIsNullOrWhiteSpaceDemo(string[] values)
        {
            foreach (string value in values)
                Console.WriteLine("CustomIsNullOrWhiteSpace({0}): {1}", value, CustomIsNullOrWhiteSpace(value));
        }

        public static bool CustomIsNullOrWhiteSpace(string value)
        {
            return value == null || value.Trim().Length == 0;
        }
    }
}
```

運行結果如下：

![image_thumb.png](/images/posts/19610/image_thumb.png)

## Link

* String.IsNullOrWhiteSpace 方法
