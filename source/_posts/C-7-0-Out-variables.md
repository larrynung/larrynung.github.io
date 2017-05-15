---
title: 'C# 7.0 - Out variables'
date: 2017-03-28 13:41:37
tags: [CSharp 7.0]
---

C# 7.0 以前使用的方法若有 Out 參數，需要事先宣告才能帶入使用。  

<!-- More -->

```C#
...
string data;
GetData(out data);
...

static void GetData(out string data)
{
    ...
}
```

<br/>


C# 7.0 以後，可以在帶入 Out 參數時直接順帶宣告。  

```C#
...
GetData(out string data);
...
```

<br/>


也可以結合使用區域型別推斷。  

```C#
...
GetData(out var data);
...
```

<br/>


完整的範例程式如下：  

```C#
using System;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            GetData(out string data);
            //GetData(out var data);
            Console.WriteLine($"{data}");
        }

        static void GetData(out string data)
        {
            data = "Level Up (http://larrynung.github.io/)";
        }
    }
}
```

<br/>


運行結果如下：  

{% asset_img 1.png %}

<br/>


反組譯查看一下，這功能也只是在編譯時幫我們做掉了參數宣告的動作。  

{% asset_img 2.png %}

<br/>