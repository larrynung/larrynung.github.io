---
layout: post
title: "Code Analysis Error CA0058"
date: 2015-09-18 14:45
comments: true
categories: 
keywords: 
description: "Code Analysis Error CA0058"
---

最近抽空把開發中的專案設定了一下 Code Analysis，運行時發生了 CA0058 這個錯誤。  

<!-- More -->

<br/>


{% img /images/posts/CA0058/1.png %}

<br/>


要解決這個問題，在 Visual Studio 2012 以前可以修改 FxCopCmd.exe.config。位置在

    C:\Program Files (x86)\Microsoft Visual Studio 11.0\Team Tools\Static Analysis Tools\FxCop\FxCopCmd.exe.config

<br/>


{% img /images/posts/CA0058/2.png %}

<br/>


實際位置需視 Visual Studio 版本或是安裝位置下去調整。  

<br/>


將之開啟找到 AssemblyReferenceResolveMode 的值改為 StrongNameIgnoringVersion。  

{% img /images/posts/CA0058/3.png %}

<br/>


Visual Studio 2012 後我們要開啟專案檔進行編輯，在第一個 PropertyGroup 中加入 CodeAnalysisAdditionalOptions，將其設為 /assemblyCompareMode:StrongNameIgnoringVersion。  

{% codeblock lang:xml %}
...
<PropertyGroup>
  ...
  <CodeAnalysisAdditionalOptions>/assemblyCompareMode:StrongNameIgnoringVersion</CodeAnalysisAdditionalOptions>
  ...
</PropertyGroup>
...
{% endcodeblock %}


{% img /images/posts/CA0058/4.png %}

<br/>


這樣設完問題應該就解決了。  

<br/>


Link
----
* [c# - Visual Studio 2012 Code Analysis Error CA0058 - Stack Overflow](http://stackoverflow.com/questions/26058751/visual-studio-2012-code-analysis-error-ca0058)
* [c# - Using Microsoft.Bcl.Async with Code Analysis causes errors - Stack Overflow](http://stackoverflow.com/questions/17298281/using-microsoft-bcl-async-with-code-analysis-causes-errors/17935400#17935400)
