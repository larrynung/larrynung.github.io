---
title: "[.NET Resource][Visual Studio]使用BatchFormat批次整理程式碼的Format與Using"
date: "2013-11-06 12:00:00"
description: "[.NET Resource][Visual Studio]使用BatchFormat批次整理程式碼的Format與Using"
---

BatchFormat是Visual Studio的extension，可以輔助開發人員批次整理程式代碼的Format與Using。

使用前需先透過Extension Manager將BatchFormat安裝起來。

安裝後將Visual Studio重新啟動，我們可以在方案總管上的滑鼠右鍵選單中看到多出了BatchFormat的選單選項，透過裡面的功能我們可以針對整個方案、整個專案、或是單一檔案進行程式碼Format與Using的整理(取決於在方案總管上的哪個位置中開啟右鍵選單)。

運行的結果我們可以在輸出視窗查閱，像是處理了那些檔案，花費了多少時間等等。

若是有某些檔案想要忽略不予以整理，可在Options中設定要忽略的檔案結尾字串。

## Link
     BatchFormat    我的第一個開源VS2010擴展：BatchFormat    BatchFormat – Remove Unused ‘Usings’ And Format Visual Studio Document