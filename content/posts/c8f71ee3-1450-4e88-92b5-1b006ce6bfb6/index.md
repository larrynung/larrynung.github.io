---
title: "Create new application with Google App Engine Launcher"
date: "2013-11-06 12:00:00"
description: "Create new application with Google App Engine Launcher"
---

要開始撰寫Google App Engine Application，我們需先在Google App Engine網站上申請一個應用程式(可參閱筆者Registering Google App Engine's Application這篇)，然後開始在本地進行應用程式的撰寫。在應用程式的撰寫上，我們可以徒手建立app.yaml與Application所需的程式主檔，也可以套用工具輔助我們產生這些必要的檔案。

在開始在本地進行應用程式的撰寫時，我們可以開啟Google App Engine Launcher，點選[File/Create New Application...]選單選項，準備建立一個新的應用程式。

![image_thumb_1.png](/images/posts/c8f71ee3-1450-4e88-92b5-1b006ce6bfb6/image_thumb_1.png)

點選後會彈出對話框詢問該Application的名稱、存放位置、Runtime、以及要在本地運行的Port，設定完後點選Create按鈕繼續。

![Image(43)_thumb.png](/images/posts/c8f71ee3-1450-4e88-92b5-1b006ce6bfb6/Image(43)_thumb.png)

回到Google App Engine Launcher主頁面後，下方的清單中會多出剛加入的項目。

![image_thumb_2.png](/images/posts/c8f71ee3-1450-4e88-92b5-1b006ce6bfb6/image_thumb_2.png)

用檔案總管開啟對應的目錄，可以看到Google App Engine Application最重要的app.yaml以及python程式主檔都會自動幫我們生成並放在裡面，不需要手動的去建置這些檔案。

![Image(47)_thumb.png](/images/posts/c8f71ee3-1450-4e88-92b5-1b006ce6bfb6/Image(47)_thumb.png)

Python的程式主檔預設產生的內容是一個簡單的HelloWorld程式。簡單的說它就是一個MainHandler的類別，負責秀出HelloWorld的字樣，而最下面有個router指定首頁是交給MainHandler去處理。我們可以開啟該Python程式主檔將之替換成我們想要處理的動作。

 ![image_thumb.png](/images/posts/c8f71ee3-1450-4e88-92b5-1b006ce6bfb6/image_thumb.png)

回到主題，接著請參閱Run application with Google App Engine Launcher這篇將Application運行起來 ，我們就可以看到Application運行起來的樣子。

![Image(48)_thumb.png](/images/posts/c8f71ee3-1450-4e88-92b5-1b006ce6bfb6/Image(48)_thumb.png)
