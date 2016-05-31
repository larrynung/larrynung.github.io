---
layout: post
title: "Jil - Fast .NET JSON (De)Serializer"
date: 2015-09-30 00:05:00
comments: true
tags: [Jil]
keywords: "Jil"
description: "Jil - Fast .NET JSON (De)Serializer"
---

Jil 是 JSON 處理的套件，號稱比 JSON.NET 更快，甚至是當前套件中處理起來第二快的，僅次於 Protobuf。  

<!-- More -->

{% img /images/posts/Jil/1.png %}

<br/>


{% img /images/posts/Jil/2.png %}

<br/>


{% img /images/posts/Jil/3.png %}

<br/>


{% img /images/posts/Jil/4.png %}

<br/>


{% img /images/posts/Jil/5.png %}

<br/>


{% img /images/posts/Jil/6.png %}

<br/>


只要加入 Nuget 參考，Using Jil 命名空間即可開始使用。  

<br/>


要序列化時，可將物件帶入 JSON.Serialize 方法，方法會回傳序列化後的 JSON 字串。  

{% codeblock lang:c# %}
...
var json = JSON.Serialize(larry);
...
{% endcodeblock %}

<Br/>



解序列化時，可將 JSON 字串帶入 JSON.Deserialize，並利用範型指定所要解回的物件型態即可。  

{% codeblock lang:c# %}
...
larry = JSON.Deserialize<Person>(json);
...
{% endcodeblock %}

<br/>



此外，它也支援動態解析的能力，使用上只要將 JSON 字串帶入 JSON.DeserializeDynamic 即會回傳 Dynamic 物件。   

{% codeblock lang:c# %}
...
var person = JSON.DeserializeDynamic(json);
...
{% endcodeblock %}

<br/>



完整的操作範例如下：  

{% codeblock lang:c# %}
using Jil;
using System;

namespace ConsoleApplication5
{
    class Program
    {
        static void Main(string[] args)
        {
            var larry = new Person
            {
                Name = "Larry Nung",
                NickName = "Larry"
            };

            var json = JSON.Serialize(larry);

            Console.WriteLine(json);


            larry = JSON.Deserialize<Person>(json);

            Console.WriteLine("{0} ({1})", larry.Name, larry.NickName);

          
            var person = JSON.DeserializeDynamic(json);

            Console.WriteLine("{0} ({1})", person.Name, person["NickName"]);
        }
    }

    public class Person
    {
        public String Name { get; set; }

        public String NickName { get; set; }
    }
}
{% endcodeblock %}

{% img /images/posts/Jil/7.png %}

<br/>


接著我們看一下序列化時效能上的比較：

{% codeblock lang:c# %}
using Jil;
using Newtonsoft.Json;
using System;
using System.Diagnostics;
using System.IO;
namespace ConsoleApplication5
{
    class Program
    {
        static void Main(string[] args)
        {
            Person Larry = new Person
            {
                Name = "Larry Nung",
                NickName = "蹂躪"
            };

            var count = 1000000;

            Console.WriteLine("Newtonsoft: {0} ms", DoTest(count, () =>
            {
                var json = JsonConvert.SerializeObject(Larry);
            }));

            Console.WriteLine("Jil: {0} ms", DoTest(count, () =>
            {
                var json = JSON.Serialize(Larry);
            }));
        }

        static long DoTest(int count, Action action)
        {
            var sw = Stopwatch.StartNew();
            for (int i = 0; i < count; ++i) action();
            return sw.ElapsedMilliseconds;
        }
    }

    public class Person
    {
        public String Name { get; set; }

        public String NickName { get; set; }
    }
}
{% endcodeblock %}

{% img /images/posts/Jil/8.png %}

<br/>


{% img /images/posts/Jil/9.png %}

<br/>


接著看一下解列化時的效能比較：  

{% codeblock lang:c# %}
using Jil;
using Newtonsoft.Json;
using System;
using System.Diagnostics;
using System.IO;

namespace ConsoleApplication5
{
    class Program
    {
        static void Main(string[] args)
        {
            Person Larry = new Person
            {
                Name = "Larry Nung",
                NickName = "蹂躪"
            };

            var json = JsonConvert.SerializeObject(Larry);
            var count = 1000000;

            Console.WriteLine("Newtonsoft: {0} ms", DoTest(count, () =>
            {
                var person = JsonConvert.DeserializeObject<Person>(json);
            }));

            Console.WriteLine("Jil: {0} ms", DoTest(count, () =>
            {
                var person = JSON.Deserialize<Person>(json);
            }));
        }

        static long DoTest(int count, Action action)
        {
            var sw = Stopwatch.StartNew();
            for (int i = 0; i < count; ++i) action();
            return sw.ElapsedMilliseconds;
        }
    }

    public class Person
    {
        public String Name { get; set; }

        public String NickName { get; set; }
    }
}
{% endcodeblock %}

{% img /images/posts/Jil/10.png %}

<br/>


{% img /images/posts/Jil/11.png %}

<br/>


可以看到 Jil 在 JSON 的處理上的確有著較佳的效率。  

<br/>

Link
----
* [kevin-montrose/Jil](https://github.com/kevin-montrose/Jil)
