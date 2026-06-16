---
title: "[Performance][C#]同時判斷多個字串是否為數值型態"
date: "2009-12-20 08:08:45"
description: "一般來說，在C#中若我們想要判斷字串是否為數值形式。多半我們會利用TryParse、正規表示式這兩種方式來做處理。相關的文章在網路上已經很多了，像是TryParse的方法就可以參閱HOW TO：判斷字串是否表示數值 (C# 程式設計手冊)這篇MSDN文章。"
tags: [CSharp,Performance]
---

一般來說，在C#中若我們想要判斷字串是否為數值形式。多半我們會利用TryParse、正規表示式這兩種方式來做處理。相關的文章在網路上已經很多了，像是TryParse的方法就可以參閱HOW TO：判斷字串是否表示數值 (C# 程式設計手冊)這篇MSDN文章。

這邊摘錄MSDN的範例，簡單的帶過：

```csharp
int i = 0;
string s = "108";
bool result = int.TryParse(s, out i); //i now = 108
```

以上就是判斷字串是否為數值的程式寫法，相信這個簡單的程式大家應該都會寫，這邊就不再深入探討。今天要談的重點是當今天碰到要判斷很多字串是否都為數值時，您會怎摸樣去做？

這邊我大概的提出了幾個我能想到的作法，再對其效能做些比較。

## 方法一

應該是大家最常用的方法，分別判斷所有的字串是否為數值。

```csharp
static Boolean IsNumeric1(string[] values)
{
    int tempValue;
    foreach (string value in values)
    {
        if (!int.TryParse(value, out tempValue))
            return false;
    }
    return true;
}
```

## 方法二

主要是把所有字串先合併成一個字串，再用TryParse作數值判斷的動作。(這個方法需特別注意的是，此種合併的作法可能會讓數值溢位。)

**方法二之一**

不處理負數的情況

```csharp
static Boolean IsNumeric2_1(string[] values)
{
    int tempValue;
    return int.TryParse(string.Join(string.Empty, values), out tempValue);
}
```

**方法二之二**

處理負數的情況

```csharp
static Boolean IsNumeric2_2(string[] values)
{
    int tempValue;
    int idx = 0;
    foreach (string value in values)
    {
        values[idx] = value.TrimStart('-');
    }
    return int.TryParse(string.Join(string.Empty, values), out tempValue);
}
```

## 方法三

用正規表示式分別判斷其是否為數值。

```csharp
static Boolean IsNumeric3(string[] values)
{
    foreach (string value in values)
    {
        if (!Regex.IsMatch(value,@"\d+"))
            return false;
    }
    return true;
}
```

## 方法四

把所有字串先合併成一個字串，再用正規表示式作數值判斷的動作。

```csharp
static Boolean IsNumeric4(string[] values)
{
    return Regex.IsMatch(string.Join(string.Empty, values), @"\d+");
}
```

## 效能比較

測試程式如下：

```csharp
static void Main(string[] args)
{
    //String[] values = InitTestStrings(1);
    String[] values = InitTestStrings(10);
    //String[] values = InitTestStrings(10,1);
    //String[] values = InitTestStrings(10, 2);
    //String[] values = InitTestStrings(10, 3);
    int testCount = 1000000;
    Stopwatch sw = Stopwatch.StartNew();
    for (int idx = 0; idx < testCount; ++idx)
    {
        IsNumeric1(values);
    }
    sw.Stop();
    Console.WriteLine("Method1: " + sw.ElapsedMilliseconds + " ms");

    sw.Reset();
    sw.Start();
    for (int idx = 0; idx < testCount; ++idx)
    {
        IsNumeric2_1(values);
    }
    sw.Stop();
    Console.WriteLine("Method2-1: " + sw.ElapsedMilliseconds + " ms");

    sw.Reset();
    sw.Start();
    for (int idx = 0; idx < testCount; ++idx)
    {
        IsNumeric2_2(values);
    }
    sw.Stop();
    Console.WriteLine("Method2-2: " + sw.ElapsedMilliseconds + " ms");

    sw.Reset();
    sw.Start();
    for (int idx = 0; idx < testCount; ++idx)
    {
        IsNumeric3(values);
    }
    sw.Stop();
    Console.WriteLine("Method3: " + sw.ElapsedMilliseconds + " ms");

    sw.Reset();
    sw.Start();
    for (int idx = 0; idx < testCount; ++idx)
    {
        IsNumeric4(values);
    }
    sw.Stop();
    Console.WriteLine("Method4: " + sw.ElapsedMilliseconds + " ms");
}

static string[] InitTestStrings(int count)
{
    string[] testStrings = new string[count];
    for (int idx = 0; idx < count; ++idx)
    {
        testStrings[idx] = idx.ToString();
    }
    return testStrings;
}

static string[] InitTestStrings(int count,int nonValueIndex)
{
    string[] testStrings = InitTestStrings(count);
    testStrings[nonValueIndex] = "Test";
    return testStrings;
}
```

帶入以下測試條件 ：

```csharp
String[] values = InitTestStrings(1);
```

其運行結果如下：

![image_thumb_2.png](/images/posts/12568/image_thumb_2.png)

帶入以下測試條件 ：

```csharp
String[] values = InitTestStrings(10);
```

其運行結果如下：

![image_thumb_3.png](/images/posts/12568/image_thumb_3.png)

帶入以下測試條件 ：

```csharp
String[] values = InitTestStrings(10,1);
```

其運行結果如下：

![image_thumb_4.png](/images/posts/12568/image_thumb_4.png)

帶入以下測試條件 ：

```csharp
String[] values = InitTestStrings(10, 2);
```

其運行結果如下：

![image_thumb_5.png](/images/posts/12568/image_thumb_5.png)

帶入以下測試條件 ：

```csharp
String[] values = InitTestStrings(10, 3);
```

其運行結果如下：

![image_thumb_6.png](/images/posts/12568/image_thumb_6.png)

帶入以下測試條件 ：

```csharp
String[] values = InitTestStrings(10, 4);
```

其運行結果如下：

![image_thumb.png](/images/posts/12568/image_thumb.png)

由以上實驗，我們可以看見的是，在某些條件下，方法二這種先合併字串，再用TryParse的方式效能最佳。某些條件下，先合併字串在集中判斷可以獲得較好的效能。主要取決於字串合併數量的多寡、與第幾個字串不為數值這兩個條件。

實驗下來我們也可以發現，字串處理的OverHead好像比數值判斷來得低很多。因此使用字串合併後再判斷約有7/10的機率可獲取較高的效，另外適時的使用功能不那摸強大的判斷方式，也可以適當的提升效能，而使用正規表示式的方式則是效能最差的判斷方式。

另外一提，有興趣的可以試者把Int.TryParse改為Decimal.TryParse看看，其對效能也有相當的影響，所以依需求用對適當的型別來處理也是很重要的。

## Link

* Int32.TryParse 方法
* HOW TO：判斷字串是否表示數值 (C# 程式設計手冊)
