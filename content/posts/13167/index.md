---
title: "[Visual Studio]Visual Studio 2010 New Feature - Navigate To"
date: "2010-01-20 09:48:26"
description: "[Visual Studio]Visual Studio 2010 New Feature - Navigate To"
tags: [Visual Studio]
---

Visual Studio 2010新增Navigate To搜尋功能，能快速的搜尋資料。

使用上可透過[Edit]→[Navigate To…]
     
或是熱鍵Ctrl+,來啟用該功能。

啟用後，Visual Studio 2010會帶出Navigate To視窗

我們只要在Search terms下方的輸入格內，輸入我們欲查詢的字串即可。

當鍵入了預搜尋的字串，Navigate To在搜尋上會幫我們找出起始字串與搜尋字串相同的結果

或是字串中含有搜尋字串的結果

與單字開頭所構成的關鍵字為搜尋字串的結果

在搜尋字串的輸入上，我們也可以依需求把兩個以上的搜尋字串用空格隔開，做And搜尋。

搜尋完後選取想要的搜尋結果後，連點滑鼠左鍵，或是按下Ok按鈕，Visual Studio會幫我們把游標帶到對應的程式碼位置。

值得一提的是
  
在輸入Navigate To的搜尋字串時，需特別注意下列這些是不支援的：
     萬用字元。     Bool邏輯運算子，包括and、or、 &、 |。     正規表示式    

還有就是若關鍵字中含有大寫字串，則搜尋時會判斷大小寫。反之，則不會區分大小寫。

## Link
     Searching and Navigating Code in VS 2010 (VS 2010 and .NET 4.0 Series)     Tips: Using “Navigate To…” for search in Visual Studio     Walkthrough: Quick Search for Files and Symbols in Visual Studio 2010 (Lisa Feigenbaum)     How to: Search for Objects, Definitions, and References (Symbols)