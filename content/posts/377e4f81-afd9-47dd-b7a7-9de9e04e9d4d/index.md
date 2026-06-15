---
title: "[網樂通改機][sh4twbox]安裝並啟動ushare，讓網樂通支援DLNA"
date: "2013-11-06 12:00:00"
description: "[網樂通改機][sh4twbox]安裝並啟動ushare，讓網樂通支援DLNA"
---

網樂通改機成功後，若想要讓網樂通支援DLNA，我們可以為網樂通加掛ushare server。這篇稍微紀錄一下要怎樣才能透過sh4twbox為網樂通加掛ushare server。

首先我們必須連進網樂通，並參閱[網樂通改機][sh4twbox]如何使用shpkg去做套件的安裝與管理這篇，或是直接呼叫命令"shpkg -S ushare"，將ushare套件安裝起來。

![image_thumb_2.png](/images/posts/377e4f81-afd9-47dd-b7a7-9de9e04e9d4d/image_thumb_2.png)

接著我們必須要呼叫命令"vi /etc/ushare.conf"做些設定，像是DLNA的DMS Server要叫什麼名字、哪個目錄下的資料要放進DMS Server去共享...等等。

![image_thumb_3.png](/images/posts/377e4f81-afd9-47dd-b7a7-9de9e04e9d4d/image_thumb_3.png)

這邊按下i進入編輯模式，我們可以將USHARE_NAME部分改為自己想要的DLNA Server名稱，不改也可以他預設會是uShare。另外要改的是USHARE_DIR，這邊是DMS Server會分享出來的位置，可以指定BT下載的目錄之類的。

![image_thumb_4.png](/images/posts/377e4f81-afd9-47dd-b7a7-9de9e04e9d4d/image_thumb_4.png)

最後可能需要調整的設定就是USHARE_OVERRIDE_ICONV_ERR，若是檔案可能是中文或日文聽說要設成yes。

![image_thumb_5.png](/images/posts/377e4f81-afd9-47dd-b7a7-9de9e04e9d4d/image_thumb_5.png)

設定完後我們可以呼叫"/etc/init.d/ushare start"將服務啟動，啟動成功會像下圖一樣告知"START OK"。

![image_thumb_6.png](/images/posts/377e4f81-afd9-47dd-b7a7-9de9e04e9d4d/image_thumb_6.png)

服務啟動後實際來測試一下DLNA的功能，這邊先將一些圖檔透過網芳複製進網樂通以方便後續測試。

![image_thumb_7.png](/images/posts/377e4f81-afd9-47dd-b7a7-9de9e04e9d4d/image_thumb_7.png)

開啟MediaPlayer，可以在左側看到有找到網樂通的DMS Server，點選圖片可以看到剛剛丟進去的圖片也確實可以透過DLNA瀏覽。

![image_thumb_8.png](/images/posts/377e4f81-afd9-47dd-b7a7-9de9e04e9d4d/image_thumb_8.png)

最後這邊要再提醒一下，像上面這樣啟動沒問題後，若是希望每次網樂通通電就可以使用這樣的功能，我們必須要參閱[網樂通改機]網樂通運行時自動啟動指定的服務這篇，將要啟動的命令寫在/etc/rc.local裡面。

![image_thumb_9.png](/images/posts/377e4f81-afd9-47dd-b7a7-9de9e04e9d4d/image_thumb_9.png)
