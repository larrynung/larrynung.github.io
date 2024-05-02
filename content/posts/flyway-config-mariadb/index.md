---
title: "Flyway - Config MariaDB"
date: "2019-07-29 22:26:35"
tags: [Flyway]
---


Flyway 要連結 MariaDB，可開啟 Flyway 設定檔。  

<!-- More -->

    vim conf/flyway.conf

</br>


設定 MariaDB 的位置與帳密。位置部分可遵循下列格式:  

    jdbc:mariadb://host:port/database

</br>


設定上會像下面這樣:  

    flyway.url=jdbc:mariadb://localhost:3306/db1
    flyway.user=root
    flyway.password=pass.123

![1.png](1.png)
