---
title: 'C# 8.0 - Indices and ranges'
date: 2019-04-09 14:35:06
tags: [CSharp 8.0]
---

C# 8.0 提供了 Index 與 Range。  

<!-- More -->

<br/>


要取得陣列指定位置的元素本來需要帶入 int 型態的索引位置到索引子，現在可改帶入 Index，Index 的數值表示寫法跟一般的整數數值類似，只是從尾部倒過來的索引可直接在前面加上 ^ 符號表示，像是最後一筆資料的索引位置可用 ^1 表示，比起以前自己要用陣列長度推算方便了許多。  

```C#
...
var lastData = data[^1];
...
```

<br/>


除了上面類似數值的表示方式外，也可以直接使用 Index 類別來撰寫。  

```C#
...
var firstData = data[Index.Start];
var secondData = data[Index.FromStart(1)];
//var secondData = data[new Index(1)];
var lastData = data[Index.FromEnd(1)];
//var secondData = data[new Index(1, true)];
...
```

<br/>


若是要取得陣列的部分內容，可搭配 Range 使用，用 .. 串接起始與中止索引，指定索引的範圍。  

```C#
...
var allData = data[..];
var firstTwoData = data[..2];
var lastTwoData = data[^2..];
var skipTwoData = data[2..];
var middleData = data[2..4];
...
```
 
<br/>


這邊一樣可以直接使用 Range 類別來撰寫。

```C#
...
var allData = data[Range.All];
var firstTwoData = data[new Range(Index.Start, Index.FromStart(2))];
var lastTwoData = data[new Range(Index.FromEnd(2), Index.End)];
var skipTwoData = data[new Range(Index.FromStart(2), Index.End)];
var middleData = data[new Range(Index.FromStart(2), Index.FromStart(4))];
...
```

<br/>


最後看一下完整的測試範例：  

```C#
using System;
using System.Linq;

namespace IndicesAndRanges
{
    class Program
    {
        static void Main(string[] args)
        {
            var data = Enumerable.Range(1, 5).ToArray();
            Index n = 2;
            
            Console.Write("Display {0}st data: ", n.Value);
            Console.WriteLine(data[n]);
            
            Console.Write("Display last data: ");
            Console.WriteLine(data[^1]);

            Console.Write("Display all data: ");
            Console.WriteLine(string.Join(",", data[..]));
            
            Console.Write("Display first {0} data: ", n.Value);
            Console.WriteLine(string.Join(",", data[..n]));
            //Console.WriteLine(string.Join(",", data[..2]));
            
            Console.Write("Skip first {0} data: ", n.Value);
            Console.WriteLine(string.Join(",", data[n..]));
            //Console.WriteLine(string.Join(",", data[2..]));
            
            Console.Write("Display last {0} data: ", n.Value);
            n = new Index(n.Value, true);
            Console.WriteLine(string.Join(",", data[n..]));
            //Console.WriteLine(string.Join(",", data[^2..]));
        }
    }
}
```

{% asset_img 1.png %}
