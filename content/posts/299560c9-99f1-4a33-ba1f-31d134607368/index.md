---
title: ".NET 4.0 New Feature - Path.Combine"
date: "2013-11-06 12:00:00"
description: ".NET 4.0 New Feature - Path.Combine"
---

在.NET 4.0以前Path.Combine只能將兩個路徑合併，因此有時候我們在處理路徑時，若有多個路徑合併的需求，我們必須像下面這樣重覆叫用Path.Combine方法來達成這樣的功能：

	Console.WriteLine(Path.Combine(Path.Combine("c:\123", "456"), "789"))

	或是自行撰寫個方法去做這樣的合併動作：

	Function CombinePathes(ByVal ParamArray pathes As String()) As String
        Dim combinedPath As String = pathes.FirstOrDefault
        For idx As Integer = 1 To pathes.Count - 1
            combinedPath = IO.Path.Combine(combinedPath, pathes(idx))
        Next
        Return combinedPath
    End Function

	在.NET 4.0以後，Path.Combine又多了三個多載函式，有允許傳入路徑字串陣列的、有傳入三個路徑去做合併的、也有傳入四個路徑去做合併的。

	其中以傳入路徑字串陣列的多載版本最為重要，看起來可以Cover其它兩個多載版本，允許傳入任意個數的路徑去做合併，使用上非常簡單，這邊不多作解釋直接看下面的使用範例就可以了：

	Console.WriteLine(Path.Combine("c:\123", "456", "789"))
Console.WriteLine(Path.Combine(New String() {"c:\123", "456", "789"}))

## 
	Link

		Path.Combine 方法