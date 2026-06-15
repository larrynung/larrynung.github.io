---
title: "[Performance][C#]StringBuilder與String.Join串接字串時的效能比較"
date: "2009-07-09 08:46:42"
description: "[Performance][C#]StringBuilder與String.Join串接字串時的效能比較"
tags: [CSharp,Performance]
---

這陣子在寫程式寫到要用分隔符號串接字串的時候，想到兩種方法：一種是透過StringBuilder去串字串、一種是先把字串塞到字串陣列，再用String.Join去串字串。雖然StringBuilder對於字串的串接效能做了很大的改善，但我直覺上仍認為後者效率比前者來得佳，特此做個實驗。

測試程式碼如下：

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;
```

```
namespace StringTest
{
    class Program
    {
        static void Main(string[] args)
        {
            string result="";
            int count = 1000;
            Stopwatch sw = Stopwatch.StartNew();
            for (int i = 0; i < count; i++)
            {
                result=Test1();
            }
            sw.Stop();
            Console.WriteLine("Method: String.Join");
            Console.WriteLine("Elapsed Time: "+sw.ElapsedMilliseconds );
            Console.WriteLine("Result: " + result);
```

```
            sw = Stopwatch.StartNew();
            for (int i = 0; i < count; i++)
            {
                result = Test2();
            }
            sw.Stop();
            Console.WriteLine("Method: StringBuilder");
            Console.WriteLine("Elapsed Time: " + sw.ElapsedMilliseconds);
            Console.WriteLine("Result: " + result);
        }
```

```
        static string Test1()
        {
            int count = 1000;
            string[] strList = new string[count];
            for (int i = 0; i < count; i++)
            {
                strList[i] = i.ToString();
            }
            return string.Join(",", strList);
        }
```

```
        static string Test2()
        {
            StringBuilder strList = new StringBuilder();
            int count = 1000;
            for (int i = 0; i < count-1; i++)
            {
                strList.Append (i.ToString() + ",");
            }
            return strList.Append((count-1).ToString()).ToString ();
        }
    }
```

}

執行結果

![image_thumb_4.png](/images/posts/9264/image_thumb_4.png)

![image_thumb_5.png](/images/posts/9264/image_thumb_5.png)

這樣看起來String.join方法是比較優一點，但後來經Ammon網友提醒發現這樣的試驗仍有著不公正的因素存在，故測試出來的結果是不正確的。這邊將其實驗代碼修改ㄧ下，把

```csharp
strList.Append (i.ToString() + ",");
```

改為

```csharp
strList.Append(i);
strList.Append(",");
```

順便加入下面程式碼讓兩個要測試的方法先行編譯，以避免JIT Compiler造成不必要的誤差。

```csharp
//Let JIT compiler precompiler
Test1(1);
Test2(1);
```

完整程式碼如下：

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;

namespace ConsoleApplication17
{
    class Program
    {
        static void Main(string[] args)
        {
            int testTimes = 10;
            int dataCount = 1000000;
            GoTest(dataCount, testTimes);
        }

        static void GoTest(int dataCount,int testTimes)
        {
            //Let JIT compiler precompiler
            Test1(1);
            Test2(1);

            //Test performance
            Stopwatch sw;
            long[] elapsedTimes = new long[testTimes];

            Console.WriteLine("String.Join...");
            for (int i = 0; i < testTimes; i++)
            {
                sw = Stopwatch.StartNew();
                Test1(dataCount);
                elapsedTimes[i] = sw.ElapsedMilliseconds;
                Console.WriteLine("Elapsed Time: " + elapsedTimes[i]);
            }
            Console.WriteLine("Average Elapsed Time: " + elapsedTimes.Average().ToString());

            Console.WriteLine();
            Console.WriteLine("StringBuilder...");
            for (int i = 0; i < testTimes; i++)
            {
                sw = Stopwatch.StartNew();
                Test2(dataCount);
                elapsedTimes[i] = sw.ElapsedMilliseconds;
                Console.WriteLine("Elapsed Time: " + elapsedTimes[i]);
            }
            Console.WriteLine("Average Elapsed Time: " + elapsedTimes.Average().ToString());
        }

        static string Test1(int count)
        {
            string[] strList = new string[count];
            for (int i = 0; i < count; i++)
            {
                strList[i] = i.ToString();
            }
            return string.Join(",", strList);
        }

        static string Test2(int count)
        {
            StringBuilder strList = new StringBuilder();
            for (int i = 0; i < count - 1; i++)
            {
                strList.Append(i);
                strList.Append(",");
            }
            return strList.Append(count - 1).ToString();
        }
    }
}
```

為避免誤差，這邊多運行了幾次，運行結果如下：

![image_thumb_7.png](/images/posts/9264/image_thumb_7.png)

![image_thumb_8.png](/images/posts/9264/image_thumb_8.png)

![image_thumb_9.png](/images/posts/9264/image_thumb_9.png)
