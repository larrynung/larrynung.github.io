---
title: Slack - Post Jenkins build notifications to a channel in Slack
date: 2018-11-14 00:06:00
tags: [Slack, Jenkins]
---

要使用 Slack 接收 Jenkins CI 的建置通知訊息，可在 Slack 中加入 Jenkins CI App。  

<!-- More -->

{% asset_img 1.png %}

<br/>


{% asset_img 2.png %}

<br/>


{% asset_img 3.png %}

<br/>


選取 Jenkins CI 建置通知訊息收到後要顯示在哪個 Channel，然後按下 Add Travis CI Integration 按鈕。  

{% asset_img 4.png %}

<br/>


然後照著指示設定 Jenkins。  

{% asset_img 5.png %}

<br/>


像是透過 Jenkins 的外掛程式管理為 Jenkins 加裝 Slack Notification 套件。  

{% asset_img 6.png %}

<br/>


{% asset_img 7.png %}

<br/>


{% asset_img 8.png %}

<br/>


{% asset_img 9.png %}

<br/>


接著進入設定系統。  

{% asset_img 10.png %}

<br/>


設定 Global Slack Notifier Settings 的 Base URL 與 Integration
 Token，按下儲存按鈕。  

{% asset_img 11.png %}

<br/>


進到 Job 的組態設定。  

{% asset_img 12.png %}

<br/>


在建置後動作加入 Slack Notifications。  

{% asset_img 13.png %}

<br/>


設定要通知的事件。  

{% asset_img 14.png %}

<br/>


當對應事件發生時 Slack 就會收到 Jenkins 的通知訊息。  

{% asset_img 15.png %}

<br/>


Link
----
* [Jenkins CI | Slack App Directory](https://slack.com/apps/A0F7VRFKN-jenkins-ci)
