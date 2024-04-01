---
title: "Firebase - Listen for value events from realtime database on the web"
date: "2018-02-25 22:32:23"
tags: [Firebase]
---


要監聽資料並自 Firebase 將資料讀取出來，需先進行 Firebase 與應用程式的連結，然後透過呼叫 Firebase 的 database 方法取得資料庫物件，調用 ref 方法取得資料物件的參考，最後調用 on 方法，指定監聽 value 事件，並帶入一個委派，在委派內取用數值即可。  

<!-- More -->

![1.png](1.png)
 
<br/>


像是本來 Firebase Realtime Database 內的資料如下：  

![2.png](2.png)
 
<br/>


將應用程式運行起來，可以看到應用程式正常取得了資料。  

![3.png](3.png)
 
<br/>


這時回到 Firebase Realtime Database 的資料頁面，將資料值做個修改。  

![4.png](4.png)
 
<br/>


可以看到應用程式監聽到了資料的改變，並做出了對應的動作。  

![5.png](5.png)
 
<br/>


Link
----
* [Read and Write Data on the Web  |  Firebase Realtime Database  |  Firebase](https://firebase.google.com/docs/database/web/read-and-write)
