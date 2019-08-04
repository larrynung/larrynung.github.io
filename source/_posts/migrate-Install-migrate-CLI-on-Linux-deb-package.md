---
title: migrate - Install migrate CLI on Linux (*.deb package)
date: 2019-08-03 21:08:02
tags: [migrate]
---

要在 Linux 上安裝 migrate，先將 migrate 的金鑰加入。  

<!-- More -->

    curl -L https://packagecloud.io/golang-migrate/migrate/gpgkey | apt-key add -

{% asset_img 1.png %}

</br>


將 migrate 加入套件來源清單。  

    echo "deb https://packagecloud.io/golang-migrate/migrate/ubuntu/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/migrate.list

{% asset_img 2.png %}

</br>


更新套件清單。

    apt-get update

{% asset_img 3.png %}

</br>


進行 migrate 套件安裝。  

    apt-get install -y migrate

{% asset_img 4.png %}

</br>


最後調用命令查閱 migrate 版本，確認安裝無誤。  

    migrate -version

{% asset_img 5.png %}

</br>


Link
=====
* [migrate CLI](https://github.com/golang-migrate/migrate/tree/master/cmd/migrate)
