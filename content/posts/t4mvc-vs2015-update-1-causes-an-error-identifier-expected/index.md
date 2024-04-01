---
title: "T4MVC - VS2015 Update 1 causes an error - Identifier Expected"
date: "2016-01-23 21:40:00"
description: "T4MVC - VS2015 Update 1 causes an error - Identifier Expected"
tags: [T4MVC]
---


T4MVC 在 Visual Studio 2015 安裝完 Update 1 後，產生的程式碼會像這樣。  

<!-- More -->

<br/>


```c#
public override void ExecuteResult(System.Web.Mvc.ControllerContext ) { }
```

<br/>


可以看到 ExecuteResult 方法的參數消失了，所以編譯時會報 Identifier Expected 的錯誤。  

{% img /images/posts/T4MVCIdentifierExpected/1.png %}

<br/>


若要解決這問題，可到 [Update for Microsoft Visual Studio 2015 (KB3110221)](https://msdn.microsoft.com/en-US/library/mt634751\(VS.140\).aspx) 這邊下載更新套件，安裝後即可解決此問題。  

<br/>


Link
----
* [VS2015 Update 1 causes an error - Identifier Expected · Issue #54 · T4MVC/T4MVC](https://github.com/T4MVC/T4MVC/issues/54)
* [Update for Microsoft Visual Studio 2015 (KB3110221)](https://msdn.microsoft.com/en-US/library/mt634751\(VS.140\).aspx)
