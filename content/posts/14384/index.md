---
title: "[C#]Notes on Measuring Cumulative Elapsed Time with Stopwatch"
slug: "csharp-notes-on-measuring-cumulative-elapsed-time-with-stopwatch"
aliases: ["/posts/csharp用stopwatch計算累計耗費時間的注意事項/"]
date: "2010-04-03 10:45:13"
description: "今天跟網友討論程式效能時，注意到在使用Stopwatch的一些注意事項，簡單紀錄一下。 Stopwatch類別重要的成員不外乎StartNew、Start、Stop、Reset、ElapsedTicks、與ElapsedMilliseconds。"
tags: [CSharp]
---

今天跟網友討論程式效能時，注意到在使用Stopwatch的一些注意事項，簡單紀錄一下。

Stopwatch類別重要的成員不外乎StartNew、Start、Stop、Reset、ElapsedTicks、與ElapsedMilliseconds。使用上，只要依序呼叫Start→Stop→ElapsedMilliseconds或ElapsedTicks，就可以得到運行的耗費時間。要計算多段程式累計耗費的時間，也只要Start→Stop→…→Start→Stop→ElapsedMilliseconds或ElapsedTicks即可。

但在計算累計耗費時間時，也有人會用Reset→Start→Stop→加總→…這樣的方法來做。但這樣的做法會比較耗時，求得的值也會有誤差。

讓我們來先看段程式

```csharp
static void Main(string[] args)
{
    int count = 1000000;
    long total = 0;
    Stopwatch sw = new Stopwatch();

    for (int i = 1; i <= count; i++)
    {
        sw.Reset();
        sw.Start();
        string guid = Guid.NewGuid().ToString();
        sw.Stop();
        total += sw.ElapsedMilliseconds;
    }
    Console.WriteLine(total);

    sw.Reset();
    for (int i = 1; i <= count; i++)
    {
        sw.Start();
        string guid = Guid.NewGuid().ToString();
        sw.Stop();
    }
    Console.WriteLine(sw.ElapsedMilliseconds);

}
```

運行結果如下

![image_thumb.png](/images/posts/14384/image_thumb.png)

從這運行結果我們可以看出，兩種不同作法的結果差異很大。那哪個才是正確的呢？讓我們再看些例子。

```csharp
static void Main(string[] args)
{
    int count = 1000;
    long total = 0;
    Stopwatch sw = new Stopwatch();

    for (int i = 1; i <= count; i++)
    {
        sw.Reset();
        sw.Start();
        System.Threading.Thread.Sleep(10);
        sw.Stop();
        total += sw.ElapsedMilliseconds;
    }
    Console.WriteLine(total);

    sw.Reset();
    for (int i = 1; i <= count; i++)
    {
        sw.Start();
        System.Threading.Thread.Sleep(10);
        sw.Stop();
    }
    Console.WriteLine(sw.ElapsedMilliseconds);

}
```

運行結果如下

![image_thumb_3.png](/images/posts/14384/image_thumb_3.png)

```csharp
static void Main(string[] args)
{
    int count = 10;
    long total = 0;
    Stopwatch sw = new Stopwatch();

    for (int i = 1; i <= count; i++)
    {
        sw.Reset();
        sw.Start();
        System.Threading.Thread.Sleep(1000);
        sw.Stop();
        total += sw.ElapsedMilliseconds;
    }
    Console.WriteLine(total);

    sw.Reset();
    for (int i = 1; i <= count; i++)
    {
        sw.Start();
        System.Threading.Thread.Sleep(1000);
        sw.Stop();
    }
    Console.WriteLine(sw.ElapsedMilliseconds);
}
```

運行結果如下

![image_thumb_2.png](/images/posts/14384/image_thumb_2.png)

由上實驗可以看出，當運算量龐大時，兩個方法所求得的值會變得相近，因此很明顯的可以看出，自行加總的方法是有誤差的。

之所以會有這樣的現象，個人推測是由於小於毫秒的花費時間，在使用加總的方式處理時，會被忽略不記所導致。
