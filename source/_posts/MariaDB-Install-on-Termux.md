---
title: MariaDB - Install on Termux
date: 2019-06-24 08:51:39
tags: [MariaDB, Termux]
---

在 Termux 安裝 MariaDB，可透過 pkg 或是 apt 安裝。  

<!-- More -->

    pkg install MariaDB

{% asset_img 1.png %}

</br>


安裝完調用 mysql_install_db 命令安裝資料庫。  

    mysql_install_db

{% asset_img 2.png %}

</br>


調用 mysqld 命令啟動服務。  

    mysqld

{% asset_img 3.png %}

</br>


在另一個 Session 調用 mysql 命令即可連進 MariaDB。  

    mysql

{% asset_img 4.png %}
