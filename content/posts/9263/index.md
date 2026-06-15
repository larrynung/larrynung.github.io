---
title: "[C#]Effective C# 條款二： 運行時常數優於編譯時常數"
slug: "[CSharp]Effective C# 條款二： 運行時常數優於編譯時常數"
date: "2009-07-09 08:46:16"
description: "[C#]Effective C# 條款二： 運行時常數優於編譯時常數"
tags: [CSharp]
---

![image_thumb_3.png](/images/posts/9263/image_thumb_3.png)

.NET中有兩種不同的常數機制：一種是編譯時(Compile-Time)常數，一種是運行時(Runtime)常數。

## 編譯時常數

編譯時常數是透過Const關鍵字宣告的變數，像是如下宣告：

```
public const int BUFFER_SIZE = 512;
```

編譯時常數故名思義就是編譯時就已被處理的常數，在編譯後會被編譯器替換成該常數值，假設有段程式如下：

```
class Program
{
    public const int BUFFER_SIZE = 512;
    static void Main(string[] args)
    {
        byte[] bytes = new byte[BUFFER_SIZE];
    }
}
```

在編譯後，我們可以透過Reflector工具反組譯查看，此時本來使用編譯時常數的地方會被編譯器替換成該變數的值。

![image_thumb.png](/images/posts/9263/image_thumb.png)

編譯時常數雖然在效能方面會比運行時常數好，但在使用彈性上卻不如運行時常數。不僅只能宣告基本型別、列舉型別、與字串型別，別的組件參考使用的話，編譯時變數值也會被編譯器給替換掉。因此若要修改該常數值，除了本身的組件外，也必需將所有參考到的組件都給重新編譯。

## 運行時常數

運行時常數是透過readonly關鍵字聲明的變數，像是如下宣告：

```
public static readonly int BUFFER_SIZE = 512;
```

運行時常數故名思義就是在運行中才可使用的常數，該常數值在運行時才會被計算，編譯後並不會被編譯器替換常數值，因此在使用上彈性優於編譯時常數。若要修改常數的值，所有參考使用的組件都不需配合重新編譯。也不像編譯時常數一樣有型別上的限制。
