---
title: Oracle SQL Developer - Source code control with subversion
date: 2017-08-01 13:14:31
tags: [Oracle SQL Developer]
---

Oracle SQL Developer 要使用 Subversion 進行程式碼的版本控制，首先要建立連線。  

<!-- More -->

<br/>


可以透過 [Team | Subversion | Create Connection...] 選單選項進行連線的建立。  

{% asset_img 1.png %}

<br/>


選取 Manually Create a Subversion Connection 後按下 OK 按鈕。  

{% asset_img 2.png %}

<br/>


輸入 Subversion Repository 位置、連線名稱、帳號、密碼建立連線。  

{% asset_img 3.png %}

<br/>


{% asset_img 4.png %}

<br/>


連線建立完成即可在 Versions 看到剛所建立的連線。  

{% asset_img 5.png %}

<br/>


連線建立後要透過 Check Out... 滑鼠右鍵選單選項進行檔案的 Check Out。  

{% asset_img 6.png %}

<br/>


{% asset_img 7.png %}

<br/>


設定 Check Out 下來的位置。  

{% asset_img 8.png %}

<br/>


若有需要也可以指定 Check Out 的版本。  

{% asset_img 9.png %}

<br/>


設定好按下 OK 按鈕繼續。  

{% asset_img 10.png %}

<br/>


{% asset_img 11.png %}

<br/>


Check Out 下來後透過 Files 視窗瀏覽檔案可看到檔案的版控狀態。  

{% asset_img 12.png %}

<br/>


後續也可以直接透過 Oracle SQL Developer 進行 Commit 之類的版控動作。  

{% asset_img 13.png %}

<br/>


{% asset_img 14.png %}

<br/>