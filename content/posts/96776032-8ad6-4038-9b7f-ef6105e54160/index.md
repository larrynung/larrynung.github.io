---
title: "Managing AVDs with AVD Manager"
date: "2013-11-06 12:00:00"
description: "Managing AVDs with AVD Manager"
---

想要開發APP，不論是Android、IPhone、Window Phone...，模擬器的使用都很重要。

以Android來說，我們必須要先熟悉AVD Manager的操作。可透過上方的ToolBar去啟動AVD Manager(Andorid Virtual Device Manager)。

![image_thumb_7.png](/images/posts/96776032-8ad6-4038-9b7f-ef6105e54160/image_thumb_7.png)

或是透過上方工具列的[Window/Android Virtual Device Manager]選單選項去啟動。

![image_thumb_9.png](/images/posts/96776032-8ad6-4038-9b7f-ef6105e54160/image_thumb_9.png)

AVD Manager啟動後會像下面這樣，會有兩個分頁頁籤。一個是Android Virtual Devices頁面，提供AVD的管理介面。

![image_thumb_12.png](/images/posts/96776032-8ad6-4038-9b7f-ef6105e54160/image_thumb_12.png)

另一個是Device Definitions頁面，提供儀器定義的管理介面，我們可以將一些常用的儀器規格在這頁面中定義。按下[New Device...]按鈕自行重頭開始進行設定，或是按下[Clone...]按鈕以現有儀器定義為基礎下去做些修改。

![image_thumb_10.png](/images/posts/96776032-8ad6-4038-9b7f-ef6105e54160/image_thumb_10.png)

儀器的定義主要就是定義一些比較不會變動的儀器資訊，像是面板的Size、Sensors...之類的。

![image_thumb_11.png](/images/posts/96776032-8ad6-4038-9b7f-ef6105e54160/image_thumb_11.png)

有了想要模擬的儀器定義後，可以開始建立對應的AVD。

可在Andorid Virtual Devices頁籤按下右側的[New...]按鈕

![image_thumb_1.png](/images/posts/96776032-8ad6-4038-9b7f-ef6105e54160/image_thumb_1.png)

或是在儀器定義這邊按下右側的[Create AVD...]按鈕。

![image_thumb_8.png](/images/posts/96776032-8ad6-4038-9b7f-ef6105e54160/image_thumb_8.png)

按鈕按下後會看到像下面這樣的對話框，在這邊要設定AVD的名稱、對應的儀器定義、Android的版本、前後Camera、記憶體大小、SD卡大小...等等。相較於儀器定義，這邊的設定可以看到是一些比較會變動的資訊。

![image_thumb_2.png](/images/posts/96776032-8ad6-4038-9b7f-ef6105e54160/image_thumb_2.png)

設定完後按下[OK]按鈕，回到Android Virtual Device Manager的Android Virtual Devices頁面，可以看到我們剛剛所加入的AVD會出現在列表裡面。

因為Android的模擬器是以慢出名，所以這邊我們可以選取AVD後按下右側的[Start...]按鈕，將模擬器先行預跑起來。

![image_thumb_3.png](/images/posts/96776032-8ad6-4038-9b7f-ef6105e54160/image_thumb_3.png)

此時會彈出Launch Options對話框，這邊可以設定是否要清除資料，以及是否要進行縮放。如果模擬器跑起來太大時這邊可以設定縮放的比例，跑起來畫面會比較舒服。如果這邊設定已調整完畢或是沒甚麼要調整的，可按下[Launch]按鈕繼續。

![image_thumb_4.png](/images/posts/96776032-8ad6-4038-9b7f-ef6105e54160/image_thumb_4.png)

模擬器就會開始進行啟動的動作...

![image_thumb_5.png](/images/posts/96776032-8ad6-4038-9b7f-ef6105e54160/image_thumb_5.png)

若啟動過程無任何問題，可以看到我們設定的模擬器跑起來的樣子。

![image_thumb_6.png](/images/posts/96776032-8ad6-4038-9b7f-ef6105e54160/image_thumb_6.png)

## Link

* [Managing AVDs with AVD Manager](http://developer.android.com/tools/devices/managing-avds.html)
* [Android 模擬器 AVD ( Android Virtual Device )](http://shaocian.blogspot.tw/2012/08/android-avd-android-virtual-device.html)
