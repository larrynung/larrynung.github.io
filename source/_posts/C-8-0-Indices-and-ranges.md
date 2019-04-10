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


完整的範例會像下面這樣：  

```C#
using System;
using System.Linq;

namespace Indices
{
    class Program
    {
        static void Main(string[] args)
        {
            var data = Enumerable.Range(1, 5).ToArray();

            //var firstData = data[0];
            //var secondData = data[1];
            //var lastData = data[^1];
            
            var firstData = data[Index.Start];
            var secondData = data[Index.FromStart(1)];
            //var secondData = data[new Index(1)];
            var lastData = data[Index.FromEnd(1)];
            //var secondData = data[new Index(1, true)];

            Console.WriteLine(firstData);
            Console.WriteLine(secondData);
            Console.WriteLine(lastData);
        }
    }
}
```

{% asset_img 1.png %}

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


完整的範例會像下面這樣：  

```C#
using System;
using System.Linq;

namespace Ranges
{
    class Program
    {
        static void Main(string[] args)
        {
            var data = Enumerable.Range(1, 5).ToArray();
            
            //var allData = data[..];
            //var firstTwoData = data[..2];
            //var lastTwoData = data[^2..];
            //var skipTwoData = data[2..];
            //var middleData = data[2..4];
            
            var allData = data[Range.All];
            var firstTwoData = data[new Range(Index.Start, Index.FromStart(2))];
            var lastTwoData = data[new Range(Index.FromEnd(2), Index.End)];
            var skipTwoData = data[new Range(Index.FromStart(2), Index.End)];
            var middleData = data[new Range(Index.FromStart(2), Index.FromStart(4))];

            Console.WriteLine(string.Join(",", allData));
            Console.WriteLine(string.Join(",", firstTwoData));
            Console.WriteLine(string.Join(",", lastTwoData));
            Console.WriteLine(string.Join(",", skipTwoData));
            Console.WriteLine(string.Join(",", middleData));
        }
    }
}
```

{% asset_img 2.png %}
