---
layout: post
title: "C# 6.0 - Parameterless constructors in structs"
date: 2015-01-21 00:17:00
comments: true
tags: [CSharp, CSharp 6.0]
keywords: "C#, Parameterless Constructor, Struct"
description: "C# 6.0 - Parameterless constructors in structs"
---

在 C# 6.0 以前，Struct 會自帶 Parameterless Constructors，且不允許我們自行實作，像是下面這樣的程式碼：  

<!-- More --> 

```c# 
...
public Blog()
    : this( string.Empty, string.Empty)
{
    Console.WriteLine( "Blog.Ctor()...");
}
public Blog(string name, string url)
{
    this.Name = name;
    this.Url = url;
}
...
```

<br/>


運行在 C# 6.0 以前，編譯器就會告知錯誤：  

{% img /images/posts/ParamlessStructConstructor/1.png %}

<br/>


如果想要在 Parameterless Constructors 自行加些處理，像是用建構子鏈導到別的建構子去建構，在 C# 6.0 以前都沒辦法。  

<br/>


在 C# 6.0 以後，就比較沒有這樣的限制了，我們可以自行撰寫自己的 Paramless Constructor，加上自己想要的處理動作。唯一要注意的是需要透過 new 語法建立的才會觸發自己撰寫的 Paramless Constructor。  

```c# 
...
var blog = default( Blog);
DumpBlog(blog);

blog = new Blog()
{
    Name = "Larry Nung",
    Url = "http://larrynung.github.io"
};
DumpBlog(blog);
...
```

<br/>


最後附上完整的使用範例：  

```c# 
using System;
using System.Collections.Generic;


public class Program
{
    static void Main(string[] args)
    {
        var blog = default( Blog);
        DumpBlog(blog);


        blog = new Blog()
        {
            Name = "Level Up",
            Url = "http://larrynung.github.io"
        };
        DumpBlog(blog);
    }


    private static void DumpBlog( Blog blog)
    {
        if ( string.IsNullOrEmpty(blog.Name) || string.IsNullOrEmpty(blog.Url))
        {
            Console.WriteLine( "(Null)");
            return;
        }
        Console.WriteLine(blog.Name + " (" + blog.Url + ")" );
    }
}


struct Blog
{
    public string Name { get; set; }
    public string Url { get; set; }
    public Blog()
        : this( string.Empty, string.Empty)
    {
        Console.WriteLine( "Blog.Ctor()...");
    }
    public Blog(string name, string url)
    {
        this.Name = name;
        this.Url = url;
    }
}
```

<br/>


其運行結果如下：  

{% img /images/posts/ParamlessStructConstructor/2.png %}

