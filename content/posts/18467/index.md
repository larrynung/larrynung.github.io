---
title: ".NET 4.0 New Feature - Enum.TryParse"
date: "2010-10-20 12:57:39"
description: ".NET 4.0 New Feature - Enum.TryParse"
tags: [VB.NET]
---

.NET 4.0加入的Enum.TryParse跟Enum.Parse同樣都是用來轉換資料回列舉型別用的方法，相較於Enum.Parse，Enum.TryParse方法少觸發了無法轉換時的例外，因此可以減去省去不必要的例外處理，跟一般其它類別的TryParse一樣，可直接透過方法的回傳值判別是否成功轉換。

Enum.TryParse具有兩個多載方法，兩個多載方法的差異只在於在轉換列舉型別物件時是否會依照大小寫的不同下去處理。

![image_thumb.png](/images/posts/18467/image_thumb.png)

在使用Enum.TryParse轉換時，可以帶入的參數有列舉型別成員之基礎值或具名常數，或以逗號 (,) 分隔之具名常數清單的字串表示或基礎值清單。這邊在MSDN上的描述比起Enum.Parse多出了基礎值清單，看起來應該是可把列舉值用逗號串起去轉換，但這邊我試不出這樣的效果。而其它的轉換都跟Enum.Parse帶入的資料是一樣的，同樣以下面這個列舉為例來看一下使用方式。

```vb
<Flags()> _
Enum Colors As Integer
        None = 0
        Red = 1
        Green = 2
        Blue = 4
End Enum
```

我們可以像下面這般將數值轉換回列舉

```vb
Dim value As String = "1"
Dim colorValue As Colors
Dim pf As Boolean
pf = [Enum].TryParse(Of Colors)(value, colorValue)
```

把列舉型別常數名稱轉回列舉

```vb
Dim value As String = "Red"
Dim colorValue As Colors
Dim pf As Boolean
pf = [Enum].TryParse(Of Colors)(value, colorValue)
```

或是透過逗號串起的列舉型別常數名稱轉回列舉

```vb
Dim value As String = String.Join(",", New Object() {"None", "Red", "Green"})
Dim colorValue As Colors
Dim pf As Boolean
pf = [Enum].TryParse(Of Colors)(value, colorValue)
```

## Link

* Enum.TryParse 方法
