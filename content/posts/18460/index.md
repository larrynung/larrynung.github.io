---
title: "[VB.NET]使用Enum.Parse將數值或列舉型別常數名稱轉換成列舉型別物件"
date: "2010-10-19 11:25:07"
description: "[VB.NET]使用Enum.Parse將數值或列舉型別常數名稱轉換成列舉型別物件"
tags: [VB.NET]
---

在研究列舉型別的新成員時，發現在 Enum.Parse中有些之前未注意到的地方，這邊將之整理一下。

Enum.Parse具有兩個多載方法，兩個多載方法的差異只在於在轉換列舉型別物件時是否會依照大小寫的不同下去處理。

在使用Enum.Parse轉換時，可以帶入的參數有列舉型別成員之基礎值或具名常數，或以逗號 (,) 分隔之具名常數清單的字串表示。

以下面的列舉為例：
Enum Colors As Integer
None = 0
Red = 1
Green = 2
Blue = 4
End Enum

我們可以像下面這般將數值轉換回列舉

Dim value As String = "1"
Dim colorValue As Colors = CType([Enum].Parse(GetType(Colors), value), Colors)

把列舉型別常數名稱轉回列舉

Dim value As String = "Red"
Dim colorValue As Colors = CType([Enum].Parse(GetType(Colors), value), Colors)

或是透過逗號串起的列舉型別常數名稱轉回列舉

Dim value As String = String.Join(",", New Object() {"None", "Red", "Green"})
Dim colorValue As Colors = CType([Enum].Parse(GetType(Colors), value), Colors)

特別注意，由於要轉換的資料不一定能對應到列舉，有可能帶入不能轉換的資料，造成ArgumentException例外發生，因此必須使用例外處理包住，或是透過Enum.IsDefined先做判別處理。

## Link

Enum.Parse 方法