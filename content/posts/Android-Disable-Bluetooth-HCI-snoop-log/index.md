---
title: "Android - Disable Bluetooth HCI snoop log"
date: "2019-03-19 22:54:20"
tags: [Android]
---


如果 Android 手機空間莫名大量變少，可確認一下手機內是否有 btsnoop_hci.log 這個檔案。  
  
<!-- More -->

![1.jpg](1.jpg)

<br/>


如果確實手機空間是被該檔佔用，我們可以開啟手機的設定。  

![2.jpg](2.jpg)

<br>


進到開發人員選項。 

![3.jpg](3.jpg)

<br/>


將 "啟用藍芽 HCI 窺探紀錄" 選項關閉。 

![4.jpg](4.jpg)

<br/>


系統就不會再因為寫入該檔案而吃掉大量手機空間。  
