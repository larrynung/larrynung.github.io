---
title: "Hubot - Using with slack"
date: "2018-11-10 00:14:25"
tags: [Hubot]
---


要將 Hubot 整合 Slack，首先要先在 Slack 上建立 Hubot App。  

<!-- More -->

<br/>


在 Slack 上點選加入 Apps。  

![1.png](1.png)

<br/>


選取安裝 Hubot App。  

![2.png](2.png)

<br/>


點選 Install 按鈕。  

![3.png](3.png)

<br/>


為加進 Slack 的 Hubot 取個名字，然後按下 Add Hubot Integration 按鈕。  

![4.png](4.png)

<br/>


複製 API Token 供後續使用，設定 Hubot 的名字、圖示...等資訓。   

![5.png](5.png)

<br/>


![6.png](6.png)

<br/>


按下 Save Integration 按鈕。  

![7.png](7.png)

<br/>


Slack 的 Apps 那區就會顯示剛所建立的 Hubot App。  

![8.png](8.png)

<br/>


接著安裝 Hubot 要用到的 Slack adapter。  

    npm install hubot-slack --save

![9.png](9.png)

<br/>


將剛剛複製的 API Token 設到環境變數。  

    set HUBOT_SLACK_TOKEN=<Token>

![10.png](10.png)

<br/>


將 Hubot 運行起來並指定使用 Slack adapter。  

    hubot --adapter slack

![11.png](11.png)

<br/>


Hubot 與 Slack 就做完整合的動作了，可直接對 Slack 的 Hubot app 調用 Hubot 的命令。  

![12.png](12.png)

<br/>


![13.png](13.png)

<br/>


![14.png](14.png)

<br/>


Link
----
* [Using Hubot with slack](https://monicagranbois.com/blog/bots/using-hubot-with-slack/)
* [hubot-slack - npm](https://www.npmjs.com/package/hubot-slack)
