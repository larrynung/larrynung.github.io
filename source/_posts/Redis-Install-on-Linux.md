---
title: Redis - Install on Linux
date: 2019-12-11 07:39:47
tags: [Redis]
---

要在 Linux 安裝 Redis，可先將 Redis 下載下來。  

<!-- More -->

    wget http://download.redis.io/redis-stable.tar.gz

{% asset_img 1.png %}

</br>


解壓縮下載下來的檔案。  

    tar xvzf redis-stable.tar.gz

{% asset_img 2.png %}

</br>


進到解壓縮後產出的目錄。  

    cd redis-stable

{% asset_img 3.png %}

</br>


進行編譯(若無法編譯，請安裝 Make 與 gcc 套件)。

    Make

{% asset_img 4.png %}

</br>


編譯完成使用 utils 下的內建腳本進行 Redis 服務的設定與啟用。  

    ./utils/install_server.sh

{% asset_img 5.png %}

</br>


{% asset_img 6.png %}

</br>


最後實際用 redis-cli 測試確認一下 Redis 服務正常運行即可。

    src/redis-cli ping

{% asset_img 7.png %}
