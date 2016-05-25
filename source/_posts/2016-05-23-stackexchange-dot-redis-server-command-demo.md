---
layout: post
title: "StackExchange.Redis - Server Command Demo"
date: 2016-05-23 23:28:00
comments: true
categories: [StackExchange.Redis]
keywords: "StackExchange.Redis"
description: "StackExchange.Redis - Server Command Demo"
---

要使用 StackeExchange.Redis 取得 Server 的資訊，或是運行 Server 的命令。要先調用 GetServer 方法取得 Server 物件，再透過該 Server 成員屬性或方法去操作即可。  

<!-- More -->

<br/>


像是下面這邊筆者遍巡了每台 Server，並將其相關的資訊顯示到主控台：    

{% codeblock lang:c# %}
using System; 
using StackExchange.Redis; 

namespace ConsoleApplication4 { 
    class Program { 
        static void Main(string[] args) { 
            var configuration = "localhost:6379"; 
            using (var conn = ConnectionMultiplexer.Connect(configuration)) { 
                var endPoints = conn.GetEndPoints(); 
                foreach (var endPoint in endPoints) { 
                    var server = conn.GetServer(endPoint); 
                   Console.WriteLine("Server: {0}", server.Multiplexer); 
                   Console.WriteLine("IsSlave: {0}", server.IsSlave); 
                   Console.WriteLine("AllowSlaveWrites: {0}", server.AllowSlaveWrites); 
                   Console.WriteLine("ServerType: {0}", server.ServerType); 
                   Console.WriteLine("Version: {0}", server.Version); 
                   Console.WriteLine("ServerTime: {0}", server.Time()); 
                   Console.WriteLine("Latency: {0}", server.Ping()); 
                   Console.WriteLine("OperationCount: {0}", server.Multiplexer.OperationCount); 
                   Console.WriteLine("Keys: {0}", string.Join(",", server.Keys().ToArray())); 
                   Console.WriteLine(new string('=', 78)); 
               }
            }
        } 
    } 
}
{% endcodeblock %}

<br/>


運行結果如下：  

{% img /images/posts/ServerCommandInStackExchange.Redis/1.png %}
