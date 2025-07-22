---
title: "[.NET Concept][VB.NET]字串 = Nothing V.S 字串 is Nothing"
date: "2009-02-22 06:56:04"
description: "[.NET Concept][VB.NET]字串 = Nothing V.S 字串 is Nothing"
tags: [.NET Concept,VB.NET]
---

今天回答網友問題時，由於一時筆誤，把本來要寫『字串 is Nothing』的地方錯打成『字串 = Nothing』，造成程式怎麼看就是看不出哪裡邏輯有問題，最後才注意到這邊打錯。

發現後覺得很神奇，因為我一直以為寫成『字串 = Nothing』會編譯錯誤的，沒想到它竟然能過。但也由於它能過的關係，導致找了半天找不到問題所在。而問題就在於若是使用『字串 is Nothing』來判斷的話，須要字串的值真的是Nothing才會成立。而使用『字串 = Nothing』來判斷的話，則判斷時會把Nothing與String.Empty視為相等，因此就算是字串為空字串該判斷條件也會成立。

簡單的示意範例如下: