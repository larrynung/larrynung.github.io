---
layout: post
title: "FX.Configuration - Read application configuration"
date: 2016-05-17 07:49:00
comments: true
categories: [FX.Configuration]
keywords: "FX.Configuration"
description: "FX.Configuration - Read application configuration"
---

要用 FX.Configuration 讀取 Application Configuration，需先引用 FX.Configuration 套件。  

<!-- More -->

<br/>


接著在 Application Configuration 中設定資料。  

{% codeblock lang:xml %}
<?xml version="1.0" encoding="utf-8" ?> 
<configuration> 
    <appSettings> 
        <add key="Setting1" value="Larry Nung"/> 
        <add key="Setting2" value="Level Up (http://larrynung.github.io/index.html)"/> 
    </appSettings> 
</configuration>
{% endcodeblock %}

<br/>


再來要設定 Application Configuration 對應的存取類別，這邊跟一般的 Model 實作類似，只是要類別需繼承自 AppConfiguration。  

{% codeblock lang:c# %}
using FX.Configuration; 

namespace ConsoleApplication12 { 
    public class MyAppConfig: AppConfiguration{ 
        public string Setting1 { get; private set; } 
        public string Setting2 { get; private set; } 
    } 
}
{% endcodeblock %}

<br/>


準備好後就只要將類別實體化即可透過成員屬性取得 Application Configuration 的設定值。  

{% codeblock lang:c# %}
using System; 

namespace ConsoleApplication12 { 
    class Program { 
        static void Main(string[] args) { 
            var config = new MyAppConfig(); 

            Console.WriteLine(config.Setting1); 
            Console.WriteLine(config.Setting2); 
        } 
    } 
}
{% endcodeblock %}
 
<br/>


{% img /images/posts/FxConfigurationReadAPPConfig/1.png %}

<br/>

Link
----
* [NuGet Gallery | FX.Configuration 0.4.1](https://www.nuget.org/packages/FX.Configuration/)
* [friendlyx / fx.configuration — Bitbucket](https://bitbucket.org/friendlyx/fx.configuration)
