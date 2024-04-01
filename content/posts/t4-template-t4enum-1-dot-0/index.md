---
title: "T4 Template - T4Enum 1.0"
date: "2016-03-22 21:38:00"
description: "T4 Template - T4Enum 1.0"
tags: [T4, T4Enum]
---


.NET 列舉的很多操作都會有難以避免的 Boxing/UnBoxing，像是要取得特定列舉值的列舉名，取得所有的列舉名，取得所有的列舉值，取得列舉值的 Attribute，都無法避免 Boxing/UnBoxing 的發生。   

<!-- More -->

<br/>


{% img /images/posts/T4Enum/1.png %}

<br/>


這邊筆者嘗試用 T4 來解這問題，用 T4 範本可以遍尋專案內的所有列舉，產生對應的輔助類別與擴充方法，藉此避開列舉操作的 Boxing/UnBoxing 問題。  

<br/>


程式可至 [NuGet Gallery | LevelUp.T4Enum 1.0.0](https://www.nuget.org/packages/LevelUp.T4Enum/1.0.0) 這邊抓取。  

<br/>


實際使用會像是下面這樣：    

```c#
using System;
using T4Enum;
using T4Enum.Extensions;

namespace ConsoleApplication7
{
    enum Permission
    {
        Function1,
        Function2,
        Function3
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Enums.Permission.Function1.Name);
            Console.WriteLine((int)Enums.Permission.Function1.Value);

            Console.WriteLine(Enums.Permission[Permission.Function2].Name);
            Console.WriteLine((int)Enums.Permission[Permission.Function2].Value);

            Console.WriteLine(Enums.Permission.GetName(Permission.Function3));
            Console.WriteLine(Permission.Function3.GetName());

            foreach (var item in Enums.Permission)
            {
                Console.WriteLine(item.Name);
                Console.WriteLine((int)item.Value);
            }

            foreach (var name in Enums.Permission.GetNames())
            {
                Console.WriteLine(name);
            }

            foreach (var value in Enums.Permission.GetValues())
            {
                Console.WriteLine((int)value);
            }
        }
    }

}
```

<br/>


運行結果如下：  

{% img /images/posts/T4Enum/2.png %}

<br/>


目前這版已經能取得列舉名，遍尋列舉名，與遍尋列舉值，但尚未支援 Attribute 的取得。  
