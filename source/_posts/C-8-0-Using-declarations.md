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


值得注意的是這樣的寫法是方便了許多，也不需要額外的縮排，但是物件的生命週期會轉交給編譯器決定，釋放時機點可能會比較沒那麼恰當。

<br/>


像是上面的例子經由反組譯後可以看到其實 disposableClass.ToString() 後物件就沒使用了，但是編譯器目前無法偵測到這點並在適合的時機點立即做釋放。  

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


另外對於程式語法的誤用目前編譯器也無法偵測。  

<br/>


像是如果未注意到使用的是 Using declarations 語法，再次主動調用 Dispose 方法。  

```c#
...
using var obj = new DisposableClass();
...
obj.Dispose();
...
```

<br/>


像是下面這樣：

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
            obj.Dispose();
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

<br/>


運行後可以看到會忠實的進行兩次物件釋放動作。  

{% asset_img 4.png %}

<br/>


反組譯查看，也可以看到編譯器只是很單純的照著程式碼編譯。  

```C#
...
DisposableClass disposableClass = new DisposableClass();
try
{
    Console.WriteLine(disposableClass.ToString());
    disposableClass.Dispose();
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

{% asset_img 5.png %}

<br/>


所以如果語法糖可能會造成誤用的話，還是要自行斟酌使用。  

<br/>

Link
----
* [Using declarations in C# 8.0](https://gunnarpeipman.com/net/using-declarations/)
