---
title: "Boxing amp; UnBoxing"
date: "2015-09-21 23:11:00"
description: "Boxing &amp; UnBoxing"
---


Boxing 是種隱含的處理，當 Value Type 物件塞到 Reference Type 時發生，會幫我們在 Managed Heap 建立一塊空間，並將本來 Value Type 的值賦予其中。  

<!-- More -->

<br/>

舉個例子來說，像是這邊宣告個 int 變數 i，若我們像下面這樣將它塞到 object。  

```c#
int i = 123; 
object o = i; // explicit boxing
```

{% img /images/posts/BoxingUnBoxing/1.png %}

<br/>


因為 int 為 Value Type，object 為 Reference Type，故會做 Boxing 的處理。  

<br/>


UnBoxing 是種明確的處理，當我們將裝箱的物件明確轉型時發生，會把裝箱的物件塞回到 Stack。  

<br/>


像是延續之前的例子，我們將 o 轉型成 int 時，裝箱在裡面的資料會被拆箱出來放到新的 Stack 位置。  

```c#
int i = 123; // a value type 
object o = i; // boxing 
int j = (int)o; // unboxing
```

{% img /images/posts/BoxingUnBoxing/2.png %}

<br/>


之所以要了解 Boxing & UnBoxing 的運作，是因為他會帶來不必要的性能耗費，透過下面這段簡單的測試就可以清楚的看出。  

```c#
using System; 
using System.Diagnostics; 

internal class Program { 
    private static void Main(string[] args) { 
        var count = 1000000000; 
        Console.WriteLine(“Boxing: {0} ms", 
        DoTest(count, () => { 
            var value = 123; 
            object value2 = value; 
        })); 
        Console.WriteLine(“None boxing: {0} ms", 
        DoTest(count, () => { 
            var value = 123; 
            var value2 = value; 
        })); 
    } 
    static long DoTest(int count, Action action) { 
        var sw = Stopwatch.StartNew(); 
        for (int i = 0; i < count; ++i) action(); 
        return sw.ElapsedMilliseconds; 
    } 
}
```

{% img /images/posts/BoxingUnBoxing/3.png %}

<br/>


到這邊你可能會說，其實我很少宣告成 Object，也不會這樣塞值。但真的是這樣嗎？看看以下例子：  

```c#
using System; 
using System.Diagnostics; 
internal class Program { 
    private static void Main(string[] args) { 
        var count = 1000000000; 
        Console.WriteLine("Boxing: {0} ms", 
        DoTest(count, () => { 
            var value = 123; 
            var value2 = string.Format("{0}", value); 
        })); 
        Console.WriteLine("None Boxing: {0} ms", 
        DoTest(count, () => { 
            var value = 123; 
            var value2 = string.Format("{0}", value.ToString()); 
        })); 
    } 
    static long DoTest(int count, Action action) { 
        var sw = Stopwatch.StartNew(); 
        for (int i = 0; i < count; ++i) action(); 
        return sw.ElapsedMilliseconds; 
    } 
}
```

{% img /images/posts/BoxingUnBoxing/4.png %}

<br/>


可以看到其實我們很容易就造成不必要的 Boxing，因為不能避免的還是會有些方法會要求傳入 Object 型態，像是 String.Format。如果叫用時帶入的數值不主動呼叫 ToString 讓它透過低階的 API 轉成字串，就會造成 Boxing。

<br/>


除了記憶體的耗費與效能的影響外，不了解 Boxing & UnBoxing 的運作可能也會寫出不如我們所預期的程式。  

<br/>


像是下面這段程式將整數數值塞入了物件，接著嘗試將物件轉型為 float。  

```c#
using System; 

internal class Program { 
    private static void Main(string[] args) 
    { 
        try { 
            var value1 = 1; 
            object value2 = value1; 
            var value3 = (float)value2; 
        } catch (Exception ex) { 
            Console.WriteLine(ex); 
        } 
    } 
}
```

{% img /images/posts/BoxingUnBoxing/5.png %}

<br/>


但因為物件內裝的是整數數值，當用 float 轉型時會長是用 float 進行拆箱，因為無法拆箱，所以系統會發出例外。  

<br/>


接著看一下下面這段程式。    

```c#
using System; 

struct Counter 
{ 
    private int x; 
    public void Increment() { this.x++; } 
    public int Count { get { return this.x; } } 
} 

internal class Riddle
 { 
    public readonly object counter = new Counter();
 } 

internal class Program 
{ 
    private static void Main(string[] args)
     { 
       var riddle = new Riddle(); 
       ((Counter)riddle.counter).Increment(); 
       Console.WriteLine(((Counter)riddle.counter).Count); 
    } 
}
```

{% img /images/posts/BoxingUnBoxing/6.png %}

<br/>


因為拆箱後是在新的 Stack 位置，所以第一次拆箱呼叫 Increment，與後來拆箱取 Count 的實體是不同的。  

<br/>


既然 Boxing & UnBoxing 那麼值得我們注意，有什麼好方法可以檢測出來嗎？以前筆者是用反組譯後看 MSIL 有無 Box 命令去偵測，後來找到 ReSharper - Heap Allocation Viewer Extension 與 Clr C# Heap Allocation Analyzer，偵測起來輕鬆了許多。  

<br/>


Link
----
* [Boxing &amp; unboxing](http://www.slideshare.net/larrynung/boxing-unboxing)
* [Boxing 和 Unboxing (C# 程式設計手冊)](https://msdn.microsoft.com/zh-tw/library/yz2be5wk.aspx)
