---
title: Flyway - Install on Linux
date: 2019-07-29 21:09:09
tags: [Flyway]
---

Flyway 要在 Linux 上使用，可到 Flyway 的下載頁面，複製 Linux 上要運行的命令。  

<!-- More -->

{% asset_img 1.png %}

</br>


運行命令，會進行檔案的下載、解壓縮、建立連結。  

    wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/5.2.4/flyway-commandline-5.2.4-linux-x64.tar.gz | tar xvz && ln -s `pwd`/flyway-5.2.4/flyway /usr/local/bin 

{% asset_img 2.png %}

</br>


進到 Flyway 目錄調用命令，查驗 Flyway 版本，確認安裝正確無誤。  

    flyway -v

{% asset_img 3.png %}

