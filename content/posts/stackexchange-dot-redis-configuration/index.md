---
title: "StackExchange.Redis - Configuration"
date: "2016-05-23 07:41:00"
description: "StackExchange.Redis - Configuration"
tags: [StackExchange.Redis]
---


欲連線至 Redis，需先設定 Configutaion，在 StackExchange.Redis 提供兩種設定方式，一種是用 ConfigurationOptions 物件直接宣告設定：  

<!-- More -->


```c#
using StackExchange.Redis; 
... 
var configuration = new ConfigurationOptions() 
{ 
    EndPoints = { 
        {"localhost", 6379}, 
        {"localhost", 6380} 
    }, 
    Password = "LarryNung" 
}; 
using (var conn = ConnectionMultiplexer.Connect(configuration)) 
{ 
    ... 
}
 ...
```

<br/>


一種是透過字串的方式設定：  

```c#
using StackExchange.Redis; 
... 
var configuration = "localhost:6379,localhost:6380,password=LarryNung"; 
using (var conn = ConnectionMultiplexer.Connect(configuration)) 
{ 
    ... 
} 
...
```

<br/>


如果不清楚有哪些可供設定，可參閱下表：  

{% img /images/posts/ConfigurationInStackExchange.Redis/1.png %}   

{% img /images/posts/ConfigurationInStackExchange.Redis/2.png %}
