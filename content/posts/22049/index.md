---
title: "[C#]取得檔案對應的MIME Content Type"
slug: "[CSharp]取得檔案對應的MIME Content Type"
date: "2011-03-24 01:12:45"
description: "在寫Youtube的上傳時，在設定上傳的資訊中有一項是Content Type，該屬性是字串型態，且未提供我們列舉直接選取或是自動由檔案名稱判別的功能，在這邊被卡關了許久，最後下才發現這邊的Content Type指的是MIME Content Type。"
tags: [CSharp]
---

在寫Youtube的上傳時，在設定上傳的資訊中有一項是Content Type，該屬性是字串型態，且未提供我們列舉直接選取或是自動由檔案名稱判別的功能，在這邊被卡關了許久，最後下才發現這邊的Content Type指的是MIME Content Type。而要取得檔案對應的MIME Content Type，其實並不困難，因為這樣的資訊都已經存在登錄檔中了，我們可以從登錄檔中的資訊下手，只要會用程式擷取出登錄檔資訊就可以取得檔案對應的MIME Content Type。

MIME Content Type資訊存放在登錄檔中的HKEY_CLASSES_ROOT\[副檔名]\Content Type下

![image_thumb_1.png](/images/posts/22049/image_thumb_1.png)

因此由指定檔案的附檔名可以找到HKEY_CLASSES_ROOT下對應的機碼，再取得機碼下的Content Type值就可以了：

```
private static string GetContentTypeForFileName(string fileName)
{
    string ext = System.IO.Path.GetExtension(fileName);
    using (Microsoft.Win32.RegistryKey registryKey = Microsoft.Win32.Registry.ClassesRoot.OpenSubKey(ext))
    {
        if (registryKey == null)
            return null;
        var value = registryKey.GetValue("Content Type");
        return (value == null) ? string.Empty : value.ToString();
    }
}
```

完整範例如下：

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
namespace ConsoleApplication10
{
    class Program
    {
        static void Main(string[] args)
        {
            const string file = @"C:\Users\Public\Music\Sample Music\Sleep Away.mp3";
            Console.WriteLine(GetContentTypeForFileName(file));
        }
        private static string GetContentTypeForFileName(string fileName)
        {
            string ext = System.IO.Path.GetExtension(fileName);
            using (Microsoft.Win32.RegistryKey registryKey = Microsoft.Win32.Registry.ClassesRoot.OpenSubKey(ext))
            {
                if (registryKey == null)
                    return null;
                var value = registryKey.GetValue("Content Type");
                return (value == null) ? string.Empty : value.ToString();
            }
        }    }
}
```

運行結果：

![image_thumb.png](/images/posts/22049/image_thumb.png)

## Link

* [MIME](http://zh.wikipedia.org/wiki/MIME)
* [MIME Reference](http://www.w3schools.com/media/media_mimeref.asp)
