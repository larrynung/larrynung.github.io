---
layout: post
title: "Debugging Http or Web Services Calls from ASP.NET with Fiddler"
date: 2015-10-04 23:22:00
comments: true
tags: 
keywords: "Fiddler"
description: "Debugging Http or Web Services Calls from ASP.NET with Fiddler"
---

要用 Fiddler 去查看 ASP.NET Web Site ，我們可以透過設定 Web.Config 將 Web Site 的 Proxy 指向 http://127.0.0.1:8888:  

<!-- More -->


{% codeblock lang:xml %}
...
<system.net>
  <defaultProxy>
    <proxy  proxyaddress="http://127.0.0.1:8888" />
  </defaultProxy>
</system.net>
...
{% endcodeblock %}

<br/>


這樣 Fiddler 就可以記錄到 Web Site 的網路使用情形：  

{% img /images/posts/DebugWebSiteWithFiddler/1.png %}

<br/>


Link
----
* [Debugging Http or Web Services Calls from ASP.NET with Fiddler - Rick Strahl's Web Log](http://weblog.west-wind.com/posts/2008/Mar/14/Debugging-Http-or-Web-Services-Calls-from-ASPNET-with-Fiddler)
