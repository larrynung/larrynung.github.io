---
title: 'C# 8.0 - Using declarations'
date: 2019-04-08 15:46:12
tags: [CSharp 8.0]
---

C# 8.0 以前使用 using 釋放物件，會像下面這樣撰寫。  

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


C# 8.0 支援 Using declarations，可以直接在變數宣告前面加掛 using，物件就會在用完後被釋放。  

```C#
...
using var obj = new DisposableClass();
...
```

<br/>


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


編譯器會將 Using declarations 的語法編譯成 try/finally 區塊，在 finally 區塊中調用 Dispose 方法做釋放的動作，執得注意的是這樣的寫法是方便了許多，也不需要額外的縮排，但是物件的釋放時機點可能會比較沒那麼恰當，像是已經沒在使用該物件了卻沒立即釋放。  

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


Link
----
* [Using declarations in C# 8.0](https://gunnarpeipman.com/net/using-declarations/)
