---
layout: post
title: "Visual Studio 14 CTP 3 - PerfTips in the Debugger"
date: 2014-08-24 00:11:00
comments: true
categories: [Visual Studio]
keywords: "Visual Studio"
description: "Visual Studio 14 CTP 3 - PerfTips in the Debugger"
---

PerfTips 是 Visual Studio 14 (CTP3 以後釋出)的新功能，能讓開發人員在除錯的同時了解程式的耗時與 CPU 的耗用。  

<!-- More -->

<br/>

以往我們為了觀測程式的耗時我們需要做程式碼的修改，用 Stopwatch 去監測。在 Visual Studio 14 CTP3 後，我們不需要修改程式就可以很輕易的監測程式的效能，只要透過 PerfTips 功能就可以了。  

<br/>

PerfTips 使用上很簡單，只要設定斷點進行除錯，看你是要 Step Into、Step Over、Step Out、或是直接 F5 跳到下一個斷點，PerfTips 都會自動在後面跳出上一步到這一步之間的耗時。  

{% img /images/posts/PerfTips/1.png %}

<br/>

預設這邊只有開啟耗時的部份，若要查閱 CPU 的耗費，我們可以將滑鼠移至 PerfTips 上面，彈出的 ToolTip 會有這方面的資訊。  

{% img /images/posts/PerfTips/2.png %}

<br/>


或者也可以點擊 PerfTips 叫出對應的選項設定。  

{% img /images/posts/PerfTips/3.png %}

<br/>


將 CPU 耗費的顯示給開啟，或是設定 PerfTips 要大於等於多少才顯示。  

{% img /images/posts/PerfTips/4.png %}

<br/>


{% img /images/posts/PerfTips/5.png %}

<br/>


Link
----
* [Visual Studio “14” CTP 3 Released - The Visual Studio Blog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/visualstudio/archive/2014/08/18/visual-studio-14-ctp-3-released.aspx)
* [PerfTips: Performance Information at-a-glance while Debugging with Visual Studio - Microsoft Application Lifecycle Management - Site Home - MSDN Blogs](http://blogs.msdn.com/b/visualstudioalm/archive/2014/08/18/perftips-performance-information-at-a-glance-while-debugging-with-visual-studio.aspx)
