---
title: "C++/CLI Managed解構子"
date: "2009-09-17 09:03:44"
description: "C++/CLI Managed解構子"
tags: [C++]
---

在傳統C++中，解構子的寫法是"~類別名()"。而在C++/CLI中雖然也有這種寫法，但效果卻截然不同。

在C++/CLI Managed類別中，"~類別名()"其實相當於.NET程式的Dispose。在其它語言參考使用時，寫有"~類別名()"的類別，我們可以透過Dispose來釋放資源。

而要撰寫C++/CLI Managed類別的解構子，我們可以用"!類別名()"。

簡單的範例如下：
```
ref class TestObj
{
public:
//Dispose
~TestObj()
{
//Release resource
...
}

//Deconstructer
!TestObj()
{
~TestObj();
}
};
```