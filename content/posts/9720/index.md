---
title: "[C#]C# 4.0 Optional Parameters"
slug: "csharp-csharp-4-0-optional-parameters"
aliases: ["/posts/csharpc#-4.0-選擇性參數-optional-parameters/"]
date: "2009-07-29 09:04:42"
description: "Introduction 選擇性參數是C# 4.0的特色之一，可減少多載函式的建立，卻可達到相同的效果，加快使用者開發。 Support C# 4.0 or latter 使用方式 選擇性參數在使用上就跟C++一樣，只需用等號為函數的參數加上預設值即可。"
tags: [CSharp]
---

## ![image_thumb_12.png](/images/posts/9720/image_thumb_12.png)

## Introduction

選擇性參數是C# 4.0的特色之一，可減少多載函式的建立，卻可達到相同的效果，加快使用者開發。

## Support

* C# 4.0 or latter

## 使用方式

選擇性參數在使用上就跟C++一樣，只需用等號為函數的參數加上預設值即可。

範例程式碼片段如下：

![image_thumb_6.png](/images/posts/9720/image_thumb_6.png)

在使用具有選擇性參數的函式時，IDE所彈出的提示視窗在顯示上會用中括弧包住選擇性參數，用以告知該參數為選擇性參數，且會用等號指出當未明確帶入參數時其自動帶入的參數預設值為何。

![image_thumb_3.png](/images/posts/9720/image_thumb_3.png)

> 在VB.NET 8.0中其實也有提供對應的用法，使用上也大同小異，只要在參數後面帶入預設值，並在參數前面加入Optional關鍵字即可。

## 注意事項

**1.選擇性參數後不得存在必要性參數**

C# 4.0的選擇性參數在使用上跟其它語言一樣，除了給予預設值之外，還需注意選擇性參數要放在必要性參數的後面，也就是說選擇性參數後面不得有必要性參數的存在。

若是在選擇性參數後存在必要性參數的話

```csharp
public void SayHello(string name="無名氏",string msg)
```

在編譯時就會顯示 "Optional parameters must appear after all required parameters”錯誤。

![image_thumb_2.png](/images/posts/9720/image_thumb_2.png)

**2.了解多載函式的取用依據**

C# 4.0中的選擇性參數在使用上跟VB.NET有些不同。以VB.NET來說，當有選擇性參數的多載函式能涵蓋處理其它多載函式，或是說兩個多載函式的差異只在於選擇性參數時，Compile會提出警示，且不允許程式進行編譯。

簡單的範例程式碼片段如下：

```vb
Sub SayHello()
    Console.WriteLine("Hi~")
End Sub

Sub SayHello(Optional ByVal name As String = "無名氏")
    Console.WriteLine("Hello~My name is " & name)
End Sub
```

警示訊息如下：

![image_thumb.png](/images/posts/9720/image_thumb.png)

但同樣的程式在C# 4.0中卻是可以運行的。像是下面這段程式碼片段：

```csharp
static void Main(string[] args)
{
    SayHello();
    SayHello("Larry");
}
static void SayHello()
{
    Console.WriteLine("Hi~");
}
static void SayHello(String name = "無名氏")
{
    Console.WriteLine("Hello~My name is " + name);
}
```

不僅可以編譯成功，也可以執行。

![image_thumb_1.png](/images/posts/9720/image_thumb_1.png)

以這個例子來看，其實兩個多載函式都可以處理指定的函式呼叫。雖哪個函式被呼叫都不奇怪，但若不了解其規則仍會讓人造成混亂，因此我們必需要了解其多載函式的取用依據。

在多載函式的取用上，C#編譯器會自動幫我們判斷最適用的多載函式。其取用順序如下：

![image_thumb_8.png](/images/posts/9720/image_thumb_8.png)

不用轉型的函式優先取用

```csharp
static void Main(string[] args)
{
    SayHello("Larry");
}
static void SayHello(object name)
{
    Console.WriteLine("Hi~My name is" + name.ToString());
}

static void SayHello(String name = "無名氏")
{
    Console.WriteLine("Hello~My name is " + name);
}
```

![image_thumb_4.png](/images/posts/9720/image_thumb_4.png)

不用省略選擇性參數的函式優先取用

```csharp
static void Main(string[] args)
{
    SayHello();
}
static void SayHello()
{
    Console.WriteLine("Hi~");
}
static void SayHello(String name = "無名氏")
{
    Console.WriteLine("Hello~My name is " + name);
}
```

![image_thumb_7.png](/images/posts/9720/image_thumb_7.png)

## 範例程式

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace SayHello
{
    class Program
    {
        static void Main(string[] args)
        {
            SayHello();
            SayHello(name:"Larry");
            SayHello("Larry");
        }
        static void SayHello()
        {
            Console.WriteLine("Hi~");
        }
        static void SayHello(object name)
        {
            Console.WriteLine("Hi~My name is" + name.ToString());
        }
        static void SayHello(String name = "無名氏")
        {
            Console.WriteLine("Hello~My name is " + name);
        }
    }
}
```

執行結果

![image_thumb_10.png](/images/posts/9720/image_thumb_10.png)

## Video

下面列出一些網路上的示範影片，有興趣的可以順便看一下。

![video8a1f6f262cc1.jpg](/images/posts/9720/video8a1f6f262cc1.jpg)

![videoab99331e5866.jpg](/images/posts/9720/videoab99331e5866.jpg)

![video161ce344d569.jpg](/images/posts/9720/video161ce344d569.jpg)

![video0725efbcc95e.jpg](/images/posts/9720/video0725efbcc95e.jpg)

## Conclusion

選擇性參數雖然不是新的概念，但對於缺少該功能的C#而言，習慣VB.NET甚至是C++的程式員來說，寫起來總是會覺得不順，在多載函式的建立上也麻煩了許多。好在這個問題在C# 4.0中已獲得改善。

## Link

* C# 4.0 新特性：動態型別、選用參數、具名參數
* Inside C# 4.0: dynamic typing, optional parameters, covariance and contravariance
* C# 4.0 Optional Parameters
* C# 4.0 Named Parameters for better code quality
* New Features in C# 4.0
* C# 4.0's New Features Explained

![image_thumb_11.png](/images/posts/9720/image_thumb_11.png)
