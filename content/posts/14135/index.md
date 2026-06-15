---
title: "[Visual Studio]Visual Studio 2010 New Feature - Zoom-In & Zoom-Out"
date: "2010-03-21 12:02:08"
description: "[Visual Studio]Visual Studio 2010 New Feature - Zoom-In & Zoom-Out"
tags: [Visual Studio]
---

在以往編輯程式，或臨時與別人討論程式時，若碰到字太小觀看不易，我們可以透過[Options]設定程式碼的顯示字型大小。

![image_thumb_3.png](/images/posts/14135/image_thumb_3.png)

或是透過預設的DecreaseTextEditorFontSize、與IncreaseTextEditorFontSize巨集，來調整編譯器的字型大小。

![image_thumb_2.png](/images/posts/14135/image_thumb_2.png)

這樣的做法使用動作繁瑣，而且是設定以後所有的顯示大小，若只是臨時有放大需求，在放大後仍需手動調回，使用上十分的不便。

在VS2010中利用了WPF的特性，提供了類似放大鏡的Zoom In與Zoom Out功能，有效的解決了這樣的問題。在VS2010程式碼編輯區的左下方，多了縮放比例的下拉選取工具，除了挑選的方式外，也提供手動輸入調整縮放比例。

![image_thumb.png](/images/posts/14135/image_thumb.png)

![image_thumb_1.png](/images/posts/14135/image_thumb_1.png)

也可以透過Ctrl+滑鼠上下捲動的方式，快速的Zoom In與Zoom Out。

Zoom In與Zoom Out顯示的效果是獨立的，每個檔案可以有各自的顯示比例，不像調整字型大小一樣是套用到整個環境。且該顯示效果是暫時的，當檔案關掉後再從方案總管叫起，系統會幫我們恢復到預設顯示比例。
