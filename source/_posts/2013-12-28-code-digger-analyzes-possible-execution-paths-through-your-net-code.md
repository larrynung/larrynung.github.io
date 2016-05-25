---
layout: post
title: "Code Digger - Analyzes possible execution paths through your .NET code"
date: 2013-12-28 12:59:00
comments: true
categories: [Visual Studio]
keywords: Code Digger, Visual Studio
description: "Code Digger - Analyzes possible execution paths through your .NET code"
---

Code Digger 是精簡版的 Pex，其內部還是使用 Pex 的程式碼分析引擎，能將有意義的參數的抓出，幫助我們更了解程式，並找到可能的淺在問題。目前該擴充套件支援 Visual Studio 2010 以後的版本 (Visual Studio 2012、 Visual Studio 2013)，Visual Studio 2010 以前我們可以改使用功能更為強大的 Pex。  

<!-- More -->

Code Digger 在設立之初只支援 Protable Class Library ，故非 Protable Class Library 的專案在使用時會看到像下面這樣的訊息框。  

{% img /images/posts/CodeDigger/1.png %}


Code Digger 的功能也無法使用。  

但在某一版後，Code Digger 能在 Options 那邊將這限制關閉。只要開啟 Options 對話框，切換至 `Pex/General` 頁籤，將 `Code Digger` 群組下的 `DisableCodeDiggerPortableClassLibraryRestriction` 設定為 True 就可以了。  


{% img /images/posts/CodeDigger/2.png %}


使用時，我們只要在要分析的方法中按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中選取 `Generate Inputs / Outputs Table` 選單選項。  

{% img /images/posts/CodeDigger/3.png %}


接著會彈出 Code Digger Analytics 對話框，詢問是否同意 Code Digger 收集使用的資訊，這邊請視個人需求下去勾選就好，若有需要後續都可以至 Options 內做修改。  

{% img /images/posts/CodeDigger/4.png %}


點擊 `OK` 按鈕將之關閉，分析的結果就會在 `Inputs / Outputs` 工具視窗中顯示。  

{% img /images/posts/CodeDigger/5.png %}


可以在這邊清楚的看到帶入的值、方法的回傳值、是否有例外、以及錯誤訊息...等等。可藉由這些資訊判定該方法是否有可能造成不如我們預期的結果。  


Link
----
* [Code Digger - Microsoft Research](http://research.microsoft.com/en-us/projects/codedigger/)
* [Microsoft Code Digger extension - Visual Studio Gallery](http://visualstudiogallery.msdn.microsoft.com/fb5badda-4ea3-4314-a723-a1975cbdabb4)
* [The Code Digger - CodeProject](http://www.codeproject.com/Tips/650193/The-Code-Digger)
* [Using Pex and Microsoft Code Digger to Better Understand and Test Your Code](http://www.codeproject.com/Articles/583520/UsingplusPexplusandplusMicrosoftplusCodeplusDigger)
