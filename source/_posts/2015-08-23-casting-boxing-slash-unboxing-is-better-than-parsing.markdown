---
layout: post
title: "Casting (Boxing/Unboxing) is better than parsing"
date: 2015-08-23 23:45
comments: true
categories: 
keywords: 
description: "Casting (Boxing/Unboxing) is better than parsing"
---

以往我們在將 Object 中被裝箱的數值轉成數值時，大概會有兩種作法。  

<!-- More -->

<br/>

 
一種是直接將數值拆箱後使用，一種則是將 Object ToString 後再用 Parse 方法將之轉成預期的數值型態。

<br/>


以往我會覺得這沒那麼重要，兩者愛用哪個都可以，但最近在 Review 時心血來潮做了個測試才發現不是那麼一回事，兩者會有效能上的差異。  

<br/>


測試程式就像下面這樣簡單：    

{% codeblock lang:c# %}
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication16
{
    class Program
    {
        static void Main( string[] args)
        {
            var count = 1000000;
            var obj = 123;

            Console.WriteLine( "(int)obj: {0}" , DoTest(count, () =>
            {
                var value = ( int)obj;
            }));

            Console.WriteLine( "int.Parse(obj.ToString()): {0}" , DoTest(count, () =>
            {
                var value = int.Parse(obj.ToString());
            }));
        }
        static long DoTest( int count, Action action)
        {
            var sw = Stopwatch.StartNew();
            for ( int i = 0; i < count; ++i)
            {
                action();
            }
            return sw.ElapsedMilliseconds;
        }
    }
}
{% endcodeblock %}

<br/>


可以看到直接拆箱的效能比先轉成字串後再去 Parse 來的要好的多。  

{% img /images/posts/CastVSParse/1.png %}

<br/>

Link
----
* [Getting Cirrius: Performance Comparison: Casting (Boxing/Unboxing) vs Parsing](http://www.gettingcirrius.com/2010/11/performance-comparison-casting.html)
