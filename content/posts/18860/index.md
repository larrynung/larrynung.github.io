---
title: ".NET 4.0 New Feature - Generic Lazy class"
date: "2010-11-07 11:39:14"
description: ".NET 4.0新增一泛型Lazy類型，可用以延遲物件初始化設定，透過Lazy類型的建構子我們可將要延遲初始化的物件類型與其初始化動作傳入，第一次存取Lazy.Value屬性或是呼叫Lazy.ToString方法時，該類型就會幫我們執行對應的初始化動作，後續再去存取就會直接取得結果，"
tags: [CSharp]
---

.NET 4.0新增一泛型Lazy類型，可用以延遲物件初始化設定，透過Lazy類型的建構子我們可將要延遲初始化的物件類型與其初始化動作傳入，第一次存取Lazy.Value屬性或是呼叫Lazy.ToString方法時，該類型就會幫我們執行對應的初始化動作，後續再去存取就會直接取得結果，而不會再去做初始化的動作。透過這樣的Lazy類型我們可以很輕鬆的延遲物件初始化設定，可以分散物件初始化的時間點、與避免不必要的初始化動作，我們不再需要使用以往的方法自行為物件成員加上延遲初始化的機制，也不需要在程式中加入額外的變數與Flag來做這樣的機制,在會耗用大量資源的物件上相當的好用。

Lazy類型在實作上其概念大概如Lazy Computation in C#這篇文章所提，會在建構時傳入初始化函式的指標並設定給內部成員變數，當呼叫Value屬性時會依內部成員變數去判別是否已經做過初始化的動作，若已初始化則傳回當初初始完後的值，若未出始化則初始化後再將其值設定給內部成員變數後回傳，當然這只是概念上的示意，實際底層的運作會比這個來的複雜許多。

```csharp
using System.Linq;
public class Lazy<T> {
  private Func<T> func;
  private T result;
  private bool hasValue;
  public Lazy(Func<T> func) {
    this.func = func;
    this.hasValue = false;
  }
  public T Value {
    get {
      if (!this.hasValue) {
        this.result = this.func();
        this.hasValue = true;
      }
      return this.result;
    }
  }
}
```

知道了實作原理後，接著來看一下如何使用，Lazy類型並未含有太多複雜的成員，只有兩個重要的屬性IsVauleCreated與Value。IsValueCreated屬性可用以判別是否有已經運行過初始化的動作，而Value則是會初始化物件或是直接將初始化後的值傳出。

![image_thumb.png](/images/posts/18860/image_thumb.png)

這邊來看一個簡單的使用範例：

```csharp
using System;
using System.Diagnostics;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            Lazy<Boolean> lazy = new Lazy<Boolean>(() =>
            {
                Console.WriteLine("Initializing...");
                System.Threading.Thread.Sleep(10000);
                Console.WriteLine("Initialized...");
                return true;
            });

            Console.WriteLine("IsValueCreated = {0}", lazy.IsValueCreated);
            Stopwatch sw = Stopwatch.StartNew();
            Console.WriteLine("result = {0}", lazy.Value);
            //Console.WriteLine("result = {0}", lazy.ToString());
            Console.WriteLine("Elapsed Time = {0} ms", sw.ElapsedMilliseconds);

            Console.WriteLine(new string('=', 50));
            Console.WriteLine("IsValueCreated = {0}", lazy.IsValueCreated);
            sw.Restart();
            Console.WriteLine("result = {0}", lazy.Value);
            //Console.WriteLine("result = {0}", lazy.ToString());
            Console.WriteLine("Elapsed Time = {0} ms", sw.ElapsedMilliseconds);
        }
    }
}
```

運行後我們可看到下面這樣的運行結果，可以看到只有第一次運行時會做初始化的動作，會耗費比較多的時間，後續再運行

就直接回傳初始化後的結果，因此會比較快速。

![image_thumb.png](/images/posts/18860/image_thumb.png)

也可以搭配變數初始器使用，同時取得變數初始器與Lazy initialization的優點：

```csharp
class Person
    {
        Lazy<int[]> _stocks = new Lazy<int[]>(
            () =>
            {
                //Initializing...
                return new int[] { 2002, 2360, 0050 };
            }
            );

        public int[] Stocks { get { return _stocks.Value; } }
    }
    ...
    static void Main(string[] args)
    {
        Person p = new Person();
        System.Console.WriteLine(string.Join(",", p.Stocks.Select((value) => { return value.ToString(); })));
    }
```

運行結果如下：

![image_thumb_1.png](/images/posts/18860/image_thumb_1.png)

需特別注意Lazy類型是用來作初始化動作的，故其被定位為初始後就不得清除變更，初始化後的值會被快取，在使用上若某些方法可能會每次呼叫傳出不同值的話並不適用於Lazy類型。另外該篇只是做個初淺的整理介紹，建議還是要參閱Lazy Computation in C#這篇文章以獲取較為清楚的概念，尤其是下方最後一個範例。

## Link

* Lazy(Of T) 類別
* Lazy(Of T) 成員
* Lazy initialization in .NET 4 – Lazy<T>
* Lazy Computation in C#
* .Net Framework 4.0: Using System.Lazy<T>
* Lazy(Of T) class in .Net Framework4.0
