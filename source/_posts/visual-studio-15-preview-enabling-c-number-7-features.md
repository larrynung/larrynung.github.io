---
layout: post
title: "Visual Studio 15 Preview - Enabling C# 7 Features"
date: 2016-04-26 21:57:00
comments: true
tags: [Visual Studio]
keywords: "Visual Studio"
description: "Visual Studio 15 Preview - Enabling C# 7 Features"
---

Visual Studio 15 Preview 開始支援部分 C# 7.0 的功能，由於尚未完全定案，故並未直接開放，需要做些特別的設定才可將之開啟。  

<!-- More -->

<br/>


若要啟用需切打開專案的屬性頁，切至建置頁面，在條件式編譯的符號那邊設定 `__DEMO__,__DEMO_EXPERIMENTAL__` 即可。  

{% img /images/posts/VS15PreviewEnableCSharp7/1.png %}

<br/>

Link
----
* [Enabling C# 7 Features in Visual Studio “15” Preview | StrathWeb. A free flowing web tech monologue.](http://www.strathweb.com/2016/03/enabling-c-7-features-in-visual-studio-15-preview/)
