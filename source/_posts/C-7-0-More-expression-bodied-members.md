---
title: 'C# 7.0 - More expression bodied members'
date: 2017-03-07 23:54:27
tags: [CSharp, CSharp 7.0]
---

C# 7.0 擴展了 Expression bodied。  

<!-- More -->

<br/>


開始支援建構子。  

```C#
...
class Program
{
    ...
    public Program() => Console.WriteLine("Program()");
    ...
}
...
```

<br/>


支援解構子。  

```C#
...
class Program
{
    ...
    ~Program() => Console.WriteLine("~Program()");
    ...
}
...
```

<br/>


支援 property accessors。  

```C#
...
private string _myProperty;
public string MyProperty
{
    get => _myProperty;
    set => _myProperty = value;
}
...
```

<br/>


支援 event accessors。  

```C#
...
public event EventHandler MyEvent
{
    add => _myEvent += value;
    remove => _myEvent -= value;
}
...
```

<br/>


{% asset_img 1.png %}

<br/>


Link
=====
* [What’s New in C# 7.0 | .NET Blog](https://blogs.msdn.microsoft.com/dotnet/2016/08/24/whats-new-in-csharp-7-0/)
* [C# 7.0 Expression Bodied Members – csharp.christiannagel.com](https://csharp.christiannagel.com/2017/01/25/expressionbodiedmembers/)
