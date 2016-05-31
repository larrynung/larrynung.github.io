---
layout: post
title: "log4net - BufferingForwardingAppender"
date: 2016-03-02 05:24:00
comments: true
tags: [log4net]
keywords: "log4net"
description: "log4net - BufferingForwardingAppender"
---

為了調效 log4net RollingFileAppender 的性能做了個簡單的測試，測試程式如下：  

<!-- More --> 

{% codeblock lang:c# %}
using System;
using System.Diagnostics;
using log4net;
using log4net.Config;

namespace ConsoleApplication27
{
    class Program
    {
        static void Main(string[] args)
        {
            XmlConfigurator.Configure();

            var count = 100000;
            var logger = LogManager.GetLogger(System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);
            
            var sw = Stopwatch.StartNew();
            for (var idx = 0; idx < count; ++idx)
            {
                logger.Debug(idx.ToString());
            }

            Console.WriteLine(sw.ElapsedMilliseconds);
        }
    }
}
{% endcodeblock %}

<br/>


{% img /images/posts/log4netBufferingForwardingAppender/1.png %}

<br/>


套上 BufferingForwardingAppender。  

{% codeblock lang:xml %}
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <configSections>
    <section name="log4net" type="log4net.Config.Log4NetConfigurationSectionHandler,log4net" />
  </configSections>
  <log4net>
    <root>
      <level value="ALL"/>
      <appender-ref ref="BufferingForwardingAppender"/>
    </root>
    
    <appender name="BufferingForwardingAppender" type="log4net.Appender.BufferingForwardingAppender">
      <bufferSize value="512" />
      <appender-ref ref="RollingFileAppender" />
    </appender>
    
    <appender name="RollingFileAppender" type="log4net.Appender.RollingFileAppender">
      ...
    </appender>
  </log4net>
</configuration>
{% endcodeblock %}

</br>


整個性能反而嚴重下降。  

{% img /images/posts/log4netBufferingForwardingAppender/2.png %}

<br/>


這邊可進一步調整 Fix 參數，像是如果我們將之設為 0，效能就會提升上去。  

{% img /images/posts/log4netBufferingForwardingAppender/3.png %}

<br/>


但是如果設為 0，Log 的資料會不正確，像是圖中的 Thread ID 就無法正確紀錄。  

<br/>


實際使用時我們應該參閱 FixFlags Enumeration，依需求下去設定。  

{% img /images/posts/log4netBufferingForwardingAppender/4.png %}

<br/>


像是可以設定為 12，使其修正 Message 與 ThreadName。  

{% img /images/posts/log4netBufferingForwardingAppender/5.png %}

<br/>


效能問題解決了，仍需考慮 Buffer 的資料是否可以正確的寫入。  

<br/>


一樣做個簡單的實驗去測試，設定 Buffer 大小為 512 筆，然後程式這邊在第 511 筆時丟出例外，可以看到這邊 Buffer 的資料並未正確的紀錄。  

{% img /images/posts/log4netBufferingForwardingAppender/6.png %}

<br/>


所以我們需要在程式中適當的時機點，像是在 Application_End 或是在全域例外處理這邊，將 Buffer Flush 讓 Log 可被寫入。  

{% codeblock lang:c# %}
...
static void Main(string[] args)
{
    AppDomain.CurrentDomain.UnhandledException += CurrentDomain_UnhandledException;
            ...
}

private static void CurrentDomain_UnhandledException(object sender, UnhandledExceptionEventArgs e)
{
    FlushBuffers();
}

public static void FlushBuffers()
{
    var rep = LogManager.GetRepository();
    foreach (IAppender appender in rep.GetAppenders())
    {
        var buffered = appender as BufferingAppenderSkeleton;
        if (buffered != null)
        {
            buffered.Flush();
        }
    }
}
...
{% endcodeblock %}

<br/>


{% img /images/posts/log4netBufferingForwardingAppender/7.png %}

<br/>

Link
----
* [c# - log4net BufferingForwardingAppender performance issue - Stack Overflow](http://stackoverflow.com/questions/11319319/log4net-bufferingforwardingappender-performance-issue)
* [Fix Property](https://logging.apache.org/log4net/log4net-1.2.13/release/sdk/log4net.Appender.BufferingAppenderSkeleton.Fix.html)
* [Is there anyway to programmably flush the buffer in log4net - Stack Overflow](http://stackoverflow.com/questions/2045935/is-there-anyway-to-programmably-flush-the-buffer-in-log4net)
