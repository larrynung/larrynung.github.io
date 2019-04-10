---
title: 'C# 8.0 - Static local functions'
date: 2019-04-10 15:07:34
tags: [CSharp 8.0]
---

C# 8.0 開始支援靜態的 Local functions，只要直接在 Local functions 前面加掛 static 關鍵字即可。  

<!-- More -->

```C#
using System;

namespace StaticLocalFunctions
{
    class Program
    {
        static void Main(string[] args)
        {
            static void SayHello(string name) =>  Console.WriteLine(string.Format("Hello~{0}", name));

            //static void SayHello(string name)
            //{
            //    Console.WriteLine(string.Format("Hello~{0}", name));
            //}

            SayHello("Larry");
        }
    }
}
```

{% asset_img 1.png %}

<br/>


Static Local functions 的資料要從參數傳入，如果直接 reference Local functions 外的變數編譯器會報錯。  

```C#
using System;

namespace StaticLocalFunctions
{
    class Program
    {
        static void Main(string[] args)
        {
            var name = "Larry";
            static void SayHello() =>  Console.WriteLine(string.Format("Hello~{0}", name));

            //static void SayHello()
            //{
            //    Console.WriteLine(string.Format("Hello~{0}", name));
            //}

            SayHello();
        }
    }
}
```

{% asset_img 2.png %}
