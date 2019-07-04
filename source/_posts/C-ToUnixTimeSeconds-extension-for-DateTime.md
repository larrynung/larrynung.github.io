---
title: 'C# - ToUnixTimeSeconds extension for DateTime'
date: 2019-07-04 15:35:45
tags:
---

DateTimeOffset 在 C# 4.6 新增了 ToUnixTimeSeconds 方法，可以取得跟 UnixTime 之間差的秒數。  

<!-- More -->

<br/>


有些時候我們會需要跟 UnixTime 之間差的秒數，但是不需要 TimeZone 資訊，這時我們其實不需要從 DateTime 換成 DateTimeOffset，只要自行跟 UnixTime 相減再取 TotalSeconds 即可。  

<br/>


為了便於使用，這邊將它包成擴充方法。  

```C#
using System;

namespace TimestampTest
{
    public static class DateTimeExtension
    {
        private static readonly DateTime _unixTime = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);

        public static int ToUnixTimeSeconds(this DateTime dateTime)
        {
            return (int) dateTime.Subtract(_unixTime).TotalSeconds;
        }
    }
}
```

<br/>


使用上會像下面這樣：  

```C#
var unitTimeSeconds = DateTime.UtcNow.ToUnixTimeSeconds();
```

<br/>


這邊筆者撰寫了個簡單的程式做個測試。  

```C#
using System;
using System.Diagnostics;

namespace TimestampTest
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(DateTime.UtcNow.ToUnixTimeSeconds());
            Console.WriteLine(DateTimeOffset.UtcNow.ToUnixTimeSeconds());

            var count = 10000000;
            Console.WriteLine(DoTest(count, ()=> { DateTime.UtcNow.ToUnixTimeSeconds(); }));
            Console.WriteLine(DoTest(count, ()=> { DateTimeOffset.UtcNow.ToUnixTimeSeconds(); }));
        }

        private static long DoTest(int count, Action action)
        {
            var sw = Stopwatch.StartNew();
            for (var i = 0; i < count; ++i)
            {
                action();
            }

            return sw.ElapsedMilliseconds;
        }
    }
}

```

</br>


透過運行的結果可以看到值跟 DateTimeOffset 內建的 ToUnixTimeSeconds 是一致的，但速度上會比 DateTimeOffset 內建的 ToUnixTimeSeconds 還要快一點點，這部分應該是因為 DateTimeOffset 要多處理 TimeZone 的原因。  

{% asset_img 1.png %}

</br>


最後附上測出來的速度比較數據。  

| Times      | DateTime | DateTimeOffset |
|:----------:|:--------:|:--------------:|
| 100000     | 6        | 7              |
| 1000000    | 61       | 73             |
| 10000000   | 597      | 713            |
| 100000000  | 5919     | 7067           |
| 1000000000 | 59118    | 70631          |

{% asset_img 2.png %}
