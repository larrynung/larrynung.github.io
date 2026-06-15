---
title: ".NET 4.0 New Feature - Enum.HasFlag"
date: "2010-10-19 09:43:02"
description: ".NET 4.0 New Feature - Enum.HasFlag"
tags: [VB.NET]
---

在.NET 4.0以前，若有要判斷Flag屬性修飾過的列舉是否含有特定Flag時，我們會將列舉值與Flag去做And運算，判斷做完運算後的值是否等同Flag，像是下面這樣：

```vb
Dim hasFlag = (enumValue And flag)  =  flag
```

  在.NET 4.0後我們有另一個更輕鬆的選擇就是Enum.HasFlag，使用上直接帶入要判斷的Flag即可。

```vb
Dim hasFlag = enumValue.HasFlag(flag)
```

這邊來看個簡化過的MSDN使用範例來加深印象

```vb
<Flags> Public Enum DinnerItems As Integer
   None = 0
   Entree = 1
   Appetizer = 2
   Side = 4
   Dessert = 8
   Beverage = 16
   BarBeverage = 32
End Enum

...
   Dim myOrder As DinnerItems = DinnerItems.Appetizer Or DinnerItems.Entree Or
                                DinnerItems.Beverage Or DinnerItems.Dessert
   Dim hasFlag As Boolean = myOrder.HasFlag(DinnerItems.Entree Or DinnerItems.Beverage)
...
```

需特別注意的是當帶入的flag 其對應值是零時，則方法會傳回 true，在設計列舉時需加留意，不要把不是代表空值的列舉值設為0。

.NET 4.0加入的Enum.HasFlag是個簡單好用的小方法，在拿列舉做些像是Enum 的設計與應用 - 簡易權限設計這篇介紹到的權限控管，或是拿來做一些狀態上的判斷時，使用Enum.HasFlag來替換傳統的處理方法會更為方便。

## Link

* Enum.HasFlag 方法
* Enum 的設計與應用 - 簡易權限設計
