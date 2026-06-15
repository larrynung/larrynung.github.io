---
title: ".NET 4.0 New Feature - Tuple"
date: "2010-11-19 12:59:23"
description: ".NET 4.0 New Feature - Tuple"
tags: [CSharp]
---
.NET 4.0在System命名空間下新增了Tuple泛型類別，用以儲存特定數目和順序的值，可做臨時性的儲存與滿足方法具有多個回傳值的需求。

.NET 4.0內建有8種Tuple泛型類別，各自帶有不同數量的泛型屬性成員。

這些Tuple泛型類別皆實作了IStructuralEquatable, IStructuralComparable, IComparable, ITuple介面，其中ITuple介面在.NET Framework 4.0中並未開出。

在Tuple泛型類別的建立上，可透過Tuple輔助類別的Create靜態方法來做建立Tuple泛型類別的動作。

像是下面範例就是在示範如何透過Tuple輔助類別來建立Tuple的物件實體：
var tupleVar= Tuple.Create(1,2,3,4);

除了透過Tuple輔助類別外，也可以直接透過Tuple泛型類別的建構子來做建構的動作：

var tupleVar = New Tuple(1, 2, 3, 4);

Tuple泛型類別建構出物件實體後，就可以透過其屬性來使用了，這邊來看一下參數最多的Tuple類別屬性，Tuple泛型類別的泛型屬性成員都為ItemN的格式命名，使用上得清楚知道各元素所存放的值為何才行。

這邊看下來可能大家會有點覺得這樣我用ArrayList去取代就好了，其實我也有點這種感覺，反正也無法從屬性中明確知道其存放值的用途，但是由於Tuple有實做IStructuralEquatable、 IStructuralComparable、IComparable這幾個介面的關係，它具有能依照元素順序去做比較大小、相等判別、與排序的功能，另外就是在使用上Tuple可以不需要轉型，個人猜測這些特性才是Tuple的主要賣點。

## 範例

using System;

namespace ConsoleApplication1
{
class Program
{
static void Main(string[] args)
{
var var1 = Tuple.Create(1, 2, 1);
var var2 = Tuple.Create(1, 1, 2);

Console.WriteLine("Var1 : {0}", var1);
Console.WriteLine("Var2 : {0}", var2);
Console.WriteLine("Var1 == Var2 : {0}", var1 == var2);
Console.WriteLine("Var1.Equals(Var2) : {0}", var1.Equals(var2));
Console.WriteLine("(Var1 as IComparable).CompareTo(Var2) : {0}", (var1 as IComparable).CompareTo(var2));

Console.WriteLine();

Console.WriteLine("Original Array...");
var tupeArray = new Tuple[] { var1, var2 };
foreach (var item in tupeArray)
Console.WriteLine(item);

Console.WriteLine();

Console.WriteLine("Sorted Array...");
Array.Sort(tupeArray);
foreach (var item in tupeArray)
Console.WriteLine(item);
}
}
}

運行結果如下：

## Link

Tuple 類別

[你必須知道的.NET]第三十二回，，深入.NET 4.0之，Tuple一二