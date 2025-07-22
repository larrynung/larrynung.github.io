---
title: ".NET 4.0 New Feature - SplitContainer implements ISupportInitialize"
date: "2013-11-06 12:00:00"
description: ".NET 4.0 New Feature - SplitContainer implements ISupportInitialize"
---

最近在使用Visual Studio 2010寫些小程式時，在界面上放了個SplitContainer，一開始運作良好，但切換到.NET Framework 4.0以前的Framework後，卻發生如下的錯誤。

查了一下才發現原來在.NET 4.0後，SplitContainer開始實作了ISupportInitialize介面。

因此當本來在.NET 4.0使用SplitContainer，切換到.NET 4.0以前的Framework就會發生錯誤，這並不算是BUG，但卻要開發人員稍微注意並處理一下，解決辦法自然就是把Designer.cs內SplitContainer調用ISupportInitialize的介面成員部分程式給拿掉就好了。

## Link
     SplitContainer.BeginInit Method    SplitContainer.EndInit Method