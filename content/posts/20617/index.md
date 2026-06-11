---
title: ".Net 4.0 New Feature - SortedSet"
date: "2011-01-06 05:28:54"
description: ".Net 4.0 New Feature - SortedSet"
tags: [CSharp]
---

SortedSet是.NET 4.0新加入的類別，位於System.Collections.Generic命名空間內，能夠依排序順序維護不重覆的物件集合。為一自我平衡紅黑樹的實作，可隨著項目的插入和刪除維護排序的順序，無法從特定位置訪問特定元素，使用上與現有的HashSet類別有點類似，一樣提供許多數學集合 (Set) 運算，像是交集、聯集、與差集等，但多了自動排序的功能，此外還具備有Min、Max的取得，與取裡面子集的功能。

其重要的成員如下：

Property

Name

Description

Count

取得 SortedSet(Of T) 中的項目數目

Max

得 SortedSet(Of T) 中的最大值

Min

取得 SortedSet(Of T) 中的最小值

Method

Name

Description

Add

將項目加入至資料集，並傳回表示是否成功加入的值

CopyTo

將SortedSet(Of T) 內容複製到指定的一維陣列

ExceptWith

從目前的 SortedSet(Of T) 物件中，移除指定之集合內的所有項目,也就是取其差集

GetViewBetween

傳回 SortedSet(Of T) 中資料子集的檢視,也就是取其子集

IntersectWith

修改目前的 SortedSet(Of T) 物件，使其僅包含同時也在指定之集合中出現的項目,也就是取其交集

IsProperSubsetOf

判斷 SortedSet(Of T) 物件是否為指定之集合的真子集

IsProperSupersetOf

判斷 SortedSet(Of T) 物件是否為指定之集合的真超集

IsSubsetOf

判斷 SortedSet(Of T) 物件是否為指定之集合的子集

IsSupersetOf

判斷 SortedSet(Of T) 物件是否為指定之集合的超集

Overlaps

判斷目前的 SortedSet(Of T) 物件與指定的集合是否共用通用的項目,也就是判斷交集是否不為空

Remove

從 SortedSet(Of T) 中移除指定項目

RemoveWhere

從 SortedSet(Of T) 中移除符合指定之述詞 (Predicate) 所定義條件的所有項目

這邊來看個完整的範例

using System.Collections.Generic;
namespace ConsoleApplication1
{
class Program
{
static void Main(string[] args)
{
var setData1 = new SortedSet() { 1, 3, 5, 7, 9 };
var setData2 = new SortedSet { 2, 4, 6, 8, 10 };

int[] array = new int[setData1.Count];
setData1.CopyTo(array);
foreach (var value in array)
setData1.Add(value);

System.Console.WriteLine("setData1");
System.Console.WriteLine(string.Join(",", setData1));

System.Console.WriteLine("setData2");
System.Console.WriteLine(string.Join(",", setData2));

System.Console.WriteLine("setData1 IsSubsetOf setData2");
System.Console.WriteLine(string.Join(",", setData1.IsSubsetOf(setData2)));

System.Console.WriteLine("setData1 Overlaps setData2");
System.Console.WriteLine(string.Join(",", setData1.Overlaps(setData2)));

System.Console.WriteLine("setData1 UnionWith setData2");
var setUnion = new SortedSet(setData1);
setUnion.UnionWith(setData2);
System.Console.WriteLine(string.Join(",", setUnion));

System.Console.WriteLine("(setData1 UnionWith setData2) Reverse");
System.Console.WriteLine(string.Join(",", setUnion.Reverse()));

System.Console.WriteLine("(setData1 UnionWith setData2) Min");
System.Console.WriteLine(string.Join(",", setUnion.Min));

System.Console.WriteLine("(setData1 UnionWith setData2) Max");
System.Console.WriteLine(string.Join(",", setUnion.Max));

System.Console.WriteLine("(setData1 UnionWith setData2) GetViewBetween({0},{1})", (setUnion.Min + setUnion.Max) / 2, setUnion.Max);
System.Console.WriteLine(string.Join(",", setUnion.GetViewBetween((setUnion.Min + setUnion.Max) / 2, setUnion.Max)));

System.Console.WriteLine("(setData1 UnionWith setData2) IsSupersetOf setData1");
System.Console.WriteLine(string.Join(",", setUnion.IsSupersetOf(setData1)));

System.Console.WriteLine("(setData1 UnionWith setData2) IsSupersetOf setData2");
System.Console.WriteLine(string.Join(",", setUnion.IsSupersetOf(setData2)));

System.Console.WriteLine("setData1 IsSubsetOf (setData1 UnionWith setData2)");
System.Console.WriteLine(string.Join(",", setData1.IsSubsetOf(setUnion)));

System.Console.WriteLine("setData2 IsSubsetOf (setData1 UnionWith setData2)");
System.Console.WriteLine(string.Join(",", setData2.IsSubsetOf(setUnion)));

System.Console.WriteLine("(setData1 UnionWith setData2) IntersectWith setData2");
var setIntersect = new SortedSet(setUnion);
setIntersect.IntersectWith(setData2);
System.Console.WriteLine(string.Join(",", setIntersect));

System.Console.WriteLine("(setData1 UnionWith setData2) ExceptWith setData2");
var setExcept = new SortedSet(setUnion);
setExcept.ExceptWith(setData2);
System.Console.WriteLine(string.Join(",", setExcept));

System.Console.WriteLine("(setData1 UnionWith setData2) RemoveWhere((value) => (value % 2) == 0)");
var setRemoveWhere = new SortedSet(setUnion);
setRemoveWhere.RemoveWhere((value) => (value % 2) == 0);
System.Console.WriteLine(string.Join(",", setRemoveWhere));
}
}
}

運行結果如下：

## Link


SortedSet(Of T) 類別

SortedSet Collection Class in .NET 4.0

探討 .NET 4 新增的 SortedSet 類

[.NET Framework][C#] .NET 4 → SortedSet Collection 初探簡介

.NET Framework 4 SortedSet

.NET Framework 4.0 Newbie : SortedSet

How to use the HashSet and SortedSet Collection Classes in C# 4.0

An introduction to SortedSet Collection of dotnet 4.0

C# 4.0/BCL 4 Series:SortedSet in Framework 4