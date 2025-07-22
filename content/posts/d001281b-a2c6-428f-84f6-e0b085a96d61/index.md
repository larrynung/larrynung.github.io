---
title: "MongoDB服務因發生exception in initAndListen_ 12596 old lock file錯誤導致無法啟動的解決方案"
date: "2013-11-06 12:00:00"
description: "MongoDB服務因發生exception in initAndListen_ 12596 old lock file錯誤導致無法啟動的解決方案"
---

最近我的虛擬機器在啟動MongoDB Service時都無法正常啟動，每次啟動都會發生1067的錯誤。

查閱MongoDB的Log檔發現裡面有"exception in initAndListen: 12596 old lock file, terminating"這樣的一個訊息，直覺就是問題所在。

因此上網查了一下，找到了修復的方法，大致來說就是要把殘留的MongoDB.lock給刪掉，或是運行mongod.exe --repair進行修復，然後再次運行服務即可。這邊筆者實際查閱了一下MongoDB.lock檔，發現它在Service運行時會大於0 KB，但是停止Service時會變為0 KB，而在筆者無法啟動的虛擬電腦中Service啟動不了，但是MongoDB.lock卻大於0 KB，裡面的內容也只是個看不懂的數字。

筆者將這個殘留的MongoDB.lock檔殺掉後再次啟動這問題就修復了，很顯然的MongoDB在這塊在某些情況下會沒處理乾淨。

## Link
     mongodb exception in initAndListen: 12596 old lock file, terminating解决方法     MongoDB非正常关闭后修复记录