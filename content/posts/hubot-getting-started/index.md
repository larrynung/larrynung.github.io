---
title: "Hubot - Getting started"
date: "2018-10-31 08:46:14"
tags: [Hubot]
---


Hubot 安裝環境內需先有 Node.js，然後透過 Node.js 套件管理工具安裝 Yeoman 與 Hubot 到全域。  

<!-- More -->

    npm install -g yo generator-hubot

![1.jpg](1.jpg)

</br>


透過 Yeoman 建立 Hubot 專案。  

    yo hubot

![2.jpg](2.jpg)

</br>


Hubot 專案建立後會幫我們產生必要的檔案。  

    ls -a

![3.jpg](3.jpg)

</br>


一開始我們只是簡單的測試，不需要使用 Redis 與 Heroku，所以開啟 external-scripts.json 設定檔。  

    vim external-scripts.json

![4.jpg](4.jpg)

<br>


將 Redis 與 Heroku 設定移除後存檔。  

![5.jpg](5.jpg)

<br>


另外可以移除 hubot-scripts.json 設定檔，避免後面操作因為空的設定看到警告訊息。  

    rm hubot-scripts.json

![6.jpg](6.jpg)

<br>


運行 Hubot。  

    bin/hubot

![7.jpg](7.jpg)

<br>


運行時可用參數 --Name 為 Hubot 命名。  

    bin/hubot --name <Name>

![8.jpg](8.jpg)

<br>


Hubot 啟動後可用一下基本指令，像是 help 指令可查詢可使用的指令。  

    <Name> help

![9.jpg](9.jpg)

<br>


ping 指令可測試回應。  

    <Name> ping

![10.jpg](10.jpg)

<br>


time 指令可查詢時間。  

    <Name> time

![11.jpg](11.jpg)

<br>


echo 指令可回送發送過去的訊息。  

    <Name> echo <Message>

![12.jpg](12.jpg)

</br>


Link
----
* [Getting Started With Hubot](https://hubot.github.com/docs/)
