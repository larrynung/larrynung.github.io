---
layout: post
title: "C# 7.0 - Digit separators"
date: 2016-05-21 00:00:00
comments: true
tags: [CSharp, CSharp 7.0]
keywords: 
description: "C# 7.0 - Digit separators"
---

以前在開發 C# 時，如果數值過大，在閱讀上會十分不易。  

<!-- More -->

<br/>


C# 7.0 以後提供了 Digit separators 功能，允許開發人員使用 `_` 將數值做些分隔，有效解決了上述問題。最普遍的用法就是將數值做千分位分隔，像是下面這樣：  

{% codeblock lang:c# %}
using System;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            var values = new int[] { 1_000, 1_000_000, 0b1_000 };

            foreach (var value in values)
            {
                Console.WriteLine(value.ToString());
            }
        }
    }
}
{% endcodeblock %}

<br/>


{% img /images/posts/CSharp7DigitSeparators/1.png %}

<br/>

Link
----
* [C# 7 features preview · Anton Sizikov](http://asizikov.github.io/2016/04/02/csharp-seven-preview/)
* [Exploring Visual Studio "15" Preview and Playing with C# 7](https://blog.cdemi.io/exploring-visual-studio-15-preview-and-playing-with-c-7/)
* [Test driving C# 7 features in Visual Studio “15” Preview » Thomas Levesque's .NET blog](http://www.thomaslevesque.com/2016/04/16/test-driving-c-7-features-in-visual-studio-15-preview/)
