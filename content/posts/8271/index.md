---
title: "[C#]HashSet 集合型別"
slug: "[CSharp]HashSet 集合型別"
date: "2009-05-02 04:39:12"
description: "[C#]HashSet 集合型別"
tags: [CSharp]
---
##
Namespace

System.Collections.Generic

##
Assemble

System.Core (在 System.Core.dll 中)

##
需求

.NET Framework 3.5(含)以上

##
功能

以數學集合 (Set) 模型為基礎，並提供高效能的集合 (Set) 運算，類似存取 Dictionary)>) 或 Hashtable 集合 (Collection) 的索引鍵。簡而言之，您可以將 HashSet)>) 類別視為沒有值的 Dictionary)>) 集合 (Collection)。

不會排序，也無法包含重複的項目。如果對應用程式來說，排序和項目重複比效能更重要，請使用 List)>) 類別配合 Sort 方法。

提供許多數學集合 (Set) 運算，例如集合 (Set) 相加 (結合) 以及集合 (Set) 相減。

##
簡易範例

執行結果如下：

由此範例可看到Hashset會自動忽略重覆的資料。

##
Reference

.NET Framework 開發人員手冊-HashSet 集合型別

.NET Framework 類別庫-HashSet(T) 類別