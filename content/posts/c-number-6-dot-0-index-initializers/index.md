---
title: "C# 6.0 - Index initializers"
date: "2015-01-15 23:32:00"
description: "C# 6.0 - Index initializers"
tags: [CSharp, CSharp 6.0]
---

以往我們在撰寫 C#，有 Object Initializer 與 Collection Initializer 可輔助我們作初始的動作，雖然可以初始大多數的資料，但在 Index 與 Event 這邊卻無法直接初始。

如果以 Dictionary 來說，因為他還是屬於集合的一種，所以仍舊可以像下面這樣透過 Collection Initializer 在初始的同時就將內容一併放入：

>
```c#
...
var blog1 = new Dictionary()
{
{ "Name", "Level Up" },
{ "Url", "http://larrynung.github.io/index.html" }
};
...
```
但並不是所有的情況下都可以用 Collection Initializer 來做 Index 的初始，所以在 C# 6.0 導入了 Index initializers，寫起來會像下面這樣，就像透過索引子塞值一般：
```c#
...
var blog = new Dictionary()
{
[ "Name"] = "Level Up" ,
[ "Url"] = "http://larrynung.github.io/index.html"
};

...

var larry = new Person()
{
Name = "Larry Nung",
Blogs = new Blogs()
{
[ "Level Up 1"] = new Blog ("Level Up 1" , "http://www.dotblogs.com.tw/larrynung" ),
[ "Level Up 2"] = new Blog ("Level Up 2" , "http://larrynung.github.io" )
}
};
...
```
可以看到 Index Initializer 結合 Object Initializer 使用，我們能做的事情更多了。

最後這邊來看個完整的使用範例：
```c#

using System;
using System.Collections;
using System.Collections.Generic;

public class Program
{
static void Main(string[] args)
{
var larry = new Person()
{
Name = "Larry Nung",
Blogs = new Blogs()
{
[ "Level Up 1"] = new Blog ("Level Up 1" , "http://www.dotblogs.com.tw/larrynung" ),
[ "Level Up 2"] = new Blog ("Level Up 2" , "http://larrynung.github.io" )
}
};
DumpPeron(larry);
}

private static void DumpPeron( Person person)
{
Console.WriteLine(person.Name);

foreach ( Blog blog in person.Blogs)
Console.WriteLine(blog.Name + " (" + blog.Url + ")" );
}
}

class Person
{
public string Name { get; set; }
public Blogs Blogs { get; set; }
}

class Blogs : IEnumerable
{
private Dictionary m_Pool { get; set; } = new Dictionary();

public Blog this[string name]
{
get
{
return m_Pool[name];
}
set
{
m_Pool[name] = value;
}
}

IEnumerator IEnumerable.GetEnumerator()
{
return GetEnumerator();
}
public IEnumerator GetEnumerator()
{
return (( IEnumerable)m_Pool.Values).GetEnumerator();
}
}

class Blog
{
public string Name { get; set; }
public string Url { get; set; }
public Blog(string name, string url)
{
this.Name = name;
this.Url = url;
}
}
```
運行結果如下：

![1.png](/images/posts/IndexInitializers/1.png)

Link
----
* [C# 6.0 – Index Initializers | Didactic Code](http://davefancher.com/2014/08/08/c-6-0-index-initializers/)