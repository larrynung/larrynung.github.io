---
layout: post
title: "Mefx - MEF Composition Analysis Tool"
date: 2014-03-16 23:20
comments: true
categories: MEF
keywords: "MEF, Mefx, Tool"
description: "Mefx - MEF Composition Analysis Tool"
---

Mefx 是一用來分析與診斷 MEF 錯誤的命令列工具。當 MEF 在運作上不如預期時，我們可藉由此工具下去做些查驗。 

<!-- More -->

程式主檔可至 [Managed Extensibility Framework - Download: MEF Analysis Tool (mefx) for .NET 4.0 Beta](http://mef.codeplex.com/releases/view/33536) 這邊下載。  

{% img /images/posts/Mefx/1.png %}

<br/>

命令列的使用語法如下：  

    mefx [files and directories] [action] [options]

<br/>

使用時首先要帶入 /file 或是 /dir 參數，並指定要進行分析的檔案或目錄。

    mefx /file:MyAddIn.dll /directory:Program\AddIns [action...]

<br/>

接著視需要加入其它參數。像是在後面帶入 /parts 參數用以查閱組件內內含哪些可以使用的 part。

    mefx /file:MyAddIn.dll /parts

<br/>

帶入 /type 查閱特定的 part。 

    mefx /file:MyAddIn.dll /type:MyAddIn.AddIn 

<br/>

或是帶入 /imports 查閱 import 點。  

    mefx /file:MyAddIn.dll /imports

<br/>

帶入 /exports 查閱 export 點。

    mefx /file:MyAddIn.dll /exports

<br/>

帶入 /verbose 顯示更為詳細的資訊。

    mefx /file:MyAddIn.dll /parts /verbose

<br/>

Link
----
* [撰寫分析工具 (Mefx)](http://msdn.microsoft.com/zh-tw/library/ff576068(v=vs.110).aspx)
* [Managed Extensibility Framework - Download: MEF Analysis Tool (mefx) for .NET 4.0 Beta](http://mef.codeplex.com/releases/view/33536)
