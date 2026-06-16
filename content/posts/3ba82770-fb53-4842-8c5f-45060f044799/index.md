---
title: "Run Google App Engine's application with dev_appserver.py"
date: "2013-11-06 12:00:00"
description: "前面筆者在Run application with Google App Engine Launcher這篇稍微介紹了一下怎樣用Google App Engine Launcher將Application在本地運行起來測試，透過GUI工具去做這樣的動作很方便，"
---

前面筆者在Run application with Google App Engine Launcher這篇稍微介紹了一下怎樣用Google App Engine Launcher將Application在本地運行起來測試，透過GUI工具去做這樣的動作很方便，但有時候我們會需要寫些Script進行自動測試之類的，GUI的工具就不太適合做類似這樣的處理，這時我們可以改用dev_appserver.py去將環境運行起來，這篇簡單的紀錄一下。

呼叫命令dev_appserver [Application Folder] (或是python dev_appserver [Application Folder])，會開始嘗試運行兩個Server，一個是用來跑我們的Application，一個用來跑管理的頁面。從Console的訊息我們可以看到一個是8080 port，一個是8000 port。

![image_thumb.png](/images/posts/3ba82770-fb53-4842-8c5f-45060f044799/image_thumb.png)

實際的開啟瀏覽器連結測試看看，Application運行良好。

![image_thumb_1.png](/images/posts/3ba82770-fb53-4842-8c5f-45060f044799/image_thumb_1.png)

管理頁面也運行良好。

![image_thumb_3.png](/images/posts/3ba82770-fb53-4842-8c5f-45060f044799/image_thumb_3.png)

用瀏覽器測試的同時，在Console畫面會秀出對應的Log訊息，便於我們偵錯。若有需要隨時可用熱鍵Ctrl + C中止服務。

![image_thumb_2.png](/images/posts/3ba82770-fb53-4842-8c5f-45060f044799/image_thumb_2.png)
