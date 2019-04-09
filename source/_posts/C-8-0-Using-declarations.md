---
title: 'C# 8.0 - Using declarations'
date: 2019-04-08 15:46:12
tags: [CSharp 8.0]
---

C# 8.0 以前使用 using 釋放物件，會在 using 後用小刮號包住要釋放的物件，然後在下面用大括號指示物件的生命週期範圍。   

<!-- More -->

```C#
...
using(var obj = new DisposableClass())
{
    ...
}
...
```

<br/>


程式寫起來會像下面這樣:  

```C#
using System;

namespace UsingDeclarations
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var obj = new DisposableClass())
            {
                Console.WriteLine(obj.ToString());
            }
        }
    }

    class DisposableClass : IDisposable
    {
        public void Dispose()
        {
            Console.WriteLine("Dispose...");
        }
    }
}
```

{% asset_img 1.png %}

<br/>


C# 8.0 後支援 Using declarations，可以直接在變數宣告前面加掛 using 關鍵字，一樣可以達到物件釋放的效果。  

```C#
...
using var obj = new DisposableClass();
...
```

<br/>


程式寫起來會像下面這樣:  

```C#
using System;

namespace UsingDeclarations
{
    class Program
    {
        static void Main(string[] args)
        {
            using var obj = new DisposableClass();
            Console.WriteLine(obj.ToString());

            Console.WriteLine("Hello World");
        }
    }

    class DisposableClass : IDisposable
    {
        public void Dispose()
        {
            Console.WriteLine("Dispose...");
        }
    }
}
```

{% asset_img 2.png %}

<br/>


該語法是利用編譯器做成的語法糖，程式在編譯時編譯器會將 Using declarations 的語法編譯成 try/finally 區塊，在 finally 區塊中調用 Dispose 方法做釋放的動作。  

<br/>


值得注意的是這樣的寫法是方便了許多，也不需要額外的縮排，但是物件的生命週期會轉交給編譯器決定，釋放時機點可能會比較沒那麼恰當，已經沒在使用的物件了會無法立即釋放。  

```C#
...
        DisposableClass disposableClass = new DisposableClass();
        try
        {
            Console.WriteLine(disposableClass.ToString());
            Console.WriteLine("Hello World");
        }
        finally
        {
            if (disposableClass != null)
            {
                ((IDisposable)disposableClass).Dispose();
            }
        }
...
```

{% asset_img 3.png %}

<br/>


對於程式語法的誤用目前也無法偵測。  

```c#
...
using var obj = new DisposableClass();
...
obj.Dispose();
...
```

<br/>


Link
----
* [Using declarations in C# 8.0](https://gunnarpeipman.com/net/using-declarations/)
