---
title: "mmock - Run mmock with Kitematic"
date: "2017-09-12 23:52:41"
tags: [mmock]
---


要透過 Kitematic 使用 mmock，可在 Kitematic 搜尋 mmock 的容器，點選 CREATE 按鈕將容器拉回啟用。  

<!-- More -->

![1.png](1.png)

<br/>


容器啟用後在 CONTAINER LOGS 這邊會看到 mmock 服務啟用的畫面，上面會帶有 http、https、console 服務的資訊。

<br/>


IP & PORTS 這邊會顯示容器與主機的 Port 號對應。  

<br/>


點選 VOLUMES 可開啟對應的目錄位置。  

![2.png](2.png)

<br/>



![3.png](3.png)

<br/>


將 mmock 的設定放至這個位置。  

![4.png](4.png)

<br/>


mmock 即可依照設定 mock API。  

![5.png](5.png)

<br/>


Link
----
* [jmartin82/mmock: Mmock is an HTTP mocking application for testing and fast prototyping](https://github.com/jmartin82/mmock)
