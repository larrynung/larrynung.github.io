---
title: "Visual Studio 2015 - New Exception Settings Window"
date: "2015-07-11 11:40:00"
description: "Visual Studio 2015 - New Exception Settings Window"
tags: [Visual Studio]
---


在使用 Visual Studio 對 .NET 程式進行除錯時，有時候我們會需要對 Exception Setting 進行些調整，以便快速的找出問題發生的點。  

<!-- More -->

<br/>


但是以往的 Exception Setting 是以對話框形式呈現，開關設定十分的不便，且不具搜尋過濾的功能，要找到指定的設定很不容易。  

<br/>


這樣的問題在 Visual Studio 2015 獲得了改善，Exception Setting 改以 Window 方式呈現能方便我們隨時進行調動，也新噌了搜尋與過濾的功能便於快速找到指定的設定。    

<br/>  


舉個例子來說，今天我們的程式碰到了個不如預期的問題，我們的程式會被導到例外被攔截的位置。  

{% img /images/posts/ExceptionSettingWindowInVS2015/1.png %}

<br/>


但例外被攔截的位置並非我們所關注的地方，此時我們會調整 Exception Setting 讓 `Common Language Runtime Exceptions` 設定被勾選，這樣因為可以攔截到 First chance exception，所以程式會改停在錯誤實際發生的位置。  

{% img /images/posts/ExceptionSettingWindowInVS2015/2.png %}

<br/>


若要細部指定特定的例外，像是 NullReferenceException，可以直接透過搜尋找到對應的設定。   

{% img /images/posts/ExceptionSettingWindowInVS2015/3.png %}

<br/>


針對非系統提供的例外，這邊也允許自行加入設定。  

{% img /images/posts/ExceptionSettingWindowInVS2015/4.png %}

<br/>


Link
----
* [The New Exception Settings Window in Visual Studio 2015 - Microsoft Application Lifecycle Management - Site Home - MSDN Blogs](http://blogs.msdn.com/b/visualstudioalm/archive/2015/02/23/the-new-exception-settings-window-in-visual-studio-2015.aspx)
* [Understanding Exceptions while debugging with Visual Studio - Microsoft Application Lifecycle Management - Site Home - MSDN Blogs](http://blogs.msdn.com/b/visualstudioalm/archive/2015/01/08/understanding-exceptions-while-debugging-with-visual-studio.aspx)
