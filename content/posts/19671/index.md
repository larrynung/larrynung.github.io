---
title: ".NET 4.0 New Feature - Stream.CopyTo"
date: "2010-11-24 12:55:49"
description: ".NET 4.0在Stream類別中新增了CopyTo方法，該方法有兩個多載版本CopyTo(Stream)、與CopyTo(Stream, Int32)。 CopyTo方法主要功能為將當前的資料流內容複製到另一資料流，能讓我們快速的做資料流內容的複製，不需要像以往一樣需先將來源資料流內容讀出，"
tags: [CSharp]
---

.NET 4.0在Stream類別中新增了CopyTo方法，該方法有兩個多載版本CopyTo(Stream)、與[CopyTo(Stream, Int32)](http://msdn.microsoft.com/zh-tw/library/dd783870.aspx)。

![image_thumb_1.png](/images/posts/19671/image_thumb_1.png)

CopyTo方法主要功能為將當前的資料流內容複製到另一資料流，能讓我們快速的做資料流內容的複製，不需要像以往一樣需先將來源資料流內容讀出，再對目標資料流寫入，以達資料流複製的功用。

值得注意的是CopyTo方法是從當前資料流的目前位置開始做複製的動作。

完整範例如下，這個範例會建立一個MemoryStream，並將"Test Stream.CopyTo"字樣寫入產生的MemoryStream，接著建立一個FileStream，其對應的檔案為Test.Txt，再透過Stream.CopyTo將MemoryStream資料內容寫入FileStream。

```csharp
using System.IO;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            using (MemoryStream sourceStream = new MemoryStream(512))
            {
                using (StreamWriter sw = new StreamWriter(sourceStream))
                {
                    sw.WriteLine("Test Stream.CopyTo");
                    sw.Flush();

                    sourceStream.Seek(0, SeekOrigin.Begin);

                    using (FileStream targetStream = new FileStream("Test.Txt", FileMode.Create))
                    {
                        sourceStream.CopyTo(targetStream);
                    }
                }
            }
        }
    }
}
```

運行後會在程式目錄下產生一個Test.Txt文字檔，其內容為"Test Stream.CopyTo"。

![image_thumb.png](/images/posts/19671/image_thumb.png)

## Link

* Stream.CopyTo 方法
* New Stream.CopyTo() in .Net framework 4
