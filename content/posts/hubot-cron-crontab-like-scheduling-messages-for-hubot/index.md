---
title: "hubot-cron - Crontab like scheduling messages for Hubot"
date: "2018-11-16 00:17:15"
tags: [Hubot]
---


要讓 Hubot 支援排程發送訊息，可以安裝 hubot-cron 套件。

<!-- More -->

    npm install hubot-cron --save

![1.png](1.png)

<br/>


然後在 external-scripts.json 加入 hubot-cron。  

![2.png](2.png)

<br/>


接著將 Hubot 運行起來。  

![3.png](3.png)

<br/>


就可以在 Hubot 內加入排程訊息。  

    <Hubot> new job <Cron> <Msg>

![4.png](4.png)

<br/>


有需要的話可以查閱加入的排程。  

    <Hubot> list jobs

![5.png](5.png)

<br/>


也可以移除加入的排程。  

    <Hubot> rm job <ID>

![6.png](6.png)

<br/>


Link
