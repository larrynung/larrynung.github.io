---
layout: post
title: "Opserver - Stack Exchange's Monitoring System"
date: 2016-04-11 23:24
comments: true
categories: [Opserver]
keywords: "Opserver"
description: "Opserver - Stack Exchange's Monitoring System"
---

Opserver 是 Stack Exchange 開發的監控系統，能夠針對以下系統進行監控：    

<!-- More -->

* Servers/Switches & anything supported by Bosun, Orion, or direct WMI monitoring
* SQL Clusters & Single Instances
* Redis
* Elasticsearch
* Exception Logs (from StackExchange.Exceptional)
* HAproxy
* PagerDuty
* CloudFlare DNS

<br/>


安裝上只需要從 Github 將 Opserver 抓下來，開啟 Opserver 專案，然後設定其對應的 Config，並將之部署到網站伺服器運行即可。  

<br/>


Opserver 的 Config 設定放置於 /Opserver/Config/ 下，參閱放置在裡面的 example 檔設定即可。需先針對 Opserver/Config/SecuritySettings.config 下去設定，設定網站的安全性，再來才是要監控的系統對應的設定。如果設定後本地運行無法看到效果，可將 IISExpress 停掉後重跑看看。   

{% img /images/posts/Opserver/1.png %}

<br/>


{% img /images/posts/Opserver/2.png %}

<br/>


{% img /images/posts/Opserver/3.png %}

<br/>


{% img /images/posts/Opserver/4.png %}

<br/>


{% img /images/posts/Opserver/5.png %}

<br/>


{% img /images/posts/Opserver/6.png %}

<br/>


{% img /images/posts/Opserver/7.png %}

<br/>


{% img /images/posts/Opserver/8.png %}

<br/>


{% img /images/posts/Opserver/9.png %}

<br/>


Link
----
* [opserver/Opserver: Stack Exchange's Monitoring System](https://github.com/opserver/Opserver)
