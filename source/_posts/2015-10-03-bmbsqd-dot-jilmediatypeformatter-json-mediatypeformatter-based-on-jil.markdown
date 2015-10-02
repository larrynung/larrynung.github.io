---
layout: post
title: "Bmbsqd.JilMediaTypeFormatter - Json MediaTypeFormatter based on JIL"
date: 2015-10-03 00:40
comments: true
categories: [Jil]
keywords: "Jil"
description: "Bmbsqd.JilMediaTypeFormatter - Json MediaTypeFormatter based on JIL"
---

如果要將 Web API 的 JSON 處理改用 Jil 替換，我們可以使用 Bmbsqd.JilMediaTypeFormatter 這個 NuGet 套件。  

<!-- More -->

<br/>


{% img /images/posts/BmbsqdJilMediaTypeFormatter/1.png %}

<br/>


{% img /images/posts/BmbsqdJilMediaTypeFormatter/2.png %}

<br/>


套件安裝完後，開啟 WebApiConfig 將 JsonFormatter 換成 JilMediaTypeFormatter。  

{% codeblock lang:c# %}
using Bmbsqd.JilMediaFormatter;
...
config.Formatters.Remove(config.Formatters.JsonFormatter);
config.Formatters.Add(new JilMediaTypeFormatter());
...
{% endcodeblock %}

<br/>


像是下面這樣：  

{% img /images/posts/BmbsqdJilMediaTypeFormatter/3.png %}

<br/>


這樣 Web API 的 JSON 處理就會換成用 Jil 去做了。  

<br/>


Link
----
* [NuGet Gallery | JIL MediaTypeFormatter 0.1.1](https://www.nuget.org/packages/Bmbsqd.JilMediaTypeFormatter/)
