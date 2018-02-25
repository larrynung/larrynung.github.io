---
title: Firebase - Read data once from realtime database on the web
date: 2018-02-25 21:58:31
tags: [Firebase]
---

要將資料自 Firebase 讀取出來，需先進行 Firebase 與應用程式的連結，然後透過呼叫 Firebase 的 database 方法取得資料庫物件，調用 ref 方法取得資料物件的參考，最後調用 once 與 then 方法，在 then 方法中帶入一個委派，在委派內取用數值即可。  

<!-- More -->

{% asset_img 1.png %}
 
<br/>


假設 Firebase Realtime Database 內的資料如下： 

{% asset_img 2.png %}
 
<br/>


運行起來可以看到會從 Firebase 取得正確的數值。  

{% asset_img 3.png %}
 
<br/>


Link
----
* [Read and Write Data on the Web  |  Firebase Realtime Database  |  Firebase](https://firebase.google.com/docs/database/web/read-and-write)
