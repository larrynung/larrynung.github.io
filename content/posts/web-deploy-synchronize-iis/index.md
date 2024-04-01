---
title: "Web Deploy - Synchronize IIS"
date: "2015-07-10 22:18:00"
description: "Web Deploy - Synchronize IIS"
tags: [Web Deploy]
---


若要做 IIS 之間的同步，我們可以使用 Web Deploy。  

<!-- More -->

<br/>

它可以做到 Local To Remote。

    msdeploy -verb:sync -source:webServer -dest:webServer,computerName=Server2


Remote To Local。  

    msdeploy -verb:sync -source:webServer,computerName=Server2 -dest:webServer


以及 Remote To Remote。  

    msdeploy -verb:sync -source:webServer,computerName=Server2 -dest:webServer,computerName=Server3

<br/>

簡單來說就只是用 msdeploy 帶入 sync verb，並指定 source 與 dest。source 與 dest若是針對整個 Server 同步則帶入 webServer，若是遠端電腦則要多帶入 computerName。  
<br/>

像是如果我要將本地的 IIS 整個同步到 192.168.0.2 的 IIS，就要像下面這樣：

    msdeploy -verb:sync -source:webServer -dest:webServer,computerName=192.168.0.2 

命令執行後 Web Deploy 即會將 WebSite、Application Pool、Binding、File、以及 Setting 等在指定的電腦間進行同步，十分的方便.  

<br/>

Link
----
* [Synchronize IIS : The Official Microsoft IIS Site](http://www.iis.net/learn/publish/using-web-deploy/synchronize-iis)
* [Web Deploy sync Operation](https://technet.microsoft.com/zh-tw/library/dd569005(v=ws.10).aspx)
