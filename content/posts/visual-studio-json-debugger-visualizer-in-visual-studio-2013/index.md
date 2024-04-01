---
title: "Visual Studio - JSON Debugger Visualizer in Visual Studio 2013"
date: "2014-02-08 22:08:00"
description: "Visual Studio - JSON Debugger Visualizer in Visual Studio 2013"
tags: [Visual Studio]
---


以往我們在做 JSON 資料的除錯時，若是不加裝外掛， 在 Visual Studio 上只能透過純文字模式下去檢視。不易查閱與驗證，若資料是非 Format 過的，則更是麻煩。

<!-- More -->

Visual Studio 2013 Update 2 CTP 後 Visual Studio 加入了 JSON Debugger Visualizer 功能。透過這個功能，能有效的解決這樣的困擾。

它提供了較為友善的除錯界面，將 JSON 資料展開用樹狀結構呈現。不管是否是 Format 過的資料，都是一樣的呈現方式。

{% img /images/posts/JSONDebugVisualizer/1.png %}

<br/>

{% img /images/posts/JSONDebugVisualizer/2.png %}

<br/>

透過樹狀結構的呈現方式， JSON Debugger Visualizer 清楚的表達了 JSON 資料的階層性與其值。

若是 JSON 內資料多到不易找尋，它也提供了搜尋的功能，能輔助我們快速的從 JSON 資料中找出感興趣的部分...  

{% img /images/posts/JSONDebugVisualizer/3.png %}

<br/>

找到感興趣的資料後，若有需要我們可以在上面按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中有提供一些複製的功能，像是複製該資料的路徑、Key、Value、或是 Key 跟 Value 一起複製。

{% img /images/posts/JSONDebugVisualizer/4.png %}

<br/>

最後一提，要是這邊所查閱的資料是非 JSON 格式的，或是格式有誤。 JSON Debugger Visualizer 會改以純文字的方式呈現，並告知我們該資料不是 JSON 格式。

{% img /images/posts/JSONDebugVisualizer/5.png %}

<br/>

Link
----
* [JSON Debugger Visualizer in Visual Studio 2013 - Microsoft Application Lifecycle Management - Site Home - MSDN Blogs](http://blogs.msdn.com/b/visualstudioalm/archive/2014/02/06/json-debugger-visualizer-in-visual-studio-2013.aspx)
