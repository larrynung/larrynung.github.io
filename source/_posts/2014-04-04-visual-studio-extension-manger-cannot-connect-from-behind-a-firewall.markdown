---
layout: post
title: "Visual Studio - Extension Manger Cannot Connect From Behind a Firewall"
date: 2014-04-04 01:02
comments: true
categories: [Visual Studio]
keywords: "Visual Studio, Extension Manager"
description: "Visual Studio - Extension Manger Cannot Connect From Behind a Firewall"
---

筆者工作環境的電腦，Visual Studio 內的 Extension Manager 無法正常的運作，查了一下才知道這是因為防火牆擋住了 100-Continue 的訊息發送所導致。 

<!-- More -->

{% img /images/posts/VSExpect100Continue/1.png %}

<br/>

因此要將 `Common7\IDE` 下的 `devenv.exe.config` 開啟調整，將 100-Continue 這個 Feature 關閉才可正常運作。 

{% img /images/posts/VSExpect100Continue/2.png %}

<br/>

檔案開啟後，在 system.net 的節點內加入 `<servicePointManager expect100Continue="false"/>`，將 100-Continue 這個 Feature 給關閉就可以了。  

{% img /images/posts/VSExpect100Continue/3.png %}

<br/>

Link
----
* [visual studio 2010 - Cannot connect to any online resource - Stack Overflow](http://stackoverflow.com/questions/2859148/cannot-connect-to-any-online-resource)
* [ServicePointManager.Expect100Continue 屬性 (System.Net)](http://msdn.microsoft.com/zh-tw/library/system.net.servicepointmanager.expect100continue(v=vs.110).aspx)
* [Visual Studio Extension Manger Cannot Connect From Behind a Firewall](https://julianscorner.com/wiki/programming/vs2011_proxy_issue)
* [Expect:100-continue | 風雪之隅](http://www.laruence.com/2011/01/20/1840.html)
