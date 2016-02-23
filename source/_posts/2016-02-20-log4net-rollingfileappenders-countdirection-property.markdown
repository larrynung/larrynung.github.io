---
layout: post
title: "log4net - RollingFileAppender's CountDirection Property"
date: 2016-02-20 19:00
comments: true
categories: [log4net]
keywords: "log4net"
description: "log4net - RollingFileAppender's CountDirection Property"
---

log4net 在使用 RollingFileAppender 去做 Log 的紀錄時，我們需要注意 CountDirection 的設定。設定值大於 0，表示以遞增的方式 Rolling。反之，表示已遞減的方式 Rolling。  

<!-- More -->

{% img /images/posts/Log4NetCountDirection/1.png %}

<br/>


該設定預設值為 -1，所以當新的檔案要產生時，他需要先用 Rename 將檔案往後擠才行，可以想見這樣會有不必要的效能耗費。透過 Process Monitor 可以很清楚的看到背後的運作。      


{% img /images/posts/Log4NetCountDirection/2.png %}

<br/>


所以可以的話，我們可以將設定值改為 1，用以取得較好的效能。  

<br/>


這邊筆者簡單的做個試驗，寫了一個簡單的程式讓它持續的寫 log，而 log4net 設定每 1 KB 產生一個檔案，用以監測效能上的影響。  

{% codeblock lang:c# %}
using log4net;
using log4net.Config;
using System;
using System.Diagnostics;

namespace ConsoleApplication6
{
    class Program
    {
        static void Main(string[] args)
        {
            XmlConfigurator.Configure();

            var count = 500;
            var logger = LogManager.GetLogger(System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);

            Console.WriteLine("{0} ms", DoTest(count, () =>
            {
                logger.Debug("test");
            }));   
        }

        static long DoTest(int count, Action action)
        {
            var sw = Stopwatch.StartNew();
            for (int i = 0; i < count; ++i)
            {
                action();
            }

            return sw.ElapsedMilliseconds;
        }
    }
}
{% endcodeblock %}

<br/>


可以看到若不設定 CountDirection，連續產生 39 個檔案時它的耗時為 586 ms。  

{% img /images/posts/Log4NetCountDirection/3.png %}

<br/>


若設定 CountDirection 為 1，則耗時為 332 ms。  

{% img /images/posts/Log4NetCountDirection/4.png %}

<br/>


當連續產生 77 個檔案時，不設定 CountDirection 耗時為 3061 ms。  

{% img /images/posts/Log4NetCountDirection/5.png %}

<br/>


設定為 1，則耗時為 518 ms。  

{% img /images/posts/Log4NetCountDirection/6.png %}

<br/>


可以看到這小小的效能差異累積起來其實也是很可觀的。  

<br/>

Link
----
* [CountDirection Property](https://logging.apache.org/log4net/log4net-1.2.11/release/sdk/log4net.Appender.RollingFileAppender.CountDirection.html)
