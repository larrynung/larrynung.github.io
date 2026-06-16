---
title: "[C#]RNGCryptoServiceProvider亂數產生器"
date: "2010-01-07 12:55:33"
description: "Assemble mscorlib (在 mscorlib.dll 中) Namespace System.Security.Cryptography RNGCryptoServiceProvider RNGCryptoServiceProvider類別是Thread Safe型別，"
tags: [CSharp]
---

## Assemble

mscorlib (在 mscorlib.dll 中)

## Namespace

System.Security.Cryptography

## RNGCryptoServiceProvider

RNGCryptoServiceProvider類別是Thread Safe型別，是使用由密碼編譯服務供應者 (CSP) 提供的實作 (implementation)，實作密碼編譯亂數產生器 (RNG)。它能產生較Random類別這種「有限性數學演算法」還亂的亂數。

在RNGCryptoServiceProvider的成員中，其主要方法有兩個 ：

<table border="1" cellpadding="2" cellspacing="0" width="601">
<tbody>
<tr>
<td valign="top" width="49">
<p>
					 </p>
</td>
<td valign="top" width="150">
<p>
					名稱</p>
</td>
<td valign="top" width="400">
<p>
					說明</p>
</td>
</tr>
<tr>
<td valign="top" width="49">
<p>
<img alt="Public method" src="/images/posts/12883/ctd75hw2.pubmethod%28zh-tw,VS.80%29.gif"/> <img alt="Supported by the .NET Compact Framework" src="/images/posts/12883/ctd75hw2.CFW%28zh-tw,VS.80%29.gif"/></p>
</td>
<td valign="top" width="150">
<p>
					GetBytes</p>
</td>
<td valign="top" width="400">
<p>
					覆寫。 在位元組陣列中填入在密碼編譯方面強式的隨機值序列。</p>
</td>
</tr>
<tr>
<td valign="top" width="49">
<p>
<img alt="Public method" src="/images/posts/12883/ctd75hw2.pubmethod%28zh-tw,VS.80%29.gif"/> <img alt="Supported by the .NET Compact Framework" src="/images/posts/12883/ctd75hw2.CFW%28zh-tw,VS.80%29.gif"/></p>
</td>
<td valign="top" width="150">
<p>
					GetNonZeroBytes</p>
</td>
<td valign="top" width="400">
<p>
					覆寫。 在位元組陣列中填入在密碼編譯方面強式的隨機非零值序列。</p>
</td>
</tr>
</tbody>
</table>

兩者的用法都是傳入一個Byte陣列，用法大同小異。主要只是差在GetNonZeroBytes所產的隨機值是不為零的而已。

使用步驟主要如下：

1. 建立RNGCryptoServiceProvider物件實體
2. 建立欲存放亂數的Byte陣列
3. 呼叫GetBytes或GetNonZeroBytes並帶入Byte陣列

![image_thumb.png](/images/posts/12883/image_thumb.png)

簡單的操作範例如下：

```csharp
static void Main(string[] args)
{
    RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider();
    byte[] random = new Byte[100];
    rng.GetBytes (random);
    foreach (byte b in random)
        Console.Write(b.ToString() + " ");
    Console.WriteLine();
}
```

運行結果如下：
![image_thumb_1.png](/images/posts/12883/image_thumb_1.png)

接著測試一下RNGCryptoServiceProvider是否會有跟Random類別一樣，當在極短時間內使用，會因亂數種子一樣而產生相同亂數組的問題。

```csharp
static void Main(string[] args)
{
    RNGCryptoServiceProvider rng1 = new RNGCryptoServiceProvider();
    RNGCryptoServiceProvider rng2 = new RNGCryptoServiceProvider();
    PrintRandomNumber(rng1);
    Console.WriteLine(new string('=',70));
    PrintRandomNumber(rng2);
}

static void PrintRandomNumber(RNGCryptoServiceProvider rng)
{
    byte[] random = new Byte[100];
    rng.GetBytes(random);
    foreach (byte b in random)
        Console.Write(b.ToString() + " ");
    Console.WriteLine();
}
```

測試結果如下：
![image_thumb_2.png](/images/posts/12883/image_thumb_2.png)

依測試結果，我們可以發現使用RNGCryptoServiceProvider，並不會有亂數種子的問題。

另外一提，為方便使用，好心的保哥已經幫我們整理好了簡單的靜態類別。使用上就跟使用Random類別類似。

```csharp
using System;
using System.Security.Cryptography;

/// <summary>
/// 使用 RNGCryptoServiceProvider 產生由密碼編譯服務供應者 (CSP) 提供的亂數產生器。
/// </summary>
public static class RNG
{
    private static RNGCryptoServiceProvider rngp = new RNGCryptoServiceProvider();
    private static byte[] rb = new byte[4];

    /// <summary>
    /// 產生一個非負數的亂數
    /// </summary>
    public static int Next()
    {
        rngp.GetBytes(rb);
        int value = BitConverter.ToInt32(rb, 0);
        if (value < 0) value = -value;
        return value;
    }
    /// <summary>
    /// 產生一個非負數且最大值 max 以下的亂數
    /// </summary>
    /// <param name="max">最大值</param>
    public static int Next(int max)
    {
        rngp.GetBytes(rb);
        int value = BitConverter.ToInt32(rb, 0);
        value = value % (max + 1);
        if (value < 0) value = -value;
        return value;
    }
    /// <summary>
    /// 產生一個非負數且最小值在 min 以上最大值在 max 以下的亂數
    /// </summary>
    /// <param name="min">最小值</param>
    /// <param name="max">最大值</param>
    public static int Next(int min, int max)
    {
        int value = Next(max - min) + min;
        return value;
    }
}
```

這邊我稍微整理了一下，把保哥的程式包成擴充方法：

```csharp
using System;
using System.Security.Cryptography;

/// <summary>
/// 使用 RNGCryptoServiceProvider 產生由密碼編譯服務供應者 (CSP) 提供的亂數產生器。
/// </summary>
public static class RNGCryptoServiceProviderExtensions
{
    private static byte[] rb = new byte[4];

    /// <summary>
    /// 產生一個非負數的亂數
    /// </summary>
    public static int Next(this RNGCryptoServiceProvider rngp)
    {
        rngp.GetBytes(rb);
        int value = BitConverter.ToInt32(rb, 0);
        return (value < 0)?-value:value;
    }
    /// <summary>
    /// 產生一個非負數且最大值 max 以下的亂數
    /// </summary>
    /// <param name="max">最大值</param>
    public static int Next(this RNGCryptoServiceProvider rngp,int max)
    {
        return Next(rngp) %  (max + 1);
    }
    /// <summary>
    /// 產生一個非負數且最小值在 min 以上最大值在 max 以下的亂數
    /// </summary>
    /// <param name="min">最小值</param>
    /// <param name="max">最大值</param>
    public static int Next(this RNGCryptoServiceProvider rngp,int min, int max)
    {
        return Next(rngp, max - min) + min;
    }
}
```

使用上就會像這樣

```csharp
RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider();
Console.WriteLine (rng.Next(10, 15));
```

## Link

* RNGCryptoServiceProvider 類別
* 亂數產生器：Random 與 RNGCryptoServiceProvider
* 生成安全的随机数
