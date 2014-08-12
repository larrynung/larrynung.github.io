---
layout: post
title: "Auto assign assembly's build/revision number"
date: 2014-08-12 23:34
comments: true
categories: [".NET"]
keywords: ".NET, Assembly, Version"
description: "Auto assign assembly's build/revision number"
---

在做軟體開發時，總是會碰到遞增產品版號的需求，通常這種時候我們會撰寫 Script 在建置之前對 Assembly.vs 檔內的版本資訊進行修改，以達到像這樣的需求。  

<!-- More -->

<br/>

然而有些時後我們只是想要讓建置的版號跟前次建立的有所區隔，不一定要將版號遞增的話，其實不需要到撰寫 Script 這樣麻煩，只要透過 Visual Studio 內建的機制就可以做到了。  

<br/>

將 Assembly.vs 檔開啟，視需求將 AssemblyVersion 的 Build 或 Revision Number 部份用 * 替換。並將 AssemblyFileVersion 設定移除。  

{% img /images/posts/AutoAssignAssemblyVersion/1.png %}

<br/>

接著存檔建置，即會發現每次建置的版號會有所不同。 

<br/>

Build 的部份會是當前本地時間與 2000 年 1 月 1 日之間所差天數，Revision 部分為與本地午夜所差的秒數除以 2。  

Link
----
* [AssemblyVersionAttribute 建構函式 (System.Reflection)](http://msdn.microsoft.com/zh-tw/library/system.reflection.assemblyversionattribute.assemblyversionattribute.aspx)
* [Auto-Incrementing Build Numbers in Visual Studio.NET](http://razorleaf.com/2010/01/auto-incrementing-visual-studio/)
* [c# - Can I automatically increment the file build version when using Visual Studio? - Stack Overflow](http://stackoverflow.com/questions/356543/can-i-automatically-increment-the-file-build-version-when-using-visual-studio)
