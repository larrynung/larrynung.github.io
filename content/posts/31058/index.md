---
title: "[Software]Sync Google Calendar with Rainlendar Using GCALDaemon"
slug: "software-sync-google-calendar-with-rainlendar-using-gcaldaemon"
aliases: ["/posts/31058/"]
date: "2011-07-05 01:34:37"
description: "Rainlendar日曆是目前用過的桌面日曆最為上手的一套軟體，付費專業版本具備同步Google日曆的功能，但是免費版本卻無此功能，因此裝了幾次到頭來最後都還是把它給移掉了。"
tags: [Software]
---

Rainlendar日曆是目前用過的桌面日曆最為上手的一套軟體，付費專業版本具備同步Google日曆的功能，但是免費版本卻無此功能，因此裝了幾次到頭來最後都還是把它給移掉了。

最近又將他裝了起來，回頭再去看了一次同步上的問題，找到了GCALDaemon這套同步軟體能達到我的需求，這邊將怎樣使用GCALDaemon做Google日曆跟Rainlendar的同步做個簡單的紀錄。

要使用GCALDaemon做Google日曆跟Rainlendar的同步，首先我們必須要至GCALDaemon網站上下載GCALDaemon這套軟體。

![image_thumb.png](/images/posts/31058/image_thumb.png)

GCALDaemon在設定上可手動對設定檔做設定，也可使用Config Editor介面去做設定，這邊我以較為簡單的Config Editor下去介紹。

GCALDaemon安裝完後執行Config Editor設定同步的帳號，切至File synchronizer頁面，先將file-base calendar synchronizer選項打勾。

![image3_thumb.png](/images/posts/31058/image3_thumb.png)

接著按下右下方的Google Accounts設定Google帳號。

![image9_thumb.png](/images/posts/31058/image9_thumb.png)

Google帳號設定完後按下右下方的New按鈕，會彈出Google Calendar Synchronization對話框，這邊是用來做同步的設定，選取要同步的Google帳號，選取Google帳號上面所要同步的日曆，並指定同步的iCal檔案位置。

![image_thumb_10.png](/images/posts/31058/image_thumb_10.png)

都設定完後存檔離開，可以先按下開始功能表內的Sync Now!進行同步測試，看看在剛剛設定的指定位置是否會產生同步的檔案。若運作正常，此時我們可以點選開始功能表內的Install，將同步的服務安裝至本機中。

![image_thumb_4.png](/images/posts/31058/image_thumb_4.png)

![image_thumb_9.png](/images/posts/31058/image_thumb_9.png)

GCALDaemon同步的部分設定完後，接著設定Rainlendar同步的部分，在Rainlendar上方點選滑鼠右鍵，點選[選項...]。

![image_thumb_2.png](/images/posts/31058/image_thumb_2.png)

將之切換至行事曆頁面，點選[增加...]設定新的行事曆。

![image_thumb_12.png](/images/posts/31058/image_thumb_12.png)

![image_thumb_5.png](/images/posts/31058/image_thumb_5.png)

新增時要注意ICS檔案需指定剛剛在GCALDaemon那邊所設定的同步日曆檔案。

![image_thumb_6.png](/images/posts/31058/image_thumb_6.png)

![image_thumb_7.png](/images/posts/31058/image_thumb_7.png)

日曆新增完後記得要勾選其[監視變更]屬性，這邊也可以透過[顯示分類]屬性去設定該行事曆的內容是屬於哪種分類。

![image_thumb_8.png](/images/posts/31058/image_thumb_8.png)

## Link

* Google日曆與Rainlendar行事曆同步
* GCALDaemon
* GCALDaemon - User's Guide
* 利用GCALDaemon來同步我的Google日曆與桌面日曆Rainlendar
* [教學] 在Windows裡安裝/設置Rainlendar與Google Calendar同步
