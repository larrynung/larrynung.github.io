---
title: "Visual Studio 2015 - New Breakpoint Configuration Experience"
date: "2015-02-05 08:32:00"
description: "Visual Studio 2015 - New Breakpoint Configuration Experience"
tags: [Visual Studio]
---


Visual Studio 2015 在除錯功能上做了一些改進，其中一項就是 New Breakpoint Configuration Experience。  

<!-- More -->

<br/>

以往在設定中斷點時，中斷點的設定視窗是彈跳出來的，設定時要參考程式碼不易，且各個設定雖然可以合併使用但卻是分開的設定視窗。Visual Studio 2015 將之做了個調整，使用類似 Peek Definition 的作法，並將設定整合，讓設定可在一個地方一次設完且一目了然。    

<br/>


使用上只要將滑鼠移至斷點之上，按下浮現的設定按鈕。  

{% img /images/posts/NewBreakpointExperienceInVS2015/1.png %}

<br/>


類似 Peek Definition 的設定視窗會跑出來，可看到之前的設定都在這邊可以一次設完，像是 Hit Condition 與 Count Condition。  

{% img /images/posts/NewBreakpointExperienceInVS2015/2.png %}

<br/>


追蹤點的設定也不例外。  

{% img /images/posts/NewBreakpointExperienceInVS2015/3.png %}

<br/>


因為是用嵌入的方式去做設定，所以設定完在除錯時若有需要，檢視上也比較容易。  

{% img /images/posts/NewBreakpointExperienceInVS2015/4.png %}

<br/>


Link
----
* [Debugging Improvements in Visual Studio 2015 | Visual Studio Toolbox | Channel 9](http://channel9.msdn.com/Shows/Visual-Studio-Toolbox/Debugging-Improvements-in-Visual-Studio-2015)
* [New Breakpoint Configuration Experience in Visual Studio 2015 - Microsoft Application Lifecycle Management - Site Home - MSDN Blogs](http://blogs.msdn.com/b/visualstudioalm/archive/2014/10/06/new-breakpoint-configuration-experience.aspx)
