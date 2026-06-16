---
title: "[C#]Point 與 Pixel 單位的互換"
slug: "[CSharp]Point 與 Pixel 單位的互換"
date: "2013-11-06 12:00:00"
description: "最近在跟UI Team合作時碰到一些問題，UI Team畫給我的UI圖中會明確標示元件的位置與要使用的字型，但是UI Team那邊在看的是Pixel，而我這邊看的是Point，當UI Team標明一個元件它裡面要顯示的是字型大小是14 Pixel時，我當下突然不知道該如何下手。"
---

最近在跟UI Team合作時碰到一些問題，UI Team畫給我的UI圖中會明確標示元件的位置與要使用的字型，但是UI Team那邊在看的是Pixel，而我這邊看的是Point，當UI Team標明一個元件它裡面要顯示的是字型大小是14 Pixel時，我當下突然不知道該如何下手。看了一下相關的網路文章，大致才了解了其中的轉換，這邊簡單的將之整理紀錄一下。

因為每英吋有72個Point，且在Windows下預設是96 dpi，所以1 in = 72 pt = 96 ppi，故當我們要將Pixel轉換為Point時，可以透過下面公式來做轉換：

```xml
point = pixel * 72 / 96
```

若要將point轉換為pixel，則可套用下面公式：

```xml
pixels = point * 96 / 72
```

若是在Mac的電腦上，預設是72 dpi，上面公式中的96就必須用72下去替換。當然這邊提到的DPI都只是預設狀態，若只是要抓個大概時可以直接拿來套用，但若要精準的轉換則還是要拿實際的解析度下去處理。

```vb
point = pixel * 72 / dpi
pixel = point * dpi /72
```

實際用程式來做轉換時，可直接用Graphics.DpiX帶入去做運算。

```xml
using (var g = this.CreateGraphics())
{
	points = pixels * 72 / g.DpiX;
	pixels = points * g.DpiX / 72
}
```

## Link

* Approximate Conversion from Points to Pixels
* c# - Convert Pixels to Points - Stack Overflow
* POINT TO PIXEL CONVERSION
* Point vs Pixel. What is the difference?
* About Points and Pixels as Units
* HowtoCustomFontswithFontconfig
* 請教各位高手幾個有關像素和解析度的問題
* 知識百科：中文字號、磅和像素對照關係
