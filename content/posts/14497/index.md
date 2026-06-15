---
title: "[VB.NET]VB 10.0 Implied Line Continuation"
date: "2010-04-10 01:53:41"
description: "[VB.NET]VB 10.0 Implied Line Continuation"
tags: [VB.NET]
---

VB.NET是line-oriented語言，與C#不同的是，在撰寫VB.NET時，不需使用像是";"的終止符號。撰寫的指令幾乎都是一行寫完，若要換行，可使用串接字元「_」，明確告知系統程式碼有斷行。

![image_thumb_4.png](/images/posts/14497/image_thumb_4.png)

但當程式一多，串接字串這樣加上去，整個程式就變得很亂，若未加上串接字元，編譯器又會偵測到錯誤，儘管該程式不會讓編譯器造成混淆，仍舊強制要加上串接字元。

![image_thumb_3.png](/images/posts/14497/image_thumb_3.png)

在VB.NET 10.0中，在某些條件下，串接字元可以忽略不寫。像是下面這樣：

![image_thumb_5.png](/images/posts/14497/image_thumb_5.png)

但若會是斷行的方式會讓編譯器造成混淆，則仍舊需要使用串接字元，不然編譯器將會告知錯誤。

像是下面這段程式在From關鍵字之前就斷行，就會讓編譯器以為第一行程式是宣告集合物件，而第二行是呼叫From函式。

```vb
Dim list As New List(Of Integer)
From{1, 2, 3, 4, 5}
```

又或著像下面這樣，造成編譯器無法判斷End與Sub是函式、End Sub、或是新的Sub副程式。

```vb
Sub Main()
End
Sub
```

更多更詳細的例子可參閱Implicit Line Continuation in VB 10 (Tyler Whitney)。

## Link

* Implicit Line Continuation in VB 10 (Tyler Whitney)
