---
title: Hubot - Using with slack
date: 2018-11-10 00:14:25
tags: [Hubot]
---

要將 Hubot 整合 Slack，首先要先在 Slack 上建立 Hubot App。  

<!-- More -->

<br/>


在 Slack 上點選加入 Apps。  

{% asset_img 1.png %}

<br/>


選取安裝 Hubot App。  

{% asset_img 2.png %}

<br/>


點選 Install 按鈕。  

{% asset_img 3.png %}

<br/>


為加進 Slack 的 Hubot 取個名字，然後按下 Add Hubot Integration 按鈕。  

{% asset_img 4.png %}

<br/>


複製 API Token 供後續使用，設定 Hubot 的名字、圖示...等資訓。   

{% asset_img 5.png %}

<br/>


{% asset_img 6.png %}

<br/>


按下 Save Integration 按鈕。  

{% asset_img 7.png %}

<br/>


Slack 的 Apps 那區就會顯示剛所建立的 Hubot App。  

{% asset_img 8.png %}

<br/>


接著安裝 Hubot 要用到的 Slack adapter。  

    npm install hubot-slack --save

{% asset_img 9.png %}

<br/>


將剛剛複製的 API Token 設到環境變數。  

    set HUBOT_SLACK_TOKEN=<Token>

{% asset_img 10.png %}

<br/>


將 Hubot 運行起來並指定使用 Slack adapter。  

    hubot --adapter slack

{% asset_img 11.png %}

<br/>


Hubot 與 Slack 就做完整合的動作了，可直接對 Slack 的 Hubot app 調用 Hubot 的命令。  

{% asset_img 12.png %}

<br/>


{% asset_img 13.png %}

<br/>


{% asset_img 14.png %}

<br/>


Link
----
* [Using Hubot with slack](https://monicagranbois.com/blog/bots/using-hubot-with-slack/)
* [hubot-slack - npm](https://www.npmjs.com/package/hubot-slack)
