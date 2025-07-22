---
title: "[Visual Studio]Visual Studio 2010 New Feature - Reference Highlight"
date: "2010-01-21 09:43:12"
description: "[Visual Studio]Visual Studio 2010 New Feature - Reference Highlight"
tags: [Visual Studio]
---

Highlight Reference是Visual Studio 2010新增的貼心小功能，能幫我們快速的找到程式中參考到的地方，並提供快速的巡覽。

	使用上只要用滑鼠在想要找參考的類別、方法、屬性…等成員上點選，讓滑鼠焦點移至該處。過一會Visual Studio 2010就會幫你把參考到的地方給高亮度標記，就像下面這樣：

	此時我們可以透過熱鍵Ctrl+Shift+DownArrow向下快速巡覽

	也可以透過熱鍵Ctrl+Shift+UpArrow向上快速巡覽

	有點像是CodeRush的Tab與Shift+Tab的功能。

	若要關閉該功能，可點選[Tools]→[Options]→[Text Editor]去設定。VB.NET的使用者可點選[Basic]→[VB Specific]，並取消勾選Enable highlight of reference keywords。

	C#的使用者可點選[C#]→[Advanced]，並取消勾選Highlight reference to symbol under cursor。