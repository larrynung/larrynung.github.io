---
title: "[Linq]Linq程式逐步執行與偵錯"
date: "2010-04-18 12:18:57"
description: "[Linq]Linq程式逐步執行與偵錯"
tags: [VB.NET, CSharp, Linq]
---

若是使用C#要對Linq程式做逐步的執行與偵錯，我們可以直接透過Step (F11)逐步執行。

舉個例子來說，假設今天想要對下列Linq程式做逐步執行。

```csharp
static void Main(string[] args)
{
    int[] items = Enumerable.Range(1, 10).ToArray();
    var linq = from item in items
               where (item % 2) == 0
               select new { Name = "Item", Value = item };

    foreach (var item in linq)
    {
        Console.WriteLine(item);
    }
}
```

我們可把中斷點設在迴圈上方，運行後會中斷在中斷點的位置上。

![image_thumb_3.png](/images/posts/14659/image_thumb_3.png)

此時透過按下Step (F11) 就可以發現執行位置跑到了Linq陳述式上方，此時我們就可以透過Visual Studio監看到Linq陳述式的值了。

![image_thumb.png](/images/posts/14659/image_thumb.png)

![image_thumb_1.png](/images/posts/14659/image_thumb_1.png)

而若是要使用VB.NET對Linq程式做逐步的執行與偵錯，相較之下會比C#來的麻煩。主要可分為三個步驟：

1. 使用函式來取代部分Linq陳述式
2. 使用迴圈讀取Linq內的元素
3. 中斷點設在函式中做逐步偵錯的動作

![image_thumb.png](/images/posts/14659/image_thumb.png)

舉個例子來說，假設今天想要對下列Linq程式做逐步執行。

```vb
Sub Main()
    Dim items() As Integer = Enumerable.Range(1, 10).ToArray
    Dim linq = From item In items Where item Mod 2 = 0 Select New With {.Name = "Item", .Value = item}

    For Each item In linq
        Console.WriteLine(item)
    Next
End Sub
```

把Linq部分陳述式改用函式替代，當程式跑到迴圈時，就可以在該函式中除錯。

![image_thumb_3.png](/images/posts/14659/image_thumb_3.png)

## Link

* 逐步執行和 LINQ
