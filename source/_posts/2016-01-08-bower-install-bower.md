---
layout: post
title: "Bower - Install Bower"
date: 2016-01-08 05:23:00
comments: true
categories: [Bower]
keywords: "Bower"
description: "Bower - Install Bower"
---

Bower 依賴於 Node.js 與 Git，安裝 Bower 需透過 Node.js 內的 npm，只要透過下列 npm 命令安裝即可：  

<!-- More -->

    npm install -g bower

<br/>


{% img /images/posts/InstallBower/1.png %}

<br/>


而  Bower 套件的安裝與使用會用到 Git，所以記得也要將之安裝。  

<br/>


如果是 Ubuntu 用戶，可以透過下列命令將整個環境安裝起來：  

{% codeblock lang:bash %}
sudo apt-get purge nodejs npm 
sudo apt-get update 
sudo apt-get install -y python-software-properties python g++ make 
sudo add-apt-repository ppa:chris-lea/node.js 
sudo apt-get update 
sudo apt-get install -y nodejs 
sudo apt-get install -y git
sudo npm install -g bower
{% endcodeblock %}
