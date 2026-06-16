---
title: "Run application with Google App Engine Launcher"
date: "2013-11-06 12:00:00"
description: "在開發Google App Engine's Application時，我們可以先在本地撰寫好程式，並在本地運行測試，當一切測試無誤後再將它上到雲端，這邊簡單的紀錄一下怎樣透過Google App Engine Launcher來運行本地測試。"
---

在開發Google App Engine's Application時，我們可以先在本地撰寫好程式，並在本地運行測試，當一切測試無誤後再將它上到雲端，這邊簡單的紀錄一下怎樣透過Google App Engine Launcher來運行本地測試。

Google App Engine Launcher開啟後，我們先將Application加至Google App Engine Launcher中。將剛加入的Application選取起來，再點選上方的Run按鈕。

![image_thumb.png](/images/posts/17813c87-3321-4d8e-be7b-eb3f15122c24/image_thumb.png)

Google App Engine就會開始嘗試在背後運行兩個Server，一個是用來跑我們的Application，一個用來跑管理的頁面。嘗試運行Server需要一些時間，若中途需要中斷，這邊隨時可以停止。

![image_thumb_1.png](/images/posts/17813c87-3321-4d8e-be7b-eb3f15122c24/image_thumb_1.png)

嘗試運行的同時，若想查看目前所在處理的動作，可以點選上面的Logs按鈕叫出Log Console視窗，在Log Console視窗中會有詳細的處理動作。

![image_thumb_2.png](/images/posts/17813c87-3321-4d8e-be7b-eb3f15122c24/image_thumb_2.png)

Server跑起來後，我們可以利用這個Server在本地端執行我們的Application，這邊可以直接按下上方的Browse按鈕， 用系統瀏覽器去跑我們的Application。

![image_thumb_3.png](/images/posts/17813c87-3321-4d8e-be7b-eb3f15122c24/image_thumb_3.png)

沒意外的話我們應該可以在瀏覽器中看到Application運行的結果。

![image_thumb_4.png](/images/posts/17813c87-3321-4d8e-be7b-eb3f15122c24/image_thumb_4.png)
