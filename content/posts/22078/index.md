---
title: "[C#]取得MIME Content Type對應的檔案副檔名"
slug: "[CSharp]取得MIME Content Type對應的檔案副檔名"
date: "2011-03-25 12:35:13"
description: "[C#]取得MIME Content Type對應的檔案副檔名"
tags: [CSharp]
---
續[C#]取得檔案對應的MIME Content Type這篇，這次反過來若是想知道MIME Content Type對應到的副檔名有哪些的話，一樣我們可以從登錄檔中取得，像是下面這樣：
private static IEnumerable GetMIMESupportedExt(string mime)
{
    var linq = from item in Microsoft.Win32.Registry.ClassesRoot.GetSubKeyNames()
               let key = Microsoft.Win32.Registry.ClassesRoot.OpenSubKey(item)
               let value = key.GetValue("Content Type")
               where value != null && value.ToString().Equals(mime, StringComparison.CurrentCultureIgnoreCase)
               select item;
    return linq;
}   

完整的範例如下：

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
namespace ConsoleApplication11
{
    class Program
    {
        static void Main(string[] args)
        {
            foreach (var item in GetMIMESupportedExt("video/x-ms-asf"))
            {
                Console.WriteLine(item); ;
            }
        }
        private static IEnumerable GetMIMESupportedExt(string mime)
        {
            var linq = from item in Microsoft.Win32.Registry.ClassesRoot.GetSubKeyNames()
                       let key = Microsoft.Win32.Registry.ClassesRoot.OpenSubKey(item)
                       let value = key.GetValue("Content Type")
                       where value != null && value.ToString().Equals(mime, StringComparison.CurrentCultureIgnoreCase)
                       select item;
            return linq;
        } 
    }
}

運行結果：