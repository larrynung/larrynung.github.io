---
title: ".NET 4.0 New Feature - BigInteger"
date: "2010-10-27 09:49:40"
description: ".NET 4.0 New Feature - BigInteger"
tags: [VB.NET]
---

先前在[C#]BigInteger這篇介紹過在3.5的Framework中，內藏有BigInteger型別可以使用，但在3.5中由於並未開出，所以得透過反射的方式把藏在內部的型別拿來使用，而在.NET 4.0推出後，我們不需兜一大圈就可以直接使用這樣的型別。

BigInteger為無上下限的任意整數 ，其可容納的值無限制，理論上只要記憶體能夠負荷，BigInteger想設定多大就可多大。

使用上需先加入參考System.Numerics.dll，並匯入System.Numerics命名空間。

![image_thumb.png](/images/posts/18628/image_thumb.png)

加入了參考與命名空間後，我們就可以開始來使用BigInteger型別了。首先，我們必需建立BigInteger型別變數。

BigInteger型別變數有兩種建立方式，一種是透過BigInteger的建構子將數值帶入使用。

```vb
Dim bigInt As New BigInteger(Long.MaxValue)
```

一種則是先宣告出BigInteger變數，在將值塞入後使用。

```vb
Dim bigInt As BigInteger
bigInt = Long.MaxValue
```

跟其它數值型別一樣，BigInteger型別具有加、減、乘、除...等基本的數學運算、數值比較、位元運算等能力。除此之外，BigInteger型別還具有許多其它數值型別所沒有的功能，像是取得兩個BigInteger的最小公因數、取Log、取餘數等等，功能十分的豐富，這邊就不一一列出了，有興趣可自行參閱BigInteger 成員。

另外在使用BigInteger型別時，我們必需注意到BigInteger型別是一種不變的型別，這邊來看一下MSDN的範例：

```vb
Dim number As BigInteger = BigInteger.Multiply(Int64.MaxValue, 3)
number += 1
Console.WriteLine(number)
```

由範例看來感覺很像BigInteger型別可以修改現有物件的值，但其實它在內部的運作跟String這種常數類別有點類似，是透過建立新的物件的方式去做的，因此在頻繁的操作下會有與String發生類似的效能問題。這邊一樣來看一下MSDN的範例：

```vb
Dim number As BigInteger = Int64.MaxValue ^ 5
Dim repetitions As Integer = 1000000
Dim sw As Stopwatch = Stopwatch.StartNew
' Perform some repetitive operation 1 million times.
For ctr As Integer = 0 To repetitions
    ' The following code executes if the operation succeeds.
    number += 1
Next
Console.WriteLine(sw.ElapsedMilliseconds)
```

像這樣的程式頻繁的在迴圈內對BigInteger做運算，花費時間約149ms。

![image_thumb_1.png](/images/posts/18628/image_thumb_1.png)

若我們將上述範例改用中繼變數去做運算，最後再回存回BigInteger：

```vb
Dim number As BigInteger = Int64.MaxValue ^ 5
Dim repetitions As Integer = 1000000
Dim actualRepetitions As Integer = 0
Dim sw As Stopwatch = Stopwatch.StartNew
' Perform some repetitive operation 1 million times.
For ctr As Integer = 0 To repetitions
    ' The following code executes if the operation succeeds.
    actualRepetitions += 1
Next
number += actualRepetitions
Console.WriteLine(sw.ElapsedMilliseconds)
```

  時間上的耗費就會降至2ms

![image_thumb_2.png](/images/posts/18628/image_thumb_2.png)

## Link

* BigInteger 結構
* BigInteger 成員
* [C#]BigInteger
