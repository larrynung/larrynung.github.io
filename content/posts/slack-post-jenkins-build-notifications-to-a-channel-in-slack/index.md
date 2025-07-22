---
title: "Slack - Post Jenkins build notifications to a channel in Slack"
date: "2018-11-14 00:06:00"
tags: [Slack, Jenkins]
---

要使用 Slack 接收 Jenkins CI 的建置通知訊息，可在 Slack 中加入 Jenkins CI App。

![1.png](1.png)

![2.png](2.png)

![3.png](3.png)

選取 Jenkins CI 建置通知訊息收到後要顯示在哪個 Channel，然後按下 Add Travis CI Integration 按鈕。

![4.png](4.png)

然後照著指示設定 Jenkins。

![5.png](5.png)

像是透過 Jenkins 的外掛程式管理為 Jenkins 加裝 Slack Notification 套件。

![6.png](6.png)

![7.png](7.png)

![8.png](8.png)

![9.png](9.png)

接著進入設定系統。

![10.png](10.png)

設定 Global Slack Notifier Settings 的 Base URL 與 Integration
Token，按下儲存按鈕。

![11.png](11.png)

進到 Job 的組態設定。

![12.png](12.png)

在建置後動作加入 Slack Notifications。

![13.png](13.png)

設定要通知的事件。

![14.png](14.png)

當對應事件發生時 Slack 就會收到 Jenkins 的通知訊息。

![15.png](15.png)

Link
----
* [Jenkins CI | Slack App Directory](https://slack.com/apps/A0F7VRFKN-jenkins-ci)