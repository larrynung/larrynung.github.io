---
layout: post
title: "StackExchange.Redis - Scripting"
date: 2016-05-24 23:40:00
comments: true
categories: [StackExchange.Redis]
keywords: "StackExchange.Redis"
description: "StackExchange.Redis - Scripting"
---

使用 StackExchange.Redis 開發 Redis 的 Lua Scripting 程式，只要簡單的透過 Database 物件的 ScriptEvaluateAsync 方法，將 Lua script 及所需的 keys 與 values 帶入即可。  

<!-- More -->

{% codeblock lang:c# %}
using StackExchange.Redis; 
... 
var configuration = GetConfiguration(); 
using (var conn = ConnectionMultiplexer.Connect(configuration)) 
{ 
    var db = conn.GetDatabase(); 
    var script = GetScript(); 
    var keys = GetKeys(); 
    var values = GetValues(); 
    var result = db.ScriptEvaluate(script, keys, values); 
    ... 
} 
...
{% endcodeblock %}

<br/>


像是下面這邊筆者用 Lua script 實作了類似 Redis 的 MSET 命令，可同時設定三組 Key/Value，寫起來會像下面這樣：   

{% codeblock lang:c# %}
using System; 
using StackExchange.Redis; 

namespace ConsoleApplication4 { 
    class Program { 
        static void Main(string[] args) { 
            var configuration = "localhost:6379"; 
            using (var conn = ConnectionMultiplexer.Connect(configuration)) { 
                var db = conn.GetDatabase(); 
                var script = @“
                                          redis.call('set', KEYS[1], ARGV[1]) 
                                          redis.call('set', KEYS[2], ARGV[2]) 
                                          redis.call('set', KEYS[3], ARGV[3])"; 
                var keys = new RedisKey[] {"Blog:Author", "Blog:Name", "Blog:Url"}; 
                var values = new RedisValue[] { "LarryNung", "LevelUp", "http://larrynung.github.io" }; 

               db.ScriptEvaluateAsync(script, keys, values, CommandFlags.FireAndForget); 

               Console.WriteLine(db.StringGet("Blog:Author", CommandFlags.PreferSlave));    
               Console.WriteLine(db.StringGet("Blog:Name", CommandFlags.PreferSlave));  
               Console.WriteLine(db.StringGet("Blog:Url", CommandFlags.PreferSlave)); 
          }
        } 
    } 
}
{% endcodeblock %}

<br/>


運行起來會像下面這樣：  

{% img /images/posts/ScriptingInStackExchange.Redis/1.png %}

<br/>


但這樣的方法有個問題，就是每次運行都會傳輸一次 Lua script。  

<br/>


比較好的做法是先將 Lua script 預先載到 Server 上再運行。  

{% codeblock lang:c# %}
using StackExchange.Redis; 
... 
var configuration = GetConfiguration(); 
using (var conn = ConnectionMultiplexer.Connect(configuration)) 
{ 
    var db = conn.GetDatabase(); 
    var script = GetScript(); 
    var preparedScript = LuaScript.Prepare(script); 
    var endPoint = conn.GetEndPoints().First(); 
    var server = conn.GetServer(endPoint); 
    var loadedScript = preparedScript.Load(server); 
    var result = db.ScriptEvaluate(loadedScript, new {Param1 = "LarryNung", Param2= "http://larrynung.github.io"}); 
    ...
} 
...
{% endcodeblock %}

<br/>


像是下面這樣：  

{% codeblock lang:c# %}
using System; 
using StackExchange.Redis; 

namespace ConsoleApplication4 { 
    class Program { 
        static void Main(string[] args) { 
            var configuration = "localhost:6379"; 
            using (var conn = ConnectionMultiplexer.Connect(configuration)) { 
                var db = conn.GetDatabase(); 
                var script = @" 
                                            redis.call('set', @AuthorKey, @AuthorValue) 
                                            redis.call('set', @NameKey, @NameValue) 
                                            redis.call('set', @UrlKey, @UrlValue)"; 
                var preparedScript = LuaScript.Prepare(script); 
                var endPoint = conn.GetEndPoints().First(); 
                var server = conn.GetServer(endPoint); 
                var loadedScript = preparedScript.Load(server); 

                db.ScriptEvaluate(loadedScript, new { 
                    AuthorKey = "Blog:Author", 
                    NameKey = "Blog:Name", 
                    UrlKey = "Blog:Url", 
                    AuthorValue = "LarryNung", 
                    NameValue = "LevelUp", 
                    UrlValue = "http://larrynung.github.io" }); 
                
                Console.WriteLine(db.StringGet("Blog:Author", CommandFlags.PreferSlave)); 
                Console.WriteLine(db.StringGet("Blog:Name", CommandFlags.PreferSlave)); 
                Console.WriteLine(db.StringGet("Blog:Url", CommandFlags.PreferSlave));
          }        }     } }
{% endcodeblock %}

<br/>


運行結果如下：  

{% img /images/posts/ScriptingInStackExchange.Redis/2.png %}
