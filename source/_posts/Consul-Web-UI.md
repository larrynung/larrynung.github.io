---
title: Consul - Web UI
date: 2018-12-13 23:38:20
tags: [Consul]
---

要啟動 Consul Web UI 可在調用 Consul 命令時帶入 -ui 參數，如果是用開發人員模式 (帶入-dev 參數)，-ui 參數可忽略不帶。  

<!-- More -->

    consul agent -dev -ui

{% asset_img 1.png %}

<br/>


訪問 `http://<Url>/ui`，即可看到 Consul Web UI。  

{% asset_img 2.png %}

<br/>


如果要使用舊的 Consul Web UI 畫面，可將 CONSUL_UI_LEGACY 環境變數設定為 true。  

{% asset_img 3.png %}

<br/>


在次起動 Consul Agent，會看到 Consul Web UI 畫面變成舊版畫面。  

{% asset_img 4.png %}

<br/>


如果運行環境比較複雜的(像是筆者在 Vagrant 的虛擬機內啟用 Consul Agent)，在啟用 Consul Web UI 後可能會有訪問被拒的現象。  

{% asset_img 5.png %}

<br/>


在 Consul Agent 起動時再加帶 -client 參數應該就可以了。  

    consul agent -dev -ui 

{% asset_img 6.png %}

<br/>


Link
----
* [Web UI | Consul - HashiCorp Learn](https://learn.hashicorp.com/consul/getting-started/ui)
