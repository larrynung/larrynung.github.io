---
title: Mailgun - Authorized Recipients
date: 2018-01-31 23:43:03
tags: [Mailgun]
---

Mailgun 使用 Sandbox subdomain 時，預設只能發送訊息給自己的信箱，除非加上自己的 Domain 或是設定 Authorized recipients。  

<!-- More -->

{% asset_img 1.png %}
 
<br/>


要設定 Autorized recipients，點選網頁右上角的帳號名稱，點選 Account Settings 選單選項。  

{% asset_img 2.png %}
 
<br/>


接著切至 Autorized recipients 頁面。  

{% asset_img 3.png %}
 
<br/>


點選 Invite New Recipient 按鈕。  

{% asset_img 4.png %}
 
<br/>


將要加入的 Recipient mail 位置填入，按下 Invite Recipient 按鈕。  

{% asset_img 5.png %}
 
<br/>


Recipient 就會被加到列表中，此時還是 Unverified 的狀態。  

{% asset_img 6.png %}
 
<br/>


Recipient 會收到來自 Mailgun 的驗證信件，按下 Aggree 按鈕進行驗證的動作。  

{% asset_img 7.png %}
 
<br/>


再次按下 Yes 按鈕確認。  

{% asset_img 8.png %}
 
<br/>


驗證的動作就完成了。  

{% asset_img 9.png %}
 
<br/>


此時 Mailgun 的 Authorized Recipients 內的狀態會變為 Verified。  

{% asset_img 10.png %}
 
<br/>


Mailgun 就可以正常的發送信件給 Recipient 了。  

{% asset_img 11.png %}
 
<br/>

