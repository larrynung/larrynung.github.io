---
title: Consul - Install on Ubuntu
date: 2018-12-06 00:33:58
tags: [Consul, Ubuntu]
---

要在 Ubuntu 安裝 Consul，要先在 [Download Consul - Consul by HashiCorp](https://www.consul.io/downloads.html) 這邊找到 Consul 檔案位置。  

<!-- More -->

{% asset_img 1.png %}

<br/>


下載 Consul 檔案。  

    wget <ConsulFileUrl>

{% asset_img 2.png %}

<br/>


將下載下來的 Consul 檔案進行解壓縮。   

    apt-get install unzip

{% asset_img 3.png %}

<br/>


    unzip <ConsulFile>

{% asset_img 4.png %}

<br/>


將檔案搬至 /usr/local/bin 下。  

    mv consul /usr/local/bin/consul

{% asset_img 5.png %}

<br/>


Consul 的安裝就完成了，可以簡單的輸入 Consul 命令做個測試。  

{% asset_img 6.png %}

<br/>


Link
----
* [Install Consul | Consul - HashiCorp Learn](https://learn.hashicorp.com/consul/getting-started/install)
* [Download Consul - Consul by HashiCorp](https://www.consul.io/downloads.html)
