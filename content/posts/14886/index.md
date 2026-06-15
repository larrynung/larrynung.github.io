---
title: "[VB.NET]Keys lt;=gt; Char"
date: "2010-04-27 11:46:52"
description: "[VB.NET]Keys <=> Char"
tags: [VB.NET]
---

今天在撰寫控制項的KeyPress事件，由於事件的參數無法點出Keys直接比對，做了一些轉換動作，這邊紀錄一下：

要把Keys轉換成Char，可以使用Convert.ToChar

```vb
Dim keyChar As Char = Convert.ToChar(key)
```

或是ChrW函式

```vb
Dim keyChar As Char = Microsoft.VisualBasic.ChrW(key)
```

而要把Char轉成Keys則可以使用Asc函式

```vb
Dim key As Keys = Asc(keyChar)
```

簡易範例如下

```vb
Imports System.Windows.Forms

Module Module1

    Sub Main()
        Dim key As Keys = Keys.A
        Dim keyChar As Char = Convert.ToChar(key)

        Console.WriteLine(Convert.ToChar(key))
        Console.WriteLine(Asc(keyChar))
        Console.WriteLine(Microsoft.VisualBasic.ChrW(key))
    End Sub

End Module
```
