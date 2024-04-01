---
title: "Jil - Serialize DateTime to ISO8601 Format"
date: "2015-09-30 23:54:00"
description: "Jil - Serialize DateTime to ISO8601 Format"
tags: [Jil]
---


Jil 在做時間的序列化，預設出來的資料會跟 JavaSriptSerializer 一樣，會序列化成下面這個樣子：  

<!-- More -->

    "/Date(1290181373164)/"

<br/>


若要改成 ISO8601 的格式，我們可以帶入 Options 進行指定：  

```c#
...
Console.WriteLine(JSON.Serialize(dt, new Options(dateFormat : DateTimeFormat.ISO8601)));
Console.WriteLine(JSON.Serialize(dt, Options.ISO8601));
...
```

<br/>


完整的範例如下：  

```c#
using Jil;
using System;

namespace ConsoleApplication5
{
    class Program
    {
        static void Main(string[] args)
        {
            var dt = DateTime.Now;

            Console.WriteLine(JSON.Serialize(dt));
            Console.WriteLine(JSON.Serialize(dt, new Options(dateFormat : DateTimeFormat.ISO8601)));
            Console.WriteLine(JSON.Serialize(dt, Options.ISO8601));
        }
    }
}
```

{% img /images/posts/JilIso8601/1.png %}
