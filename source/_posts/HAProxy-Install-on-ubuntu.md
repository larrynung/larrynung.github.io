---
title: HAProxy - Install on ubuntu
date: 2019-02-19 00:06:20
tags: [HAProxy]
---

要在 Ubuntu 使用 HAProxy，可直接透過 apt-get 進行 HAProxy 的安裝。  

<!-- More -->

    apt-get install haproxy

{% asset_img 1.png %}

<br/>


安裝完後可調用命令並帶入參數 -v 確認安裝無誤。   

    haproxy -v

{% asset_img 2.png %}
