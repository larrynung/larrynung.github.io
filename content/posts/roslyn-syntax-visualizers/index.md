---
title: "Roslyn Syntax Visualizers"
date: "2014-10-05 23:23:00"
description: "Roslyn Syntax Visualizers"
tags: [Roslyn, Visual Studio]
---


在使用 Roslyn 做開發時，常免不了會要去處理語法的解析，這時我們會需要輔助工具將語法解析轉換為語法樹，以視覺的方式呈現，讓 Roslyn 的開發上更為便利。  

<!-- More -->

<br/>

所以開發前我們要到 [.NET Compiler Platform Syntax Visualizer extension](http://visualstudiogallery.msdn.microsoft.com/70e184da-9b3a-402f-b210-d62a898e2887) 這邊下載 Roslyn Syntax Visualizer。  

{% img /images/posts/RoslynSyntaxVisualizer/1.png %}

<br/>


下載完後進行安裝。  

{% img /images/posts/RoslynSyntaxVisualizer/2.png %}

<br/>


{% img /images/posts/RoslynSyntaxVisualizer/3.png %}

<br/>


安裝完我們可以透過 Visual Studio 的主選單選項(View\Other Windows\Roslyn Syntax Visualizer)將 Roslyn Syntax Visualizer Tool Window 叫出。  

{% img /images/posts/RoslynSyntaxVisualizer/4.png %}

<br/>


叫出後 Roslyn Syntax Visualizer 後，它會偵測目前所編輯的程式碼，將之解析成語法樹。且會偵測編輯區的選取，反映在語法樹上。  

{% img /images/posts/RoslynSyntaxVisualizer/5.png %}

<br/>


反之亦然。 

{% img /images/posts/RoslynSyntaxVisualizer/6.png %}

<br/>


語法樹上的節點有做顏色的區分，可以透過上方的 Legend 按鈕查閱各顏色所代表的意義。  

{% img /images/posts/RoslynSyntaxVisualizer/7.png %}

<br/>


語法樹上節點的滑鼠右鍵快顯選單也有提供一些功能，像是可以用更直覺的圖形方式呈現。    

{% img /images/posts/RoslynSyntaxVisualizer/8.png %}
 
<br/>


Link
----
* [.NET Compiler Platform Syntax Visualizer extension](http://visualstudiogallery.msdn.microsoft.com/70e184da-9b3a-402f-b210-d62a898e2887)
* [.NET Compiler Platform ("Roslyn") - Documentation](https://roslyn.codeplex.com/wikipage?title=Syntax%20Visualizer)
* [Roslyn Syntax Visualizers - The Visual Studio Blog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/visualstudio/archive/2011/10/19/roslyn-syntax-visualizers.aspx)
