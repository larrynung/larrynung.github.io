---
title: ".NET 4.0 New Feature - Environment.FailFast"
date: "2010-11-29 09:37:09"
description: ".NET 4.0 New Feature - Environment.FailFast"
tags: [CSharp]
---

.NET 4.0中新增FailFast(String, Exception)多載方法，該多載方法主要是在應用程式損壞無法修復且執行try...catch...finally將會損壞程式資源下使用 ，可將訊息和例外狀況資訊寫入至 Windows 應用程式事件記錄檔後終止處理序,不會執行到try...catch...finally區塊。

實際看個使用上的例子，假設今天我們的程式發生了例外，且該例外我們無法將它修復，我們可以像下面這樣撰寫：

```csharp
using System;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Environment.FailFast("A castrophic failure has occured.", new DivideByZeroException ());
            }
            catch (Exception)
            {
                Console.WriteLine("catch...");
            }
            finally
            {
                Console.WriteLine("finally...");
            }
        }
    }
}
```

運行後程式會強迫終止，catch與finally區塊也不會運行到，運行後我們開啟事件檢視器，打開應用程式的事件，我們可以看到剛剛的運行讓我們多了兩筆事件，一個事件會告知發生的問題、堆疊、與寫入的訊息。

![image_thumb.png](/images/posts/19789/image_thumb.png)

一個事件則是會有例外的資訊。

![image3_thumb.png](/images/posts/19789/image3_thumb.png)

## Link

* Environment.FailFast 方法 (String, Exception)
