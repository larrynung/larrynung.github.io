---
title: "[Software]TortoiseGit的TGitCache佔用過多的CPU"
date: "2013-11-06 12:00:00"
description: "[Software]TortoiseGit的TGitCache佔用過多的CPU"
---

今天在測試程式運作時發現整個系統效能有點低落，看了一下工作管理員發現有個TGitCache.exe的處理續在吃我的CPU，吃的量還滿大的，在雙核的情況下還能吃到25%左右。

此時我沒有除了在除錯外並沒有在做什麼特別跟Git有關的操作，因此這問題有必要好好的看一下。查了一下tortoisegit是現有的問題，這問題在另一套SVN筆者也碰到過，那時也是有個另外的處理緒在背後更新，把CPU吃夠夠。

碰到這個問題的話可到Settings內的Icon Overlays頁面，視個人需求將Status cache設定為Shell或是None，這樣設定也許檔案總管瀏覽時狀態圖示的顯示會不夠即時，但卻能解決吃CPU的問題。
     

  
## Link
     Issue 48:    High CPU usage during TGitCache process of large repositories    Issue 980:    100% CPU with TGitCache in Windows 7 "Libraries" folder