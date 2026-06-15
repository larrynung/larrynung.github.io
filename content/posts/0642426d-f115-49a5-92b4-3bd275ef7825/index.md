---
title: "[Web][.NET Resourec]使用compilify.net在網站上撰寫簡易的C#程式"
date: "2013-11-06 12:00:00"
description: "[Web][.NET Resourec]使用compilify.net在網站上撰寫簡易的C#程式"
tags: [CSharp]
---

compilify.net是一個可以線上撰寫C#程式的網站，使用上十分簡單，網站主要分為三個區塊，左邊是用來做些定義的，右邊是要執行的動作，下方是執行後的結果。實際來看一下網站預設的程式，它在左邊定義區塊定義了一個Person類別，內含有Greet成員方法，右邊執行區塊宣告了一個Person物件並叫用Greet後將結果回傳。

![image6_thumb.png](/images/posts/0642426d-f115-49a5-92b4-3bd275ef7825/image6_thumb.png)

若沒有需要事先定義的程式，也可以直接撰寫執行部份的程式碼。這邊可以看到它連區域型別推斷都已經實作進去了。

![image_thumb_5.png](/images/posts/0642426d-f115-49a5-92b4-3bd275ef7825/image_thumb_5.png)

不過像是Linq或是async這些語法就還未被實作進去。

![image_thumb_4.png](/images/posts/0642426d-f115-49a5-92b4-3bd275ef7825/image_thumb_4.png)

這邊筆者試著用複雜一點的例子來測試一下，寫了一個測試空字串的程式碼片段：

```csharp
using System.Diagnostics;
private static string TestEmptyString(int count)
{
    String test;
    Stopwatch sw = Stopwatch.StartNew();
    for (int idx = 0; idx < count; ++idx)
    {
        test = "";
    }
    sw.Stop();
    return "EmptyString: " + sw.ElapsedMilliseconds.ToString();
}
```

實際運行測試時，帶入1000000當作參數下去測試。

```csharp
return TestEmptyString(1000000);
```

運行後整個運作都還算良好，整個看起來完成度還算不錯，在寫些小程式時還滿好用的。

![image9_thumb.png](/images/posts/0642426d-f115-49a5-92b4-3bd275ef7825/image9_thumb.png)

另外它也具備存檔功能，按下上方的Save後，仔細注意網站的網址會變換，這個網址就是儲存後的網址，複製這段網址給別人，別人就可以看到你在上面所輸入的程式，可以直接運行看到運行結果，雖然不知道儲存能保留多久，但是這樣的功能對於類似在論壇上回覆這種遠距離的指導程式時，感覺特別好用。

![image_thumb_6.png](/images/posts/0642426d-f115-49a5-92b4-3bd275ef7825/image_thumb_6.png)

這個服務整個測下來感覺還不錯用，美中不足的是沒有intellisense，也不能除錯，Console.WriteLine、Debug.WriteLine、Trace.WriteLine這些輸出輔助訊息的方法都無效，整個除錯上變得困難許多，從例外中也不好找到問題所在。

![image3_thumb.png](/images/posts/0642426d-f115-49a5-92b4-3bd275ef7825/image3_thumb.png)

## Link

* [compilify.net alpha](http://compilify.net)
* [Compilify——讓你在瀏覽器中編譯.NET代碼](http://www.dotblogs.com.tw/larrynung/1204)
* [Compile .NET in your browser using Compilify by Justin Rusbatch](http://www.hanselman.com/blog/CompileNETInYourBrowserUsingCompilifyByJustinRusbatch.aspx)
* [Compilify / Compilify](https://github.com/compilify/Compilify)
