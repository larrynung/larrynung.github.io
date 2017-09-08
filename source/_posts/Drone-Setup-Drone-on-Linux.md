---
title: Drone - Setup Drone on Linux
date: 2017-09-07 00:13:50
tags: [Drone]
---

要安裝 Drone，首先需要安裝 Docker。  

<!-- More -->

<br/>


接著下載 Drone 的 deb 檔。  

    wget downloads.drone.io/master/drone.deb

{% asset_img 1.png %}

<br/>


透過 dpkg 安裝 Drone。  

    dpkg -i drone.deb

{% asset_img 2.png %}

<br/>


若有需要可開啟 Drone 配置文件配置 Port 以及資料庫連線，配置後將服務重啟。  

    vi /etc/drone/drone.toml 

{% asset_img 3.png %}

<br/>


即可用瀏覽器訪問架設好的 Drone 網站。  

{% asset_img 4.png %}

<br/>


Link
----
* [How to Setup Drone on Ubuntu/Debian - FoxuTech](https://foxutech.com/how-to-setup-drone/)
