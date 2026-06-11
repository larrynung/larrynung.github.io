---
title: ".NET 4.0 New Feature - String.Concat"
date: "2010-11-23 12:26:01"
description: ".NET 4.0 New Feature - String.Concat"
tags: [CSharp]
---

.NET Framework 4.0新增了兩個String.Concat的多載函式Concat(IEnumerable)、與Concat(IEnumerable)。

這兩個新的多載函式跟String.Join的新多載函式類似，能幫我們串連IEnumerable集合中的元素，不必預先將元素轉換為字串後再處理，同時也支援更多的集合類型。

完整範例如下：

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
Console.WriteLine("{0}: {1}", title, string.Concat(values));
}
}
}

運行結果如下：

## Link


String.Concat 方法