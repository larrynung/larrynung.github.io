---
layout: post
title: "FX.Configuration - Read mixed configuration"
date: 2016-05-21 14:53:00
comments: true
tags: [FX.Configuration]
keywords: "FX.Configuration"
description: "FX.Configuration - Read mixed configuration"
---

要用 FX.Configuration 同時讀取 Application 與 JSON Configuration，需先引用 FX.Configuration 套件。  

<!-- More -->

<br/>


接著在 Application Configuration 中設定資料。  

{% codeblock lang:xml %}
<?xml version="1.0" encoding="utf-8" ?> 
<configuration> 
    <appSettings> 
        <add key="Setting1" value="Larry Nung"/>    </appSettings> 
</configuration>
{% endcodeblock %}

<br/>


以及在 JSON Configuration 中設定資料。 

{% codeblock lang:json %}
{     
    "Setting2": "Level Up (http://larrynung.github.io/index.html)" 
}
{% endcodeblock %}

<br/>


再來要設定 Configuration 對應的存取類別，這邊跟一般的 Model 實作類似，只是要類別需繼承自 MixedConfiguration。

{% codeblock lang:c# %}
using FX.Configuration; 

namespace ConsoleApplication12 { 
    public class MyMixedConfig : MixedConfiguration { 
        public string Setting1 { get; private set; } 
        public string Setting2 { get; private set; } 
    } 
}
{% endcodeblock %}

<br/>


準備好後就只要將類別實體化即可透過成員屬性取得 Configuration 的設定值。  

{% codeblock lang:c# %}
using System; 

namespace ConsoleApplication12 { 
    class Program { 
        static void Main(string[] args) { 
            var config = new MyMixedConfig(); 

            Console.WriteLine(config.Setting1); 
            Console.WriteLine(config.Setting2); 
        } 
    } 
}
{% endcodeblock %}

<br/>


{% img /images/posts/FxConfigurationReadMixedConfig/1.png %}

<br/>

Link
----
* [NuGet Gallery | FX.Configuration 0.4.1](https://www.nuget.org/packages/FX.Configuration/)
* [friendlyx / fx.configuration — Bitbucket](https://bitbucket.org/friendlyx/fx.configuration)
