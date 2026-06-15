---
title: ".NET 4.0 New Feature - Environment.Is64BitProcess & Environment.Is64BitOperatingSystem"
date: "2010-12-12 11:33:51"
description: ".NET 4.0 New Feature - Environment.Is64BitProcess & Environment.Is64BitOperatingSystem"
tags: [CSharp]
---

.NET 4.0在Environment類別新增Is64BitOperatingSystem與Is64BitProcess屬性，其功用分別為判斷當前作業系統是否為64位元版本，與判斷當前處理序是否為64位元。

Property

<table border="1" cellpadding="2" cellspacing="0" width="466"><tbody> <tr> <td valign="top" width="176">Name</td> <td valign="top" width="288">Description</td> </tr> <tr> <td valign="top" width="180">Is64BitOperatingSystem</td> <td valign="top" width="288">是否為64位元作業系統</td> </tr> <tr> <td valign="top" width="184">Is64BitProcess</td> <td valign="top" width="288">是否為64位元處理序</td> </tr> </tbody></table>

使用範例：

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication4
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("64位元作業系統: {0}",Environment.Is64BitOperatingSystem);
            Console.WriteLine("64位元處理序: {0}", Environment.Is64BitProcess);
        }
    }
}
```

運行結果：

![image_thumb.png](/images/posts/20075/image_thumb.png)
