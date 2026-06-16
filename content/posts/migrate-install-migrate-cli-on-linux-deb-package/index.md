---
title: "migrate - Install migrate CLI on Linux (*.deb package)"
date: "2019-08-03 21:08:02"
description: "要在 Linux 上安裝 migrate，先將 migrate 的金鑰加入。 curl -L https://packagecloud.io/golang-migrate/migrate/gpgkey | apt-key add - 將 migrate 加入套件來源清單。"
tags: [migrate]
---

要在 Linux 上安裝 migrate，先將 migrate 的金鑰加入。

curl -L https://packagecloud.io/golang-migrate/migrate/gpgkey | apt-key add -

![1.png](1.png)

將 migrate 加入套件來源清單。

echo "deb https://packagecloud.io/golang-migrate/migrate/ubuntu/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/migrate.list

![2.png](2.png)

更新套件清單。

apt-get update

![3.png](3.png)

進行 migrate 套件安裝。

apt-get install -y migrate

![4.png](4.png)

最後調用命令查閱 migrate 版本，確認安裝無誤。

migrate -version

![5.png](5.png)

Link
=====
* [migrate CLI](https://github.com/golang-migrate/migrate/tree/master/cmd/migrate)