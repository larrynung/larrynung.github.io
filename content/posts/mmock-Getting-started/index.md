---
title: "mmock - Getting started"
date: "2017-09-14 21:01:47"
tags: [mmock]
---


要使用 mmock 除了將 mmock 服務啟用外。  

<!-- More -->

![1.png](1.png)

<br/>


還要在放置 mock 設定在放置設定檔的目錄，mmock 會去放置設定檔的目錄找尋並載入設定。  

![2.png](2.png)

<br/>


放置好後透過 mmock 的 http 或是 https 位置訪問 mock 出來的 API 位置即可，像是筆者的 mmock http 位置為 192.168.99.100:3281，而設定檔內設定的是 http 這個 path，所以訪問 http://192.168.100:3281/hello 就會依設定檔內的設定去回應。  

![3.png](3.png)

<br/>


如果有開啟 mmock 的 console 頁面，當 request 進來時 console 頁面會立即收到請求，可在主控台查閱發送的請求。   

![4.png](4.png)

<br/>


點選展開可看到更為詳細的資訊，像是回應的內容...等。  

![5.png](5.png)

<br/>


切到 Mapping 頁面，可看到 mmock 載入進去的設定檔，設定檔檔名、設定的 Method、與 Path，點選後面的 View 按鈕。  

![6.png](6.png)

<br/>


可看到設定檔的內容。  

![7.png](7.png)

<br/>


如果需要調動設定，可點選後方的 Edit 按鈕。  

![8.png](8.png)

<br/>


調動設定檔後存檔。  

![9.png](9.png)

<br/>


Link
-----
* [jmartin82/mmock: Mmock is an HTTP mocking application for testing and fast prototyping](https://github.com/jmartin82/mmock)
