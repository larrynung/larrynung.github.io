---
title: Firebase - Set data to realtime database on the web
date: 2018-02-25 00:05:34
tags: [Firebase]
---

建立完 Firebase 專案且調完資料庫的安全性規則設定，可以開始嘗試進行 Firebase Realtime Database 的寫入動作，因為這邊是用 Web 專案開發，所以點選 "將 Firebase 加入您的網路應用程式"。進行應用程式的連結。  

<!-- More -->

{% asset_img 1.png %}
 
<br/>


這邊會給予一段連結應用程式用的 JavaScript 程式，按下複製按鈕複製下來，貼至應用程式中。完成應用程式的連結。  

{% asset_img 2.png %}
 
<br/>


接著進行撰寫寫入的部分，透過呼叫 Firebase 的 database 方法取得資料庫物件，調用 ref 方法取得資料物件的參考，最後調用 set 方法將要設定的資料值帶入即可。  


{% asset_img 3.png %}
 
<br/>


將撰寫的應用程式運行起來。  

{% asset_img 4.png %}
 
<br/>


回到 Firebase Realtime Database 的資料頁面，可以看到資料已被正確的寫入。  

{% asset_img 5.png %}
 
<br/>


{% asset_img 6.png %}

<br/>


{% asset_img 7.png %}

<br/>


Link
----
* [Read and Write Data on the Web  |  Firebase Realtime Database  |  Firebase](https://firebase.google.com/docs/database/web/read-and-write)
