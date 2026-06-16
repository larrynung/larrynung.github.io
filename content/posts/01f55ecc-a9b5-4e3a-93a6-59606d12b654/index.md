---
title: "[Visual Studio]Build Reusable Cross-Platform Assemblies with the Portable Class Library Template"
slug: "visual-studio-build-reusable-cross-platform-assemblies-with-the-portable-class-library-template"
aliases: ["/posts/01f55ecc-a9b5-4e3a-93a6-59606d12b654/"]
date: "2013-11-06 12:00:00"
tags: [Portable Class Library, Visual Studio]
description: "近年隨著科技的進步，很多人手邊都有多個裝置，也許是WP7、也許是桌機、筆電、XBox...，這是個美好的時代，行動計算無所不在，生活充滿了更多的便利性。但這樣的時代卻苦了程式開發人員，同樣的程式往往開發人員必須在各個裝置上建置，就像是一個好的App，能讓使用者高度的黏在App上，"
---

近年隨著科技的進步，很多人手邊都有多個裝置，也許是WP7、也許是桌機、筆電、XBox...，這是個美好的時代，行動計算無所不在，生活充滿了更多的便利性。但這樣的時代卻苦了程式開發人員，同樣的程式往往開發人員必須在各個裝置上建置，就像是一個好的App，能讓使用者高度的黏在App上，桌機有使用者就會想要手機也能用，手機有就會想要桌機也能用，就是因為這樣開發人員往往必須要在各個平台撰寫相同的功能，每個平台可能就開了一個專案，不僅開發時程變長，連維護的成本也跟著變高。

好在貼心的微軟又注意到了，微軟在Visual Studio中提供了Portable Class library的樣板來解決這樣的問題，這個樣版能讓開發人員指定我們想要套用在哪些平台上面，進而限制能使用到的功能，因此在開發上只能用平台共用的組件來完成，寫出來的組件就能在各平台重用。

Portable Class library在Visual Studio 11中是內建的，Visual Studio 2010上要使用必須先安裝SP1，再到Portable Library Tools下載來安裝，就可以在Visual Studio 2010中使用了。

Portable Class library樣板在使用上很簡單，只要建立專案時選取Portable Class library當作開發的樣板。

![image_thumb.png](/images/posts/01f55ecc-a9b5-4e3a-93a6-59606d12b654/image_thumb.png)

然後切換置專案屬性去設定Target frameworks，決定開發的組件要支援哪些平台。

![image_thumb_2.png](/images/posts/01f55ecc-a9b5-4e3a-93a6-59606d12b654/image_thumb_2.png)

這邊內建有.NET Framework 4、Silverlight 4、Windows Phone 7、與Xbox 360可以選擇，如果開發環境是Visual Studio 11的話，會有更多的平台可以選擇使用。

![image_thumb_3.png](/images/posts/01f55ecc-a9b5-4e3a-93a6-59606d12b654/image_thumb_3.png)

選取的平台會影響到專案能加入參考的組件，開發環境會過濾出能被共用的組件給我們加入參考，像下圖所示，我們可以看到本來在一般專案範本時應該可以看到很多的.NET組件，變得只有少少的幾個。

![image_thumb_4.png](/images/posts/01f55ecc-a9b5-4e3a-93a6-59606d12b654/image_thumb_4.png)

## Link

* Portable Class Library in .NET
* Create a Continuous Client Using Portable Class Libraries
* Portable Class Libraries: A Primer
* Portable Class Libraries
* Portable Library Tools
