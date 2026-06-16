---
title: "[C#]LevelUp.Lazy"
slug: "[CSharp]LevelUp.Lazy"
date: "2011-04-04 12:30:18"
description: "在.NET 4.0 New Feature - Generic Lazy class中介紹過.NET 4.0提供的好用的Lazy類別，能輕鬆的讓我們做物件的初始動作，但在.NET 4.0以前想要使用類似的類別呢?好在筆者在.NET 4.0的修練中有大約的知道簡易的實作概念，這邊將其概念加以延伸，"
tags: [CSharp]
---

在.NET 4.0 New Feature - Generic Lazy class中介紹過.NET 4.0提供的好用的Lazy類別，能輕鬆的讓我們做物件的初始動作，但在.NET 4.0以前想要使用類似的類別呢?好在筆者在.NET 4.0的修練中有大約的知道簡易的實作概念，這邊將其概念加以延伸，稍微花了一點時間整理成自己的Lazy類別便於後續使用。

該類別除了跟4.0的Lazy類別具有一樣的Lazy Evaluation特性外，外加入清除初始值的功能，藉由初始值的清除與ㄧ開始傳入的初始動作，可以很輕鬆的做出重新整理的效果。另外，該類別也加入了類似Proxy pattern概念的效果、與非同步初始、背景初始等功能，這些功能的加入可以應用在很多地方，像是歡迎畫面出現時啟用背景初始，或是在值尚未初始的狀況顯示預設的值，有興趣的可以試玩看看。

完整的使用範例如下：

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using LevelUpLazy = LevelUp.Lazy;
using System.Diagnostics;

namespace LazyDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            var count = 10;
            LevelUpLazy.Lazy<string>[] lazys = new LevelUpLazy.Lazy<string>[count];
            for (int i = 0; i < count; i++)
            {
                lazys[i] = new LevelUpLazy.Lazy<string>(DoWork);
            }

            lazys[3].ValueInited += new EventHandler(laz3_ValueInited);
            lazys[3].BeginInit();

            lazys[2].BeginInit();

            Stopwatch sw = Stopwatch.StartNew();
            Console.WriteLine("lazy1 result = {0}", lazys[1].Value);
            Console.WriteLine("lazy1 Elapsed Time = {0} ms", sw.ElapsedMilliseconds);

            sw.Restart();
            Console.WriteLine("lazy1 result = {0}", lazys[1].Value);
            Console.WriteLine("lazy1 Elapsed Time = {0} ms", sw.ElapsedMilliseconds);

            //Refresh Init
            sw.Restart();
            lazys[1].ClearValue();
            Console.WriteLine("lazy1 result = {0}", lazys[1].Value);
            Console.WriteLine("lazy1 Elapsed Time = {0} ms", sw.ElapsedMilliseconds);

            sw.Restart();
            Console.WriteLine("lazy2 result = {0}", lazys[2].Value);
            Console.WriteLine("lazy2 Elapsed Time = {0} ms", sw.ElapsedMilliseconds);

            //Proxy
            lazys[4].InitialValue ="Temp Value";
            for (int i = 0; i < 10; ++i)
            {
                Console.WriteLine("lazy4 result = {0}", lazys[4].Value);
                System.Threading.Thread.Sleep(200);
            }

            //Background Init
            LevelUpLazy.Lazy<string>.EnableBackgroundInit = true;
            System.Threading.Thread.Sleep(5000);
            for (int i = 0; i < count; ++i)
            {
                if (lazys[i].IsValueCreated)
                    Console.WriteLine("lazy{0} result = {1}", i, lazys[i].Value);
            }

        }

        static void laz3_ValueInited(object sender, EventArgs e)
        {
            LevelUpLazy.Lazy<string> lazy3 = sender as LevelUpLazy.Lazy<string>;
            Console.WriteLine("lazy3 result = {0}", lazy3.Value);
        }

        static string DoWork()
        {
            System.Threading.Thread.Sleep(1000);
            return Guid.NewGuid().ToString ();
        }
    }
}
```

運行結果如下：

![image_thumb.png](/images/posts/22246/image_thumb.png)

## Download

Lazy.zip
