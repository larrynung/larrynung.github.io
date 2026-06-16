---
title: "[C#]取得檔案內容中的詳細資料"
slug: "csharp-取得檔案內容中的詳細資料"
aliases: ["/posts/csharp取得檔案內容中的詳細資料/"]
date: "2011-03-21 10:16:06"
description: "這邊記錄ㄧ下要如何取得檔案內容中的詳細資料 ... 首先我們必須將Microsoft Shell Controls and Automation加入參考。 加入Shell32命名空間後就可以開始使用了..."
tags: [CSharp]
---

這邊記錄ㄧ下要如何取得檔案內容中的詳細資料 ...

![image_thumb.png](/images/posts/21994/image_thumb.png)

首先我們必須將Microsoft Shell Controls and Automation加入參考。

![image_thumb_3.png](/images/posts/21994/image_thumb_3.png)

加入Shell32命名空間後就可以開始使用了...

使用上先建立ShellClass物件實體，透過ShellClass中的Namespace方法取得Folder物件，接著利用ParseName方法取得FolderItem物件，取得了FolderItem物件後對其叫用GetDetailsOf，將要抓取的詳細資料索引代入即可求得。

static string GetDetailValue(string file, int column)
{
    ShellClass sh = new ShellClass();
    Folder dir = sh.NameSpace(Path.GetDirectoryName(file));
    FolderItem item = dir.ParseName(Path.GetFileName(file));
    return dir.GetDetailsOf(item, column);
}

但是詳細資料頁面中的資料有很多，依照不同檔案類型又有不同的資訊，要如何才能取得想要的詳細資料索引?只要透過類似上面的作法，將GetDetailsOf方法的第一個參數代入0即可：

```
static IEnumerable<KeyValuePair<string, int>> GetDetailColumn()
{
    ShellClass sh = new ShellClass();
    Folder dir = sh.NameSpace(@"c:\");

    int idx = 0;
    string columnName = dir.GetDetailsOf(0, idx);
    do
     {
        yield return new KeyValuePair<string, int>(columnName, idx);
        columnName = dir.GetDetailsOf(0, ++idx);
     } while (!string.IsNullOrEmpty(columnName));
}
```

完整的範例如下：

```
using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using Shell32;

using System.IO;

namespace ConsoleApplication1

{

    class Program

    {

        static void Main(string[] args)

        {

            ViewDetailColumn();

            Console.WriteLine(new string('=', 50));

            var file = @"C:\Users\Public\Music\Sample Music\Kalimba.mp3";

            ViewDetailValue(file, "Album");

            ViewDetailValue(file, "Size");

        }

        static IEnumerable<KeyValuePair<string, int>> GetDetailColumn()

        {

            ShellClass sh = new ShellClass();

            Folder dir = sh.NameSpace(@"c:\");

            int idx = 0;

            string columnName = dir.GetDetailsOf(0, idx);

            do

            {

                yield return new KeyValuePair<string, int>(columnName, idx);

                columnName = dir.GetDetailsOf(0, ++idx);
            } while (!string.IsNullOrEmpty(columnName));

        }

        static IEnumerable<KeyValuePair<string, int>> GetDetailColumn(int offset, int count)

        {

            ShellClass sh = new ShellClass();

            Folder dir = sh.NameSpace(@"c:\");

            for (var idx = offset; idx < offset + count; ++idx)

            {

                yield return new KeyValuePair<string, int>(dir.GetDetailsOf(0, idx), idx);

            }

        }

        static void ViewDetailColumn()

        {

            var columns = GetDetailColumn();

            foreach (var item in columns)

            {

                Console.WriteLine(item.Key);

            }

        }

        static void ViewDetailColumn(int offset, int count)

        {

            var columns = GetDetailColumn(offset, count);

            foreach (var item in columns)

            {

                Console.WriteLine(item.Key);

            }

        }

        static string GetDetailValue(string file, int column)

        {

            ShellClass sh = new ShellClass();

            Folder dir = sh.NameSpace(Path.GetDirectoryName(file));

            FolderItem item = dir.ParseName(Path.GetFileName(file));

            return dir.GetDetailsOf(item, column);

        }

        static void ViewDetailValue(string file, int column)

        {

            Console.WriteLine(GetDetailValue(file, column));

        }

        static string GetDetailValue(string file, string column)

        {

            var linq = from item in GetDetailColumn()

                       where item.Key == column

                       select item.Value;

            return GetDetailValue(file, linq.FirstOrDefault());

        }

        static void ViewDetailValue(string file, string column)

        {

            Console.WriteLine(GetDetailValue(file, column));

        }

    }

}
```

運行結果如下：

![image_thumb_2.png](/images/posts/21994/image_thumb_2.png)

## Link

* 如何用C#获得文件信息以及扩展信息
