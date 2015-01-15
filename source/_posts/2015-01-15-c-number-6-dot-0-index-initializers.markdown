---
layout: post
title: "C# 6.0 - Index initializers"
date: 2015-01-15 23:32
comments: true
categories: [C#]
keywords: "C#, Index initializers"
description: "C# 6.0 - Index initializers"
---

以往在初始 Dictionary，我們可能是宣告出 Dictionary 實體後，再將其內容加入 Dictionary 內，或是像下面這樣透過 Collection Initializer 在初始的同時就將內容一併放入：  
<!-- More -->
>
{% codeblock lang:c# %}
...
var blog1 = new Dictionary<string , string >()
{
    { "Name", "Level Up" },
    { "Url", "http://larrynung.github.io/index.html" }
};
...
{% endcodeblock %}

<br/>


在 C# 6.0 導入了 Index initializers，我們多了一個選擇，也可以像下面這樣撰寫，就像透過索引子在塞值一般：

{% codeblock lang:c# %}
...
var blog2 = new Dictionary<string , string >()
{
    [ "Name"] = "Level Up" ,
    [ "Url"] = "http://larrynung.github.io/index.html"
};
...
{% endcodeblock %}

<br/>


最後來看個完整的使用範例：

{% codeblock lang:c# %}
using System;
using System.Collections.Generic;


public class Program
{
    public static void Main()
    {
        var blog1 = new Dictionary<string , string >()
        {
            { "Name", "Level Up" },
            { "Url", "http://larrynung.github.io/index.html" }
        };


        var blog2 = new Dictionary<string , string >()
        {
            [ "Name"] = "Level Up" ,
            [ "Url"] = "http://larrynung.github.io/index.html"
        };


        DumpBlog(blog1);  
        DumpBlog(blog2);
    }


    private static void DumpBlog( Dictionary<string , string > blog)
    {
        Console.WriteLine( string.Format( "Blog: {0}", blog["Name" ]));
        Console.WriteLine( string.Format( "Url: {0}", blog["Url" ]));
    }
}
{% endcodeblock %}

<br/>


運行結果如下：

{% img /images/posts/IndexInitializers/1.png %}

<br/>


Link
----
* [C# 6.0 – Index Initializers | Didactic Code](http://davefancher.com/2014/08/08/c-6-0-index-initializers/)

