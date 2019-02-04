---
title: Slack - Setting up Slack build notification in Travis CI
date: 2018-11-13 00:13:09
tags: [Slack, Travis]
---

要使用 Slack 接收 Travis CI 的建置通知訊息，可在 Slack 中加入 Travis CI App。  

<!-- More -->

{% asset_img 1.png %}

<br/>


{% asset_img 2.png %}

<br/>


{% asset_img 3.png %}

<br/>


選取 Travis CI 建置通知訊息收到後要顯示在哪個 Channel。  

{% asset_img 4.png %}

<br/>


{% asset_img 5.png %}

<br/>


選好後按下 Add Travis CI Integration 按鈕。  

{% asset_img 6.png %}

<br/>


接著照著教學設置 Travis CI 的設定檔。  

{% asset_img 7.png %}

<br/>


{% asset_img 8.png %}

<br/>


再接著設置 Travis CI App 的名字、描述、圖示等，設置完後按下 Save Settings 按鈕存檔。  

{% asset_img 9.png %}

<br/>


後續 Travis CI 建置時。Slack 就可以在指定的 Channel 收到對應的建置通知。  

{% asset_img 10.png %}

<br/>


Link
---
* [Setting Up Slack Build Notification in Travis CI for Github Project - AxdLog](https://axdlog.com/2018/setting-up-slack-build-notification-in-travis-ci-for-github-project/)
