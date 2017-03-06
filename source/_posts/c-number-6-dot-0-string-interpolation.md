---
layout: post
title: "C# 6.0 - String interpolation"
date: 2015-01-15 07:51:00
comments: true
tags: [CSharp, CSharp 6.0]
keywords: "C#, 6.0, String Interpolation"
description: "C# 6.0 - String interpolation"
---

以往在做比較簡單的字串串接，我們可能會用 + 運算符號進行串接，或是用 String.Format 帶入 Pattern 與要串接的字串去處理，像是下面這樣：  

<!-- More -->
{% codeblock lang:c# %}
...
Console.WriteLine((++idx).ToString("D2") + ". " + blog.Name + " (" + blog.Url + ")");

Console.WriteLine( String.Format( "{0:D2}. {1} ({2})", ++idx, blog.Name, blog.Url));
...
{% endcodeblock %}

<br/>


在 C# 6.0 導入了 String Interpolation，可以像下面這樣簡化寫法：  

{% codeblock lang:c# %}
...
Console.WriteLine( "\{++idx, 5 :D2 }. \{blog.Name } (\{blog.Url ?? String.Empty})" );
...
{% endcodeblock %}

<br/>


有點像是本來 String.Format 的 Pattern 內直接用斜線與大括號包住帶入運算式，且支援 optional alignment 與 format specifiers 的設定。  

<br/>


這邊來看個完整的使用範例：  

{% codeblock lang:c# %}
using System;
using System.Collections.Generic;


public class Program
{
    static void Main(string[] args)
    {
        var blog = new Blog
        {
            Name = "Level Up",
            Url = "http://larrynung.github.io/"
        };

        var idx = 0;
        Console.WriteLine((++idx).ToString( "D2") + ". " + blog.Name + " (" + blog.Url + ")");
        Console.WriteLine( String.Format( "{0:D2}. {1} ({2})", ++idx, blog.Name, blog.Url));
        Console.WriteLine( "\{++idx : D2 }. \{blog.Name } (\{blog.Url })");
    }
}

class Blog
{
    public string Name { get; set; }
    public string Url { get; set; }
}
{% endcodeblock %}

<br/>


運行結果如下：  

{% img /images/posts/StringInterpolation/1.png %}

<br/>


反組譯看一下，其實背後也是將其編譯成 String.Format。  

{% img /images/posts/StringInterpolation/2.png %}

<br/>


Link
----
* [String interpolation - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/String_interpolation)
* [What’s new in C# 6.0? - String Interpolation - CodeProject](http://www.codeproject.com/Articles/846566/What-s-new-in-Csharp-String-Interpolation)
