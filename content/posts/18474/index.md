---
title: ".NET 4.0 New Feature - StringBuilder.Clear"
date: "2010-10-20 09:12:02"
description: ".NET 4.0 New Feature - StringBuilder.Clear"
tags: [VB.NET]
---

以往在使用StringBuilder時，若要重覆使用現有的StringBuilder物件，必需要將StringBuilder的內容清空，然而在StringBuilder類別中並未附有直覺的方法可供直接叫用，因此我們可能需要透過StringBuilder.Remove方法來清空內容。

```vb
Dim str = New StringBuilder()
...
str.Remove(0, str.Length)
...
```

或是透過把StringBuilder.Length設為0的方式來清除內容。

```vb
Dim str = New StringBuilder()
...
str.Length = 0
...
```

但這樣的做法總是有點不直覺，撰寫上也不太方便，因此在.NET 4.0中StringBuilder類別多加了Clear方法可以直接叫用，該方法把StringBuilder.Length設為0的方式給包裝了起來，直接叫用就可以清除掉StringBuilder中的內容。

```vb
Dim str = New StringBuilder()
...
str.Clear()
...
```

這邊將三種方法做個測試比較，測試程式如下：

```vb
Imports System.Text

Module Module1

    Sub Main()
        Dim str As New StringBuilder
        Dim size As Integer = 100000000

        Dim sw As New Stopwatch

        '預先編譯降低測試誤差
        AppendData(str, size)
        ClearData1(str)
        ClearData2(str)
        ClearData3(str)

        '開始測試
        AppendData(str, size)
        Console.WriteLine("Test Remove...")
        sw.Restart()
        ClearData1(str)
        Console.WriteLine(sw.ElapsedMilliseconds)

        AppendData(str, size)
        Console.WriteLine("Test Length...")
        sw.Restart()
        ClearData2(str)
        Console.WriteLine(sw.ElapsedMilliseconds)

        AppendData(str, size)
        Console.WriteLine("Test Clear...")
        sw.Restart()
        ClearData3(str)
        Console.WriteLine(sw.ElapsedMilliseconds)
    End Sub

    Private Sub AppendData(ByVal str As StringBuilder, ByVal size As Integer)
        str.Append(New String("0", size))
    End Sub

    Private Sub ClearData1(ByVal str As StringBuilder)
        str.Remove(0, str.Length)
    End Sub

    Private Sub ClearData2(ByVal str As StringBuilder)
        str.Length = 0
    End Sub

    Private Sub ClearData3(ByVal str As StringBuilder)
        str.Clear()
    End Sub

End Module
```

感覺速度上是沒有太大的差異，挑自己順手的方法寫就好了。

![image_thumb.png](/images/posts/18474/image_thumb.png)

## Link

* [StringBuilder.Clear 方法](http://msdn.microsoft.com/zh-tw/library/system.text.stringbuilder.clear.aspx)
