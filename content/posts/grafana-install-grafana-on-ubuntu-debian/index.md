---
title: "Grafana - Install Grafana on Ubuntu  Debian"
date: "2019-02-26 00:10:05"
description: "參照 Grafana Download page。 下載 Grafana 套件。 wget https://dl.grafana.com/oss/release/grafana_6.0.0_amd64.deb 安裝 Grafana 套件。"
tags: [Grafana]
---

參照 [Grafana Download page](https://grafana.com/grafana/download)。

![1.png](1.png)

下載 Grafana 套件。

wget https://dl.grafana.com/oss/release/grafana_6.0.0_amd64.deb

![2.png](2.png)

安裝 Grafana 套件。

sudo dpkg -i grafana_6.0.0_amd64.deb

![3.png](3.png)

啟動 Grafana 服務。

sudo service grafana-server start

![4.png](4.png)

訪問 http://localhost:3000，輸入預設帳密 admin/admin。

![5.png](5.png)

更換預設帳號的密碼。

![6.png](6.png)

就可以開始使用 Grafana 了。

![7.png](7.png)