---
layout: post
title: "StackExchange.Redis - Pub/Sub Demo"
date: 2016-05-24 07:51:00
comments: true
categories: [StackExchange.Redis]
keywords: "StackExchange.Redis"
description: "StackExchange.Redis - Pub/Sub Demo"
---

使用 StackExchange.Redis 開發 Redis 的 Pub/Sub 程式，需先調用 GetSubscriber 方法取得 Subscriber 物件，再透過該 Subscriber 物件去設定事件訂閱以及發佈訂閱即可。  

<!-- More -->

<br/>


像是下面這邊筆者訂閱了 MemberOnLine 的事件，當事件發生時會將上線資訊顯示在主控台，然後發佈 LarryNung 上線的事件給訂閱者：  

{% codeblock lang:c# %}
using System; 
using StackExchange.Redis; 

namespace ConsoleApplication4 { 
    class Program { 
        static void Main(string[] args) { 
            var configuration = "localhost:6379"; 
            using (var conn = ConnectionMultiplexer.Connect(configuration)) { 
                var sub = conn.GetSubscriber(); 
                var key = "MemberOnLine"; 
                sub.Subscribe(key, (c, v) => { 
                    Console.WriteLine("{0} Online...", v);
                 }); 
                sub.PublishAsync(key, "LarryNung", CommandFlags.FireAndForget);
            }
        } 
    } 
}
{% endcodeblock %}

<br/>


運行結果如下：

{% img /images/posts/PubSubInStackExchange.Redis/1.png %}
