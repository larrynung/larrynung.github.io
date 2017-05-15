---
layout: post
title: "ASP.NET - Logging application shutdown events"
date: 2015-07-11 21:54:00
comments: true
tags: [ASP.NET]
keywords: "ASP.NET"
description: "ASP.NET - Logging application shutdown events"
---

做網站服務最害怕的就是服務不能正常運作，有時要追出實際發生的問題需要花費我們很多的時間。這時如果系統能將停止服務的原因正確的記錄下來，可有助於我們將問題快速的釐清。  

<!-- More -->

<br/>


可惜的是服務停止的原因預設是無法取得的，因為並沒有直接開放給開發人員調用。不過好在這樣的資訊還是有的，只是未被開出而已，所以我們仍舊可以透過反射下去取得。  

<br/>

要擷取這樣的資訊我們要從 HttpRuntime 類別下手，類別內有個 _theRuntime 靜態私有欄位用以存放唯一的物件實體，實體內的 _shutDownMessage 與 _shutDownStack 私有欄位分別存放著 Shutdown 的訊息與呼叫堆疊。  

<br/>


程式寫起來就像下面這樣：  

```c#
...
        private void LogShutDownInfo()
        {
            if (! m_Logger.IsInfoEnabled )
                return;

            var type = typeof (HttpRuntime );
            var runtime = ( HttpRuntime) type .InvokeMember( "_theRuntime" ,
                BindingFlags.NonPublic | BindingFlags.Static | BindingFlags .GetField,
                null, null , null);

            if (runtime == null)
                return;

            var message = ( string) type .InvokeMember( "_shutDownMessage" ,
                BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags .GetField,
                null,
                runtime,
                null);

            var stack = ( string) type .InvokeMember( "_shutDownStack" ,
                BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags .GetField,
                null,
                runtime,
                null);

            m_Logger.Info (string. Format(" {0}{1}{2}", message, Environment .NewLine, stack));
        }
...
```

<br/>


使用時只要在 Application_End 中呼叫即可：  

```c#
        /// <summary>
        /// Application_s the end.
        /// </summary>
        protected void Application_End()
        {
            m_Logger.Info ("Application End...");

            LogShutDownInfo();
        }
...
```

<br/>


這樣當系統就會自動在 Shutdown 時將 Shutdown 訊息記錄下來。  

{% img /images/posts/LogShutDownInfo/1.png %}

<br/>

Link
----
* [ScottGu's Blog - Logging ASP.NET Application Shutdown Events](http://weblogs.asp.net/scottgu/433194)
* [ASP.NET Case Study: Lost session variables and appdomain recycles - If broken it is, fix it you should - Site Home - MSDN Blogs](http://blogs.msdn.com/b/tess/archive/2006/08/02/asp-net-case-study-lost-session-variables-and-appdomain-recycles.aspx)
