---
title: Firebase - Realtime database rules
date: 2018-02-21 23:59:05
tags: [Firebase]
---

Firebase 專案建立後，若要使用 Realtime Database 功能可點選左側 DEVELOP 下的 Database。   

<!-- More -->

{% asset_img 1.png %}
 
<br/>


點選 Realtime Database 下的開始使用按鈕。  

{% asset_img 2.png %}
 
<br/>


在開始使用 Realtime Database 之前，我們需先切至規則頁面，調整 Realtime Database 的的安全性規則設定。  

<br/>


預設的安全性規則設定為讀寫都需先經過認證。  

{% asset_img 3.png %}
 
<br/>


我們可以開啟模擬工具簡單的測試一下，嘗試讀取 Realtime Database。  

{% asset_img 4.png %}
 
<br/>


因為沒通過認證，所以讀取的動作會被拒絕。  

{% asset_img 5.png %}
 
<br/>


如果我們將設定調整如下，直接開放讀取與寫入，讓讀取與寫入的動作不需要經過認證。  
  
{% asset_img 6.png %}
 
<br/>


同樣的透過模擬工具簡單的測試一下。  

{% asset_img 7.png %}
 
<br/>


會發現讀寫的動作都會不會被拒絕了。  

{% asset_img 8.png %}
 
<br/>


Link
----
* [Understand Firebase Realtime Database Rules  |  Firebase Realtime Database  |  Firebase](https://firebase.google.com/docs/database/security/)
