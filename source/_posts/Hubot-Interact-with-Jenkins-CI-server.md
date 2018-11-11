---
title: Hubot - Interact with Jenkins CI server
date: 2018-11-11 23:28:26
tags: [Hubot]
---

要將 Hubot 整合 Jenkins 服務，可為 Hubot 加裝 hubot-jenkins 套件。  

<!-- More -->

    npm i hubot-jenkins

{% asset_img 1.png %}

<br/>


開啟 external-scripts.json，加上 hubot-jenkins 設定，存檔後關閉。

{% asset_img 2.png %}

<br/>


然後要透過 HUBOT_JENKINS_URL 環境變數設定 Jenkins 服務的位置。  

    set HUBOT_JENKINS_URL=<JenkinsUrl>

{% asset_img 3.png %}

<br/>


透過 HUBOT_JENKINS_AUTH 環境變數設定 Jenkins 服務的帳密 (使用 user:password 這樣的格式做設定)。  

    set HUBOT_JENKINS_AUTH=<Auth>

{% asset_img 4.png %}

<br/>


將 Hubot 啟動，可對 Hubot 調用命令查閱 Jenkins 服務上有的 Job。  

    <Hubot> jenkins list

{% asset_img 5.png %}

<br/>


{% asset_img 6.png %}

<br/>


可查詢指定的 Jenkins Job。  

    <Hubot> jenkins describe <Job>

{% asset_img 7.png %}

<br/>


可用 Jenkins Job Name 去建置特定的 Jenkins Job。  

    <Hubot> jenkins build <Job>

{% asset_img 8.png %}

<br/>


或是用編號建置特定的 Jenkins Job。  

    <Hubot> jenkins b <No>

{% asset_img 9.png %}

<br/>


{% asset_img 10.png %}

<br/>


也可以查詢特定 Jenkins Job 最後一次建置。  

    <Hubot> jenkins last <Job>

{% asset_img 11.png %}

<br/>


Link
----
* [hubot-jenkins - npm](https://www.npmjs.com/package/hubot-jenkins)
