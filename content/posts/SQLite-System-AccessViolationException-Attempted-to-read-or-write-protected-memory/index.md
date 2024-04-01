---
title: ">-"
date: "2016-11-04 13:48:08"
tags: [SQLite]
---


最近在使用 SQLite 讀取資料時，程式運行出現了 `System.AccessViolationException: Attempted to read or write protected
  memory` 這樣的訊息。  

<!-- More -->

![1.png](1.png)

<br/>


反覆查驗後發現因為目錄有個殘留的 SQLite.Interop.dll 這個檔案所導致，將此檔刪除即可正常運作。  

![2.png](2.png)

<br/>
