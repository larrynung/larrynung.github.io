---
title: "sonar - Getting started"
date: "2017-10-29 16:11:28"
tags: [sonar]
---


要使用 sonar CLI，需先要有 Node.js v8.x 以上的版本。   

<!-- More -->

<br/>


再透過 npm 安裝 sonar 到全域。   

    npm install -g --engine-strict @sonarwhal/sonar

![1.png](1.png)

<br/>


安裝完可查詢 sonar 版本確認安裝的狀態。  

    sonar -v

![2.png](2.png)

<br/>


若安裝無誤可用 sonar 命令產生 sonar 的設定檔。  

    sonar --init

![3.png](3.png)

<br/>


設定完 sonar 的設定檔 (.sonarrc) 就會產生在當前目錄。    

![4.png](4.png)

<br/>


若有需要可將設定檔開啟修改。  

![5.png](5.png)

<br/>


![6.png](6.png)

<br/>


最後調用 sonar 命令並帶上要分析的網址，即可使用 sonar 分析指定的網站。  

    sonar [URL]

![7.png](7.png)

<br/>


![8.png](8.png)

<br/>


Link
----
* [User guide | sonar documentation](https://sonarwhal.com/docs/user-guide/)
