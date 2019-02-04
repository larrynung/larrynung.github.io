---
title: Consul - Registering services
date: 2018-12-11 00:38:22
tags: [Consul]
---

要使用 Consul 註冊服務，先準備一個目錄用來存放 Consul 的設定。  	

<!-- More -->

    mkdir <ConfigDir>

{% asset_img 1.png %}

<br/>


在建立的設定檔目錄內放置 Consul 的設定檔，設定檔內會指定服務的名稱、Tag、與服務的 Port。  

    {"service": {"name": "<Name>", "tags": ["<Tag>"], "port": <Port>}}

{% asset_img 2.png %}

<br/>


設定檔準備好後，啟動 Consul agent，使用 -config-dir 參數指定設定檔目錄。  

    consul agent -dev -config-dir=<ConfigDir>

{% asset_img 3.png %}

<br/>


{% asset_img 4.png %}

<br/>


啟動後可用 DNS API 做個測試。  

    dig @<IP> -p <Port> <ServiceName>.service.consul

{% asset_img 5.png %}

<br/>


{% asset_img 6.png %}

<br/>


或是用 HTTP API 測試也可以。  

    curl http://<IP>/v1/catalog/service/<ServiceName>

{% asset_img 7.png %}

<br/>


Link
----
* [Registering Services | Consul - HashiCorp Learn](https://learn.hashicorp.com/consul/getting-started/services)
