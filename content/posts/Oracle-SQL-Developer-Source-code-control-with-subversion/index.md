---
title: "Oracle SQL Developer - Source code control with subversion"
date: "2017-08-01 13:14:31"
tags: [Oracle SQL Developer]
---


Oracle SQL Developer 要使用 Subversion 進行程式碼的版本控制，首先要建立連線。  

<!-- More -->

<br/>


可以透過 [Team | Subversion | Create Connection...] 選單選項進行連線的建立。  

![1.png](1.png)

<br/>


選取 Manually Create a Subversion Connection 後按下 OK 按鈕。  

![2.png](2.png)

<br/>


輸入 Subversion Repository 位置、連線名稱、帳號、密碼建立連線。  

![3.png](3.png)

<br/>


![4.png](4.png)

<br/>


連線建立完成即可在 Versions 看到剛所建立的連線。  

![5.png](5.png)

<br/>


連線建立後要透過 Check Out... 滑鼠右鍵選單選項進行檔案的 Check Out。  

![6.png](6.png)

<br/>


![7.png](7.png)

<br/>


設定 Check Out 下來的位置。  

![8.png](8.png)

<br/>


若有需要也可以指定 Check Out 的版本。  

![9.png](9.png)

<br/>


設定好按下 OK 按鈕繼續。  

![10.png](10.png)

<br/>


![11.png](11.png)

<br/>


Check Out 下來後透過 Files 視窗瀏覽檔案可看到檔案的版控狀態。  

![12.png](12.png)

<br/>


後續也可以直接透過 Oracle SQL Developer 進行 Commit 之類的版控動作。  

![13.png](13.png)

<br/>


![14.png](14.png)

<br/>
