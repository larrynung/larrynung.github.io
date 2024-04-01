---
title: "Hubot - Using with SSH"
date: "2018-11-11 00:13:28"
tags: [Hubot]
---


要將 Hubot 整合 SSH，可以安裝 hubot-sshbot。  

<!-- More -->

    npm install --save hubot-sshbot

![1.png](1.png)

<br/>


安裝完後透過 HUBOT_SSH_HOST_KEY 環境變數指定 SSH key。  

    set HUBOT_SSH_HOST_KEY=<SSHKey>

![2.png](2.png)

<br/>


透過 HUBOT_SSH_POST 環境變數指定要使用的 Port (預設是使用 3050)。  

    set HUBOT_SSH_PORT=<Port>

![3.png](3.png)

<br/>


透過 HUBOT_SSH_HOST 環境變數指定 Host 的位置 (預設是 0.0.0.0)。

<br/>


將 Hubot 運行起來並指定使用 SSH adapter。  

    hubot -a sshbot

![4.png](4.png)

<br/>


接著透過 SSH 連進去。  

![5.png](5.png)

<br/>


就可以看到 SSH Hubot 的畫面。  

![6.png](6.png)

<br/>


可以透過 SSH Hubot 調用 Hubot 命令。  

![7.png](7.png)

<br/>


![8.png](8.png)

<br/>


Link
----
* [kylemacey/hubot-sshbot: An SSH based Hubot adapter to allow Hubot to be accessed from an SSH client.](https://github.com/kylemacey/hubot-sshbot)
