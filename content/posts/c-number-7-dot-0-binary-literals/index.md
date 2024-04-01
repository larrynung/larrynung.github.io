---
title: "C# 7.0 - Binary literals"
date: "2016-05-16 05:27:00"
description: "C# 7.0 - Binary literals"
tags: [CSharp, CSharp 7.0]
---


在程式開發時，有時我們會需要使用二進制的數值，像是在使用標有 FlagsAttribute 的列舉值做權限時就會用到。在 C 7.0# 前我們必需要使用十進制數值表示法，確保他是二進制的數值。  

<!-- More -->

<br/>


在  C# 7.0 後開始支援二進制數值表示法，使用上只需用 0b 當做前綴即可，像是  0 可以寫成 0b00、1 可以寫成 0b01、2 可以寫成 0b10、4 可以寫成 0b100，以此類推。  

```c#
using System;

namespace ConsoleApplication1

    class Program
    {
        static void Main(string[] args)
        {
            var values = new int[] { 0b00, 0b01, 0b10, 0b100, 0b1000 };

            foreach (var value in values)
            {
                Console.WriteLine(value.ToString());
            }
        }
    }
}
```

<br/>


{% img /images/posts/CSharp7Binaryliterals/1.png %}

<br/>

Link
----
* [A glance at C# vNext - CodeProject](http://www.codeproject.com/Articles/699708/A-glance-at-Csharp-vNext#binary-literals-and-separators)
