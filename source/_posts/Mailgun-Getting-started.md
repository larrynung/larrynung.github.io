---
title: Mailgun - Getting started
date: 2018-01-29 00:02:23
tags: [Mailgun]
---

要使用 Mailgun 發送 Email，先要有 Mailgun 會員帳號。  

<!-- More -->

{% asset_img 1.png %}
 
<br/>


{% asset_img 2.png %}
 
<br/>


註冊成為 Mailgun 會員後，會被導到 https://app.mailgun.com/app/account/setup 頁面，該頁面會簡單的展示 Curl、Ruby、Python、PHP、Java、與 C# 等不同的使用方式。  

{% asset_img 3.png %}
 
<br/>


這邊可以簡單的用 Curl 測試一下，下完 Curl 命令後可從 API 的回應看到訊息已發送至 Mailgun 且被 Queue 起來供後續處理。  

{% asset_img 4.png %}
 
<br/>


處理的紀錄可在 Mailgun 的 Logs 頁面查閱。  

{% asset_img 5.png %}
 
<br/>


若有需要也可以進一步展開查閱更為細節的部分。  

{% asset_img 6.png %}
 
<br/>


{% asset_img 7.png %}
 
<br/>


Link
====
* [Transactional Email API Service For Developers | Mailgun](https://www.mailgun.com/)
