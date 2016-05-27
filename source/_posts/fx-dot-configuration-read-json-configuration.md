---
layout: post
title: "FX.Configuration - Read JSON configuration"
date: 2016-05-21 08:06:00
comments: true
categories: [FX.Configuration]
keywords: 
description: "FX.Configuration - Read JSON configuration"
---

要用 FX.Configuration 讀取 JSON Configuration，需先引用 FX.Configuration 套件。  
<!-- More -->

<br/>


接著在 JSON Configuration 中設定資料。  

{% codeblock lang:json %}
{ 
    "Setting1": "Larry Nung", 
    "Setting2": "Level Up (http://larrynung.github.io/index.html)" 
}
{% endcodeblock %}

<br/>


再來要設定 JSON Configuration 對應的存取類別，這邊跟一般的 Model 實作類似，只是要類別需繼承自 JsonConfiguration，另外要注意設定檔的位置在哪，如果是跟組件檔案同目錄下的 Config.json 檔，那我們不需多做處理，如果檔案在其他目錄下，或是檔案名稱不是 Config.json，我們可以透過建構子設定。  

{% codeblock lang:c# %}
using FX.Configuration; 

namespace ConsoleApplication12 { 
    public class MyJSONConfig: JsonConfiguration {         
        //public MyJSONConfig() 
        // : base("Config.json") 
        //{
        //} 
        public string Setting1 { get; private set; } 
        public string Setting2 { get; private set; } 
    } 
}
{% endcodeblock %}
<br/>


準備好後就只要將類別實體化即可透過成員屬性取得 JSON Configuration 的設定值。  

{% codeblock lang:c# %}
using System; 

namespace ConsoleApplication12 { 
    class Program { 
        static void Main(string[] args) { 
            var config = new MyJSONConfig(); 

            Console.WriteLine(config.Setting1); 
            Console.WriteLine(config.Setting2); 
        } 
    } 
}
{% endcodeblock %}

<br/>


{% img /images/posts/FxConfigurationReadJSONConfig/1.png %}

<br/>

Link
-----
* [NuGet Gallery | FX.Configuration 0.4.1](https://www.nuget.org/packages/FX.Configuration/)
* [friendlyx / fx.configuration — Bitbucket](https://bitbucket.org/friendlyx/fx.configuration)
