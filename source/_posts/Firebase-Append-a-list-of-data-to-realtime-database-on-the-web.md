---
title: Firebase - Append a list of data to realtime database on the web
date: 2018-02-26 12:10:13
tags: [Firebase]
---

要將資料附加到 Firebase 的 List 內，需先進行 Firebase 與應用程式的連結，然後透過呼叫 Firebase 的 database 方法取得資料庫物件，調用 ref 方法取得資料物件的參考，再調用 push 方法取得新資料的參考，透過參考調用 set 方法將資料寫入即可。  

<!-- More -->

{% asset_img 1.png %}
 
<br/>


{% asset_img 2.png %}
 
<br/>


Link
----
* [Work with Lists of Data on the Web  |  Firebase Realtime Database  |  Firebase](https://firebase.google.com/docs/database/web/lists-of-data)
