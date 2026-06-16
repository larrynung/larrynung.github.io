---
title: "Create your first android app with Android Studio"
date: "2013-11-06 12:00:00"
tags: [Android]
description: "參閱Prepare android development environment with Android Studio這篇準備好開發環境後，讓我們實際的用Android Studio建立一個App看看。 滑鼠點擊Android Studio程式Icon，啟動Android Studio。"
---

參閱Prepare android development environment with Android Studio這篇準備好開發環境後，讓我們實際的用Android Studio建立一個App看看。

滑鼠點擊Android Studio程式Icon，啟動Android Studio。

![image39_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image39_thumb.png)

![image_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image_thumb.png)

啟動完成會看到像下面這樣的對話框，我們可以透過這個對話框進行建立專案、匯入專案、開啟專案...等動作。因為這篇是要建立我們的第一個Android App，所以這邊直接用滑鼠點擊[New Project...]，開始建立一個新的Android App專案。

![image6_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image6_thumb.png)

接著會彈出New Project對話框，可以設定這個Application的名稱、專案的名稱、組件的名稱、支援的SDK、是否要有Activity、以及是否要有custim launcher icon...等。設定完成請按下方的[Next]按鈕繼續

![image9_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image9_thumb.png)

這邊如果剛剛有勾選Create custom launcher icon的話，會開始進行custom launcher icon的設置。設置完成按下[Next]按鈕繼續。

![image12_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image12_thumb.png)

如果剛剛有勾選Create activity，會出現Create Activity的設置頁面。這邊選取你想要建立的Activity樣板，設置完成按下[Next]按鈕繼續。

![image15_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image15_thumb.png)

設定Activity的名稱...等細部資訊後，按下[Finish]按鈕結束新專案的建立動作。

![image18_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image18_thumb.png)

操作上跟使用eclipse去開發是大同小異的。

到這邊新建的專案已經被Android Studio載入。接著透過熱鍵Shift + F10，或是上方工具列上的運行按鈕，實際的將程式運行起來看看。

![image56_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image56_thumb.png)

運行後Android Studio會彈出Choose Device對話框，詢問我們要將程式運行至哪邊。如果Android模擬器已經跑起，我們可以選取"Choose a running device"選項，然後按下[OK]按鈕，將程式跑在運行中的模擬器。

![image60_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image60_thumb.png)

如果Android模擬器尚未跑起，我們可以選取Launch emulator選項，在下方的Android virtual device那邊下拉選取想要運行的AVD。

![image36_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image36_thumb.png)

如果下拉清單沒有可用的AVD，我們可以點選後方的[...]按鈕進行AVD的設定。

![image30_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image30_thumb.png)

AVD的設定可參閱筆者[Managing AVDs with AVD Manager](http://www.dotblogs.com.tw/larrynung/archive/2013/07/27/112558.aspx)這篇...

![image33_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image33_thumb.png)

設定完成按下[OK]按鈕，模擬器會開始啟動。模擬器啟動完成Application也回開始佈署到模擬器上面，佈署完成Application就會運行起來，運行的畫面會像下面這樣：

![image63_thumb.png](/images/posts/d6a53137-24fb-489d-accf-4df3d53e95cd/image63_thumb.png)
