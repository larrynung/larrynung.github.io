---
title: ".NET 4.0 New Feature - Environment.Is64BitProcess amp; Environment.Is64BitOperatingSystem"
date: "2010-12-12 11:33:51"
description: ".NET 4.0 New Feature - Environment.Is64BitProcess &amp; Environment.Is64BitOperatingSystem"
tags: [CSharp]
---

.NET 4.0在Environment類別新增Is64BitOperatingSystem與Is64BitProcess屬性，其功用分別為判斷當前作業系統是否為64位元版本，與判斷當前處理序是否為64位元。

Property
              Name        Description                  Is64BitOperatingSystem        是否為64位元作業系統                  Is64BitProcess        是否為64位元處理序          

使用範例：
  using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication4
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("64位元作業系統: {0}",Environment.Is64BitOperatingSystem);
            Console.WriteLine("64位元處理序: {0}", Environment.Is64BitProcess);
        }
    }
}

運行結果：