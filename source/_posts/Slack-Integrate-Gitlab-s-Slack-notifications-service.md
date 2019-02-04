---
title: Slack - Integrate GitLab's Slack notifications service
date: 2018-11-20 00:41:17
tags: [Slack]
---

要使用 Slack 接收 GitLab CI 的通知訊息，可在 Slack 中加入 Incoming WebHooks App。

<!-- More -->

{% asset_img 1.png %}

<br/>


{% asset_img 2.png %}

<br/>


{% asset_img 3.png %}

<br/>


選取 GitLab CI 通知訊息收到後要顯示在哪個 Channel。  

{% asset_img 4.png %}

<br/>


複製 Webhook URL 後續在 GitLab 設定那邊使用。  

{% asset_img 5.png %}

<br/>


設置 App 的名字、描述、圖示等，設置完後按下 Save Settings 按鈕存檔。  

{% asset_img 6.png %}

<br/>


開啟 GitLab 的 Integrations 專案設定。  

{% asset_img 7.png %}

<br/>


點選 Slack notifications。  

{% asset_img 8.png %}

<br/>


設定何時要通知 Slack，以及要通知到哪個 Channel。  

{% asset_img 9.png %}

<br/>


設定 Slack 的 Wabhook URL，按下 Test settings and save changes 按鈕測試並存檔。  

{% asset_img 10.png %}

<br/>


Slack 就會收到 GitLab 傳來的通知訊息。  

{% asset_img 11.png %}

<br/>


Link
----
* [Slack Notifications Service | GitLab](https://docs.gitlab.com/ee/user/project/integrations/slack.html)
* [【SLACK】串接 gitlab 事件到 slack – 進擊的 Tool’ s – Medium](https://medium.com/tool-s/slack-%E4%B8%B2%E6%8E%A5-gitlab-%E4%BA%8B%E4%BB%B6%E5%88%B0-slack-e9549a7907ff)
