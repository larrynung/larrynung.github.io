---
title: "[VB.NET]使用SuppressIldasmAttribute防止MSIL反組譯工具對組件進行反組譯"
date: "2010-05-09 10:17:59"
description: "Introduction 使用SuppressIldasmAttribute可為自己開發的組件加上一層簡單的防護，該防護動作只對MSIL反組譯工具(Ildasm.exe)有效，對於Reflector則無任何的防護效果。"
tags: [VB.NET]
---

## Introduction

使用SuppressIldasmAttribute可為自己開發的組件加上一層簡單的防護，該防護動作只對MSIL反組譯工具(Ildasm.exe)有效，對於Reflector則無任何的防護效果。值得注意的是，該防護是非常簡單的防護，很輕鬆的就可以把該防護給拿掉，因此不建議單純靠這屬性來保護組件。

## NameSpace

System.Runtime.CompilerServices

## Assembly

mscorlib (在 mscorlib.dll 中)

## SuppressIldasmAttribute

對於一般未保護的.NET程式來說，我們都可以把組件放入IL Dasm查看其中繼碼，如下圖所示：

![image_thumb_1.png](/images/posts/15105/image_thumb_1.png)

而在.NET 2.0後，[System.Runtime.CompilerServices](http://msdn.microsoft.com/zh-tw/library/system.runtime.compilerservices.aspx)命名空間加入了[SuppressIldasmAttribute](http://msdn.microsoft.com/zh-tw/library/system.runtime.compilerservices.suppressildasmattribute.aspx)屬性可防止組件被載入IL Dasm。使用上我們只需在AssemblyInfo這個檔案中，加入<Assembly: SuppressIldasmAttribute()> 。

![image_thumb_2.png](/images/posts/15105/image_thumb_2.png)

編譯出來的組件就會變得無法用IL Dasm載入。

![image_thumb_3.png](/images/posts/15105/image_thumb_3.png)

## Link

* [SuppressIldasmAttribute 類別](http://msdn.microsoft.com/zh-tw/library/system.runtime.compilerservices.suppressildasmattribute.aspx)
