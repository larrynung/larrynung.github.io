---
layout: post
title: "C# 7.0 - Local functions"
date: 2016-05-11 06:21:00
comments: true
tags: [CSharp, CSharp 7.0]
keywords: 
description: "C# 7.0 - Local functions"
---
有時候我們在開發程式時，會碰到一些情境是需要建立個方法，但這個方法只有某個地方會用到，這時我們多半是用委派去做掉，但帶來的問題就是會有額外的記憶體耗費，而且無法被 inline 處理。 

<!-- More -->

<br/>

C# 7.0 後，我們可以改用 Local functions 功能去處理。使用方式很簡單，就是一般的方法宣告，只是是寫在方法裡面。像是：  

{% codeblock lang:c# %}
using System;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            void SayHello(string name)
            {
                Console.WriteLine(string.Format("Hello~{0}", name));
            }

            SayHello("Larry");
        }
    }
}
{% endcodeblock %}

<br/>


這邊也可以搭配使用 C# 6.0 的 Expression Bodied Members，程式碼會更為精簡。 

{% codeblock lang:c# %}
using System;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            void SayHello(string name) =>  Console.WriteLine(string.Format("Hello~{0}", name));

            SayHello("Larry");
        }
    }
}
{% endcodeblock %}

<br/>


運行結果如下： 

{% img /images/posts/CSharp7LocalFunctions/1.png %}

<br/>


反組譯看一下： 

{% img /images/posts/CSharp7LocalFunctions/2.png %}

<br/>


可以看到編譯器幫我們產生了對應的方法以供調用，因此使用上無需額外的記憶體消耗，還能被 inline 處理。 

<br/>

Link
----
* [C# 7 New Features: Non-Nullable references, Local Functions, Immutable Objects](https://www.kenneth-truyers.net/2016/01/25/new-features-in-c-sharp-7-part-2/)
* [C# 7.0 Local Functions](http://druss.co/2016/04/c-7-0-local-functions/)
* [New features of C# 7.0](http://www.c-sharpcorner.com/article/all-about-C-Sharp-7-features/)
