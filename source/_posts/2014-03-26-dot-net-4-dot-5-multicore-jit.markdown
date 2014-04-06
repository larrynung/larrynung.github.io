---
layout: post
title: ".NET 4.5 - Multicore JIT"
date: 2014-03-26 23:33
comments: true
categories: [CSharp, JIT]
keywords: "Multicore, JIT"
description: ".NET 4.5 - Multicore JIT"
---

以往我們的程式要增快啟動速度時，我們會使用 ngen 去產生原生映像檔，讓程式運行時改運行預先編譯過的原生映像檔，以減少 JIT 編譯的耗費。   

<!-- More -->

<br/>

然而 ngen 這種改善方案只適用於某些情境下，像是有安裝包的部署。並不是所有的情境都可以套用 ngen 這種改善方案。故在 .Net Framework 4.5 出現了 Multicore JIT 的概念，以並行編譯的方式來提升程式的啟動速度，預期可加速約 20% - 50% 。  

微軟官方也有提供一些比較數據可供參考。  

{% img /images/posts/MultiCoreJIT/1.png %}

<br/>

{% img /images/posts/MultiCoreJIT/2.png %}

<br/>

Multicore JIT 的運作原理主要是將運行分為兩種 Mode。一個是 Recording mode，於程式第一次運行時啟動，會將跟 Compile 要求的編譯紀錄到指定的 Profile 檔案。

{% img /images/posts/MultiCoreJIT/3.png %}

<br/>

一個是 Plackback mode，會依照 Recording mode 所紀錄的 Profile 用另外一個 CPU 下去在背景編譯。  

{% img /images/posts/MultiCoreJIT/4.png %}

<br/>

以程式面來說，Asp.Net 4.5 與 Silverlight 5 這邊會自動啟用 Multicore JIT 功能，不需要做什麼特別的設定，如果有需要也可以修改 web.config 去將之關閉。  

{% codeblock lang:xml %}
<system.web> 
  <compilation profileGuidedOptimizations="None" />
</system.web>
{% endcodeblock %}

<br/>

如果是非 Asp.Net 4.5 與 Silverlight 5 的程式，像是 Window Form 程式之類的則要手動啟用，需埋入兩行程式。  

{% codeblock lang:c# %}
 ProfileOptimization.SetProfileRoot(@"C:\MyAppFolder");
 ProfileOptimization.StartProfile("Startup.Profile");
{% endcodeblock %}

<br/>

用以告知 JIT profile 的存放目錄以及觸發啟用。

<Br/>

Link
----
* [CLR 4.5: Multicore Just-in-Time (JIT) | eknowledger](http://eknowledger.wordpress.com/2012/04/26/clr-4-5-multicore-just-in-time-jit/)
* [An easy solution for improving app launch performance - .NET Blog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/dotnet/archive/2012/10/18/an-easy-solution-for-improving-app-launch-performance.aspx)
* [ProfileOptimization Class (System.Runtime)](http://msdn.microsoft.com/en-us/library/system.runtime.profileoptimization%28v=vs.110%29.aspx)
