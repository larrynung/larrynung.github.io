---
layout: post
title: "UniqueIdGenerator - C# implementation of Twitter's Snowflake"
date: 2016-04-07 05:43:00
comments: true
tags: 
keywords: 
description: "UniqueIdGenerator - C# implementation of Twitter's Snowflake"
---

UniqueIdGenerator 是 Twitter Snowflake ID 的 C# 實作。  

<!-- More -->

<br/>


產生的 ID 預設有 64 bit，就一個 long 的大小，由 41 bit 為 Timestamp，10 bit 為 Generator id，13 bit 的 Sequence 所組成。

<br/>


使用上要先透過 NuGet 安裝 UniqueIdGenerator 套件。  

{% img /images/posts/UniqueIdGenerator/1.png %}

<br/>


{% img /images/posts/UniqueIdGenerator/2.png %}

<br/>


接著引用 UniqueIdGenerator.Net 命名空間，帶入 Generator id 與 EPoch 建立 Generator，然後調用 Next() 取得文字型態的 ID，或是透過 NextLong() 取得數值型態的 ID 即可。 
{% codeblock lang:c# %}
...
using UniqueIdGenerator.Net;
...
var generatorID = GetGeneratorID();
var epoch = GetEPoch();
var generator = new Generator(generatorID, epoch);
...
var id = generator.Next();
var idValue = generator.NextLong();
...
{% endcodeblock %}

<br/>


最後附上完整的測試範例：  

{% codeblock lang:c# %}
using System;  
using System.Net;
using UniqueIdGenerator.Net;

namespace ConsoleApplication32
{
    class Program
    {
        static void Main( string[] args)
        {
            var localIp = short.Parse(Dns .Resolve(Dns .GetHostName()).AddressList[0].ToString().Split('.')[3]);
            var generator = new Generator(localIp, new DateTime(1970,1,1));
           
            for ( var idx = 0; idx < 100; ++idx)
            {
                Console.WriteLine(generator.Next());
                Console.WriteLine(generator.NextLong());
            }
        }
    }
}
{% endcodeblock %}

<br/>


運行結果如下：  

{% img /images/posts/UniqueIdGenerator/3.png %}

<br/>

Link
-----
* [mschuler/UniqueIdGenerator: C# implementation of Twitter's Snowflake](https://github.com/mschuler/UniqueIdGenerator)
