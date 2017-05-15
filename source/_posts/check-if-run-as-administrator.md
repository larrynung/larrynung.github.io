---
layout: post
title: "Check if run as administrator"
date: 2014-02-25 23:46:00
comments: true
tags: CSharp
keywords: "Administrator"
description: "Check if run as administrator"
---

要判斷當前使用者是否具有管理者權限，我們可以先取得當前使用的 WindowsIdenty。 

<!-- More -->
    var wi = WindowsIdentity.GetCurrent();


接著帶入剛取得的 WindowsIdenty，建立對應的 WindowsPrinciple。 

    var wp = new WindowsPrincipal(wi);


透過 WindowsPrinciple 的 IsInRole 方法判斷當前的使用者是否為 WindowsBuiltInRole.Administrator。 

    var isAdmin = wp.IsInRole(WindowsBuiltInRole.Administrator);


所以整個程式會像下面這樣 : 

```c# 
private bool IsRunAsAdministrator() 
{
    var wi = WindowsIdentity.GetCurrent(); 
    var wp = new WindowsPrincipal(wi); 
    return wp.IsInRole(WindowsBuiltInRole.Administrator);
}
```

<br/>

Link
-----
* [AntsCode: Running a ClickOnce Application as Administrator](http://antscode.blogspot.tw/2011/02/running-clickonce-application-as.html)
