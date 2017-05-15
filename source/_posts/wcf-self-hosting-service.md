---
layout: post
title: "WCF - Self hosting service"
date: 2014-04-03 23:43:00
comments: true
tags: [WCF, CSharp]
keywords: "WCF, Hosting"
description: "WCF - Self hosting service"
---

要 Self hosting WCF 的服務。首先要先將 System.ServiceModel 加入參考。  

<!-- More -->

{% img /images/posts/WCFSelfHosting/1.png %}

<br/>

接著在程式設計中建立 ServiceHost。建立的同時要指定欲運行的 Service 型態，以及要 Host 的位置。 

```c#
    var serviceUrl = "http://localhost:6525/ExecuteService";
    var serviceUri = new Uri( serviceUrl );
    using (var host = new ServiceHost (typeof(WcfServiceLibrary1. ExecuteService), serviceUri))
    {
        ...
    }
```

<br/>

再來要建立 ServiceMetadataBehavior 並對其做些對應的設定，像是啟用 HttpGet。 

```c#
    ...
    var smb = new ServiceMetadataBehavior ();
    smb.HttpGetEnabled = true;
    smb.MetadataExporter.PolicyVersion = PolicyVersion.Policy15;
    ...
```

<br/>

將剛建立的 ServiceMetadataBehavior 加到 ServiceHost.Description.Behaviors。

```c#
    ...
    host.Description.Behaviors.Add(smb);
    ...
```

<br/>

在開始需要服務時，叫用 ServiceHost 的 Open 方法啟用 WCF 服務。  

```c#
    ...
    host.Open();
    ...
```

<br/>

接著使用 WCF Service 所提供的服務。 

當不再需要使用 WCF Service 服務時，叫用 ServiceHost 的 Close 方法關閉 WCF 服務。  

```c#
    ...
    host.Close();
    ...
```

<br/>

整個程式寫起來會像下面這樣： 

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceModel;
using System.ServiceModel.Description;
using System.Text;
using System.Threading.Tasks;
using ConsoleApplication16.ServiceReference1;


namespace ConsoleApplication16
{
    class Program
    {
        static void Main(string[] args)
        {
            Uri baseAddress = new Uri( "http://localhost:6525/ExecuteService" );


            using (ServiceHost host = new ServiceHost (typeof(WcfServiceLibrary1. ExecuteService), baseAddress))
            {
                ServiceMetadataBehavior smb = new ServiceMetadataBehavior ();
                smb.HttpGetEnabled = true;
                smb.MetadataExporter.PolicyVersion = PolicyVersion.Policy15;
                host.Description.Behaviors.Add(smb);


                host.Open();


                var client = new ExecuteServiceClient();


                var result = client.Execute("test");


                Console.WriteLine(result);


                host.Close();
            }
        }
    }
}
```

<br/>

像這樣的程式運行起來會連帶將 WCF Service 給帶起。

{% img /images/posts/WCFSelfHosting/2.png %}

<br/>

此時開啟瀏覽器做個簡單的測試，若是服務正常運作，應可看到該服務頁面。

{% img /images/posts/WCFSelfHosting/3.png %}
