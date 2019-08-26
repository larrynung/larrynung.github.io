---
title: MethodTimer.Fody - Injects some very basic method timing code
date: 2019-08-26 07:21:41
tags: [Fody]
---

MethodTimer.Fody 能透過 Fody 在程式編譯時將用來計算時間的程式放入掛有 TimeAttribute 的方法。  

<!-- More -->

</br>


使用時需先引用 MethodTimer.Fody 套件。  

```xml
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <OutputType>Exe</OutputType>
        <TargetFramework>netcoreapp2.2</TargetFramework>
    </PropertyGroup>


    <ItemGroup>
      <PackageReference Include="MethodTimer.Fody" Version="3.0.0" PrivateAssets="All" />
    </ItemGroup>

</Project>
```

</br>


然後加入 FodyWeavers.xml 檔，檔案內容如下，指示 Fody 要使用 MethodTimer。  

```xml
<?xml version="1.0" encoding="utf-8"?>
<Weavers xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="FodyWeavers.xsd">
  <MethodTimer />
</Weavers>
```

</br>


接著在 MethodTimeLogger 的 Log 方法撰寫時間計算的部分。  

```c#
using System;
using System.Reflection;


namespace Fody.MethodTimer
{
    public static class MethodTimeLogger
    {
        public static void Log(MethodBase methodBase, long milliseconds, string message)
        {
            Console.WriteLine($"[{methodBase.DeclaringType.Name}.{methodBase.Name}] {message} {milliseconds} ms");
        }
    }
}
```

</br>


{% asset_img 1.png %}

</br>


然後在要計算時間的部分加掛 TimeAttribute，TimeAttribute 可掛在方法、類別、模組上，掛上時可順帶帶入對應的訊息。  

```c#
using System;
using MethodTimer;


namespace Fody.MethodTimer
{
    class Program
    {
        [Time("Application start...")]
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
```

{% asset_img 2.png %}

</br>


Link
====
* [Fody/MethodTimer: Injects some very basic method timing code](https://github.com/Fody/MethodTimer)
