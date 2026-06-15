---
title: "VC++ Region/EndRegion"
date: "2011-08-05 12:45:08"
description: "VC++ Region/EndRegion"
tags: [C++]
---

Visual Studio IDE提供Region功能能讓程式開發人員依自己的需求將程式碼片段分類整理，在C#與VB.NET中其關鍵字都是很簡單的#region，像是：

C#

```c
#region Region Name
... code ...
#endregion
```

VB.NET

```vb
#Region "Region Name"
    ... code ...
#End Region
```

在C++的開發環境中，Region的寫法就比較有些不同了，必須使用#paragma region去做。

```c
#pragma region Region Name
... code ...
#pragma endregion
```

這樣寫實際跑起來就會有Region的效果，可以看到下圖Region區塊的前方會有可以摺疊的區塊。

![image_thumb.png](/images/posts/32606/image_thumb.png)

## Link

* C/C++ Preprocessor Reference - region, endregion
