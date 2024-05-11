---
title: "[C#]使用NetSparkle為應用程式加入自動更新機制"
slug: "[CSharp]使用NetSparkle為應用程式加入自動更新機制"
date: "2013-11-06 12:00:00"
description: "[C#]使用NetSparkle為應用程式加入自動更新機制"
tags: [CSharp]
---

<p>
	NetSparkle是從Mac的Sparkle移值而來的，一個號稱易於使用的自動更新開源框架。雖然號稱易於使用，但相關的文件真是少的可憐，實際使用上也令我卡關滿久的一個框架(它的類別成員與類別我真的無法一眼看懂它想要幹嘛...orz)。Anyway~這邊隨手做個簡單的整理與記錄。</p>
<p>
	 </p>
<p>
	使用前我們必須先將NetSparkle的組件加入參考，可以從官網NetSparkle - AutoUpdate for .NET Developer取得NetSparkle的組件後將之加入參考，或是直接透過NuGet加入參考也可以。</p>
<p>
	<img alt="image" border="0" height="431" src="\images\posts