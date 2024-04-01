---
title: "ASP.NET MVC - Remove unnecessary view engine"
date: "2014-04-08 00:08:00"
description: "ASP.NET MVC - Remove unnecessary view engine"
tags: [ASP.NET MVC]
---


ASP.NET MVC 預設會載入多個 View engine，儘管在專案建立之時我們就已明確的指定了所要使用的 View engine。  

<!-- More -->

<br/>

以一個最簡單的空專案來看，這邊特地將 Home 的 Index view 給刪掉，接著將之運行，運行後因為找不到 View 所以會顯示錯誤頁面。  

{% img /images/posts/RemoveUnnecessaryViewEngine/1.png %}

<br/>

這邊可以看到系統會嘗試載入不同程式語言所撰寫的不同 View engine 檔。然而在大部分的情況下，我們只會選用ㄧ種程式語言與View engine。

<br/>

因此像這樣載入過多的 View engine 反而形成不必要的耗費，故我們可以在啟動時加入程式將之移除。

```c# 
protected void Application_Start()
{
    ViewEngines.Engines.Clear();
    ViewEngines.Engines.Add(new RazorViewEngine());
    ...
}
```

<br/>

再次運行就會看到這樣作就只會嘗試載入我們預期的 View Engine。

{% img /images/posts/RemoveUnnecessaryViewEngine/2.png %}

<br/>

如果真有同時載入多個 View engine 的需求，那我們就不能像這樣直接的將 View engine 給移除，取而代之的是我們必需去調整 View engine 的順序，取比較好的載入順序。
