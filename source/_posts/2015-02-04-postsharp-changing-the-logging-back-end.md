---
layout: post
title: "PostSharp - Changing the Logging Back-End"
date: 2015-02-04 00:31:00
comments: true
categories: [PostSharp]
keywords: "PostSharp"
description: "PostSharp - Changing the Logging Back-End"
---

前面介紹 PostSharp 時，筆者多半都是透過精靈介面將之套用至專案之中，在加 Log 時有一步驟是設定 Log 機制背後要用的服務，這個在精靈介面設定完後，若有修改的必要，我們可以參閱下表：  

<!-- More -->

{% img /images/posts/PostSharpChangLoggingBackEnd/1.png %}

<br/>


將本來使用到的 Log Profile 其對應的 NuGet Package 移除，然後將欲使用 Log Profile 對應的 NuGet Package 加入專案中，接著開啟副檔名為 psproj 的設定檔，將其 LoggingBackend 的值設為對應的 Log Profile Name。  

{% img /images/posts/PostSharpChangLoggingBackEnd/2.png %}

<br/>


Link
----
* [Walkthrough: Changing the Logging Back-End](http://doc.postsharp.net/logging-changing-backend)
