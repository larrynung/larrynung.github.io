---
title: "[Visual Studio][C++]Inspect Header Includes with the /showIncludes Compiler Option"
slug: "visual-studio-cpp-inspect-header-includes-with-the-showincludes-compiler-option"
aliases: ["/posts/52278/"]
date: "2011-11-05 11:21:59"
description: "C++程式寫到後面，程式越寫越大，開發人員常會無法掌握每個Header實際Include的狀態，一不小心就會發生Redefine之類的錯誤。這時候我們可以開啟Visual Studio，打開專案屬性設定對話框，"
tags: [Visual Studio,C++]
---

C++程式寫到後面，程式越寫越大，開發人員常會無法掌握每個Header實際Include的狀態，一不小心就會發生Redefine之類的錯誤。這時候我們可以開啟Visual Studio，打開專案屬性設定對話框，切至[Configuratio Properties / C/C++ / Advanced]頁面，將[Show Includes]選項設為Yes (/showIncludes)。

![image_thumb.png](/images/posts/52278/image_thumb.png)

設定完後編譯，輸出視窗就會在編譯時顯示Header Include的狀態，像是下面這樣：

![image_thumb_1.png](/images/posts/52278/image_thumb_1.png)

需注意到的是，顯示出來的Header Include狀態，若巢狀Include則會在前面空一個空格，像是下面這個顯示的就是afxwin.h內有Include afx.h，afx.h內又有Include new.h。

```xml
1>  Note: including file:  C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\atlmfc\include\afxwin.h
1>  Note: including file:   C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\atlmfc\include\afx.h
1>  Note: including file:    C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\include\new.h
```

這個簡易的內建功能雖然不是很強大，但是對於在不裝額外工具去了解或是調整Header Include的順序，甚至是解決Redefine之類的問題，還滿實用的。

## Link

* /showIncludes (列示包含檔)
* VC++ Tip: Show Includes
