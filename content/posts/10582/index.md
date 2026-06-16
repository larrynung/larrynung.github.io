---
title: "[VB.NET]統計英文字串中字母個數"
date: "2009-09-12 12:58:56"
description: "今天在論壇中看到一個不算難的問題，是想要能統計出英文單字的個數。由於一開始誤解了其意思，就變成了統計英文字串中字母的個數了。既然都寫了，隨手記錄一下。這問題有很多解法，這邊隨手寫了三個，也希望大家能提供一些不一樣的寫法。"
tags: [VB.NET]
---

今天在論壇中看到一個不算難的問題，是想要能統計出英文單字的個數。由於一開始誤解了其意思，就變成了統計英文字串中字母的個數了。既然都寫了，隨手記錄一下。這問題有很多解法，這邊隨手寫了三個，也希望大家能提供一些不一樣的寫法。

## 解法一

採用陣列搭配ASCII編碼來記錄出現次數

```vb
Sub Test(ByVal inputString As String)
    Dim symbolCount(25) As Integer
    Dim startAscii As Integer = Asc("a"c)
    Dim maxSymbolIdx As Integer
    Dim idx As Integer

    For Each c As Char In inputString
        idx = Asc(c) - startAscii
        symbolCount(idx) = symbolCount(idx) + 1
        If symbolCount(idx) > symbolCount(maxSymbolIdx) Then
            maxSymbolIdx = idx
        End If
    Next

    For idx = 0 To 25
        Console.Write(Chr(startAscii + idx) & ": ")
        Console.WriteLine(symbolCount(idx).ToString)
    Next
    Console.WriteLine()
    Console.Write("Max Count Symbol: ")
    Console.WriteLine(Chr(startAscii + maxSymbolIdx))
End Sub
```

##

## 解法二

```vb
Sub Test(ByVal inputString As String)
    Dim chars() As Char = inputString.ToCharArray
    Array.Sort(chars)

    Dim maxChar As Char
    Dim maxCount As Integer = 0
    Dim preChar As Char = chars(0)
    Dim count As Integer = 0
    For Each c As Char In chars
        If preChar <> c Then
            Console.Write(preChar & ": ")
            Console.WriteLine(count.ToString)
            preChar = c
            count = 0
        End If
        count += 1
        If count > maxCount Then
            maxCount = count
            maxChar = c
        End If
    Next
    Console.WriteLine()
    Console.Write("Max Count Symbol: ")
    Console.WriteLine(maxChar)
End Sub
```

## 解法三

採用Linq的Group By與Order By來做

```vb
Sub Test(ByVal inputString As String)
    Dim chars() As Char = inputString.ToCharArray
    Dim linq = From c In chars Group c By c Into Group Order By Group.Count Descending Select New With {.Symbol = c, .Count = Group.Count}
    For Each item In linq
        Console.WriteLine(item.Symbol & ": " & item.Count)
    Next
    Console.WriteLine()
    Console.Write("Max Count Symbol: ")
    Console.WriteLine(linq(0).Symbol)
End Sub
```
