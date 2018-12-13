---
title: Consul - Web UI
date: 2018-12-13 23:38:20
tags: [Consul]
---

要啟動 Consul Web UI 可在調用 Consul 命令時帶入 -ui 參數。  

<!-- More -->

    consul agent -dev -ui

{% asset_img 1.png %}

<br/>


訪問 http://<Url>/ui，即可看到 Consul Web UI。  

{% asset_img 2.png %}

<br/>


如果要使用舊的 Consul Web UI 畫面，可將 CONSUL_UI_LEGACY 環境變數設定為 true。  

{% asset_img 3.png %}

<br/>


{% asset_img 4.png %}

<br/>


如果 Consul Web UI 訪問被拒。  

{% asset_img 5.png %}

<br/>


可加帶 -client 設定。  

{% asset_img 6.png %}

<br/>


Link
----
* [Web UI | Consul - HashiCorp Learn](https://learn.hashicorp.com/consul/getting-started/ui)
