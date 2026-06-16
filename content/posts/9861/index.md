---
title: "[C#]C# 4.0 動態繫結 (Dynamic Lookup)"
slug: "[CSharp]C# 4.0 動態繫結 (Dynamic Lookup)"
date: "2009-08-05 09:02:48"
description: "Introduction 動態繫結是C# 4.0的特色之一，其功能在現階段與晚期繫結大同小異。有用過VB.NET晚期繫結的，相信都能很快速的上手。主要能讓程式在執行階段才指定型別，並進行動態叫用。"
tags: [CSharp]
---

## Introduction

動態繫結是C# 4.0的特色之一，其功能在現階段與晚期繫結大同小異。有用過VB.NET晚期繫結的，相信都能很快速的上手。主要能讓程式在執行階段才指定型別，並進行動態叫用。

> VB.NET在VB2005 (VB 7.0)開始支援晚期繫結 (Late-Binding)

## Support

* C# 4.0 or latter

## 動態繫結

動態繫結最大的功能就是能在執行階段才決定指定的型態，並在執行階段做型別檢查，且可動態叫用函示、運算、索引子、屬性、與欄位。不論你的物件是從COM、IronPython、HTML DOM、或是reflection所取得，動態繫結允許你採用一至的方法動態的去叫用它。

此外，使用動態繫結還有個好處，就是可以精簡程式碼。

像下面這樣的程式

```csharp
Calculator calc = GetCalculator();
int sum = calc.Add(10, 20);
```

在以往要達到動態的效果，我們可能會用反射來寫

```csharp
object calc = GetCalculator();
Type calcType = calc.GetType();
object res = calcType.InvokeMember("Add",
    BindingFlags.InvokeMethod, null,
    new object[] { 10, 20 });
int sum = Convert.ToInt32(res);
```

或是寫成像下面這樣

```csharp
ScriptObject calc = GetCalculator();
object res = calc.Invoke("Add", 10, 20);
int sum = Convert.ToInt32(res);
```

但有了動態繫結我們可以更為精簡

```csharp
dynamic calc = GetCalculator();
int sum = calc.Add(10, 20);
```

> 在使用動態繫結時，IDE的IntelliSense功能會無法提示。不用太在意，直接輸入就可以了。若輸入錯誤或該成員不存在，則程式會在執行階段做告知的動作。

## 使用方式

在C# 4.0中要使用動態繫結我們可以使用dynamic關鍵字。讓我們直接來看New Features in C# 4.0文件中的程式碼片段。

```csharp
dynamic d = GetDynamicObject(…);
d.M(7); // calling methods
d.f = d.P; // getting and settings fields and properties
d[“one”] = d[“two”]; // getting and setting thorugh indexers
int i = d + 3; // calling operators
string s = d(5,7); // invoking as a delegate
```

相信多數人光看這個程式碼片段還是很模糊，但起碼能從中了解它能動態叫用方法、欄位與運算子、索引子、委派。

接著我們再看一範例應該就會清楚些

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication16
{
    class Program
    {
        static void Main(string[] args)
        {
            dynamic[] ds = new dynamic[2];
            ds[0] = new System.Windows.Forms.TextBox(){Name="TextBox"};
            ds[1] = new Person() { Name = "Larry" };
            foreach (dynamic d in ds)
            {
                Console.WriteLine(d.Name);
            }
        }
    }
    class Person
    {
        public string Name { get; set; }
    }
}
```

由於不用把型態從Object轉回匿名型別，因此動態繫結也可以用在匿名型別上，真的方便許多,看來以後若要偷懶直接傳遞匿名型別也可以了(不建議也不鼓勵濫用)。

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication19
{
    class Program
    {
        static void Main(string[] args)
        {
            dynamic d = new { Name = "Larry" };
            Console.WriteLine(d.Name);

            d = GetLarry();
            Console.WriteLine(d.Name);
        }

        static dynamic GetLarry()
        {
            return new { Name = "Larry" };
        }
    }
}
```

就算回傳值改為Object也可以使用

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication19
{
    class Program
    {
        static void Main(string[] args)
        {
            dynamic d = new { Name = "Larry" };
            Console.WriteLine(d.Name);

            d = GetLarry();
            Console.WriteLine(d.Name);
        }

        static Object GetLarry()
        {
            return new { Name = "Larry" };
        }
    }
}
```

## Link

* [C# 4.0（VB 10）與CLR 4.0之驚鴻一瞥](http://blog.miniasp.com/post/2009/02/CSharp-40-VB-10-CLR-4.aspx)
* [C# 4.0 新特性：動態型別、選用參數、具名參數](http://blog.miniasp.com/post/2009/02/CSharp-40-New-Features-Dynamic-Lookup-and-Named-and-Optional-Arguments.aspx)
* [New Features in C# 4.0](http://code.msdn.microsoft.com/csharpfuture/Release/ProjectReleases.aspx?ReleaseId=1686)
* [C# 4.0 Dynamic Lookup - Are You Kidding Me?](http://www.dev102.com/2008/11/03/c-40-dynamic-lookup-are-you-kidding-me/)
* [C# 4.0's New Features Explained](http://www.codeproject.com/KB/cs/CSharp4Features.aspx?msg=3110596)
* [C# 4.0 新功能：動態繫結](http://huan-lin.blogspot.com/2009/02/dynamic-binding-in-csharp-4.html)
* [Dynamic Lookup & dynamic Type, C# 4.0 Part 1](http://towardsnext.wordpress.com/2009/03/16/dynamic-lookup-dynamic-type-c-40-part-1/)
