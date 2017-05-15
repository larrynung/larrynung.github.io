---
layout: post
title: "C# 6.0 - Nameof expressions"
date: 2014-08-25 23:40:00
comments: true
tags: [CSharp, CSharp 6.0]
keywords: "C#"
description: "C# 6.0 - Nameof expressions"
---

Nameof expressions 是預計要在 C# 6.0 釋出的新功能，目前已可在 Visual Studio 14 CTP3 中透過設定將功能開啟進行體驗，只要在方案檔中加上：

<!-- More -->

    <LangVersion>experimental</LangVersion>


Nameof expressions 能讓開發人員輕易的在程式中取得變數或是類別名稱。 

<br/>

以往我們是無法取得變數名稱的，所以像是在撰寫參數檢查，當丟出的例外需要帶入參數名稱時，多半是自己填入字串帶入。但這樣的做法不是很恰當，因為拼錯時並不容易發現，且當重構參數名稱時很容易遺漏要配合修改。  

<br/>

至於類別名稱的取得，相較於變數名稱的取得是簡單了許多。但是名稱的取得需要 Runtime 進行解析，這樣的做法有時又多了一些無謂的耗費。  

<br/>

Nameof expressions 的出現能幫助開發人員解決這樣的問題，使用上只要叫用nameof，並帶入欲取得名稱的類別或變數即可。 

    nameof( 欲取得名稱的類別或變數 )


這邊直接看個完整的使用範例: 

```c#
using System;

namespace ConsoleApplication10
{
    class Program
    {
        static void Main(string[] args)
        {
            var blog = new Blog
            {
                Name = "Level Up" ,
                Url = "http://larrynung.github.io/"
            };


            DumpBlogInfo(blog);
            DumpBlogInfo(null);
        }


        static void DumpBlogInfo(Blog blog)
        {
            Console.WriteLine( string.Format( "Dump data (Type is {0})..." , nameof(Blog )));


            if (blog == null) throw new ArgumentNullException(nameof (blog));
           
            Console.WriteLine(blog .Name);
            Console.WriteLine(blog .Url);
            Console.WriteLine();
        }
    }


    class Blog
    {
        public string Name { get; set; }
        public string Url { get; set; }
    }
}
```


其運行結果如下:  

{% img /images/posts/NameofExpression/1.png %}

<br/>


可以看到程式中很輕易的就取得了類別與變數的名稱。 

<br/>

最後反組譯看一下，可以發現使用 Nameof expressions 功能，編譯器會在編譯時幫我們編譯成對應的字串，所以 Runtime 時無需額外的解析耗費。  

{% img /images/posts/NameofExpression/2.png %}

