---
title: "[C#][VB.NET]使用Nothing或Null作數值運算"
slug: "csharp-vbnet-使用nothing或null作數值運算"
aliases: ["/posts/csharpvb.net使用nothing或null作數值運算/"]
date: "2009-08-13 09:02:18"
description: "今天突然發現VB.NET的Nothing可以拿來作運算，因此作了一點小實驗。意外發現VB.NET與C#在相同的程式邏輯下會跑出不一樣的結果。 以VB.NET來說，"
tags: [VB.NET, CSharp]
---

今天突然發現VB.NET的Nothing可以拿來作運算，因此作了一點小實驗。意外發現VB.NET與C#在相同的程式邏輯下會跑出不一樣的結果。

以VB.NET來說，假設我們拿Nothing來跟數值作運算

```vb
Console.WriteLine(0 + Nothing)
Console.WriteLine(0 - Nothing)
Console.WriteLine(1 * Nothing)
Console.WriteLine(1 / Nothing)
Console.WriteLine(2 ^ Nothing)
```

則我們會得到像下面的執行結果

![image_thumb.png](/images/posts/10028/image_thumb.png)

可以發現Nothing在VB.NET中作數值運算時會先被轉換成0後再來處理。讓我們來確認一下

```vb
Console.WriteLine(0 = Nothing)
Console.WriteLine(1 = Nothing)
```

結果發現Nothing真的被當作0來處理

![image1_thumb.png](/images/posts/10028/image1_thumb.png)

再來看一下C#程式

```csharp
Console.WriteLine(0 + null);
Console.WriteLine(0 - null);
Console.WriteLine(1 * null);
Console.WriteLine(1 / null);
Console.WriteLine(2 ^ null);
```

執行後會得到像下面這樣

![image_thumb.png](/images/posts/10028/image_thumb.png)

完全看不到任何東西，猜測應該是運算後被變成null了。做個簡單的實驗看看就知道了

```csharp
Console.WriteLine((0 + null) == null);
```

運行後可以證明真的被轉為null了

![image15_thumb.png](/images/posts/10028/image15_thumb.png)
