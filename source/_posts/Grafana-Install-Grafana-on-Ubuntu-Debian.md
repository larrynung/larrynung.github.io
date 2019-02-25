---
title: Grafana - Install Grafana on Ubuntu & Debian
date: 2019-02-26 00:10:05
tags: [Grafana]
---

參照 [Grafana Download page](https://grafana.com/grafana/download)。  

<!-- More -->

{% asset_img 1.png %}

<br/>


下載 Grafana 套件。  

    wget https://dl.grafana.com/oss/release/grafana_6.0.0_amd64.deb 

{% asset_img 2.png %}

<br/>


安裝 Grafana 套件。  

    sudo dpkg -i grafana_6.0.0_amd64.deb 

{% asset_img 3.png %}

<br/>


啟動 Grafana 服務。  

    sudo service grafana-server start

{% asset_img 4.png %}

<br/>


訪問 http://localhost:3000，輸入預設帳密 admin/admin。  

{% asset_img 5.png %}

<br/>


更換預設帳號的密碼。  

{% asset_img 6.png %}

<br/>


就可以開始使用 Grafana 了。  

{% asset_img 7.png %}
