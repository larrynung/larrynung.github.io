---
title: "使用Visual Studio International Pack做資源檔的簡繁轉換"
date: "2013-11-06 12:00:00"
description: "使用Visual Studio International Pack做資源檔的簡繁轉換"
---

Visual Studio International Pack 是微軟提供用來建立全球化的應用程式的類別庫。其內含Visual Studio的Add-In，能讓Visual Studio快速的把資源檔作簡繁轉換 。

  使用上我們需先到微軟下載中心下載Microsoft Visual Studio International Pack 1.0。     

解壓縮後安裝CHTCHSConv.msi。

安裝好後我們可在方案總管上的資源檔上按右鍵，會多個轉換的選項。若要從繁體資源檔轉到簡體資源檔，可點選[From Traditional to Simplified Chinese]。轉換後會在方案總管上多個簡體的資源檔，若是本來已有資源檔則檔案會被覆蓋。

若要從簡體資源檔轉到繁體資源檔，可點選[From Simplified to Traditional Chinese]。

若在檔名明確指出非簡繁語系的資源檔上按右鍵，則轉換選單內的選項會被Disable。

而在檔名沒有指定語系的資源檔上按右鍵，由於Add-In無法判定該資源檔是繁體還是簡體，因此轉換選單內的選項都會被Enable。

另外讀我檔案內有提到這個Add-In已知的問題，詳情可以參閱Visual Studio International Pack 1.0 讀我檔案。

## Link
     Microsoft Visual Studio International Pack 1.0 SR1 版