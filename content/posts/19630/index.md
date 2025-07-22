---
title: ".NET 4.0 New Feature - String.Join"
date: "2010-11-22 08:08:33"
description: ".NET 4.0 New Feature - String.Join"
tags: [CSharp]
---.NET Framework 4.0新增了三個String.Join的多載函式Join(String, IEnumerable)、Join(String, IEnumerable)、與Join(String, Object[])。

這三個多載函式可以看出，我們可傳入Object[]、IEnumerable這三種新的型態，不需再將List、StringCollection等型態的資料塞成String[]就可以使用，也能在陣列中放入不同的型態，不需先將集合元素轉成字串，這部份在4.0(含)以後.NET Framework會幫我們做掉了。

完整的使用範例如下：
using System;
using System.Collections.Generic;

namespace ConsoleApplication1
{
class Program
{
static void Main(string[] args)
{
String[] stringCollection = { "123", "456", "789" };
int[] intCollection = { 123, 456, 789 };
Object[] objCollection = { 123, "456", 789.0f };
float[] floatCollection = { 123.0f, 456.0f, 789.0f };

ShowValue("stringCollection", stringCollection);
ShowValue("intCollection", intCollection);
ShowValue("objCollection", objCollection);
ShowValue("floatCollection", floatCollection);
}

static void ShowValue(string title, IEnumerable values)
{
Console.WriteLine("{0}: {1}", title, string.Join(",", values));
}
}
}

運行結果如下：

也可以整理成IEnumerable的擴充方法使用。

public static class IEnumerableExtension
{
public static string Join(this IEnumerable obj, string seperator)
{
return string.Join(seperator, obj);
}
}

這邊將上面的範例改為擴充方法的版本：

using System;
using System.Collections.Generic;

namespace ConsoleApplication1
{
class Program
{
static void Main(string[] args)
{
String[] stringCollection = { "123", "456", "789" };
int[] intCollection = { 123, 456, 789 };
Object[] objCollection = { 123, "456", 789.0f };
float[] floatCollection = { 123.0f, 456.0f, 789.0f };

Console.WriteLine("{0}: {1}", "stringCollection", stringCollection.Join(","));
Console.WriteLine("{0}: {1}", "intCollection", intCollection.Join(","));
Console.WriteLine("{0}: {1}", "objCollection", objCollection.Join(","));
Console.WriteLine("{0}: {1}", "floatCollection", floatCollection.Join(","));
}
}

public static class IEnumerableExtension
{
public static string Join(this IEnumerable obj, string seperator)
{
return string.Join(seperator, obj);
}
}
}

## Link

String.Join 方法