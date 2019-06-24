---
title: MariaDB - Secure MariaDB server with mysql_secure_installation command
date: 2019-06-24 13:21:22
tags: [MariaDB]
---

MariaDB 安裝完後可調用 mysql_secure_installation 命令進行一連串的安全性設定。  

<!-- More -->

    mysql_secure_installation

{% asset_img 1.png %}

</br>


像是 root 的密碼。  

{% asset_img 2.png %}

</br>


是否移除匿名使用者?  

{% asset_img 3.png %}

</br>


是否允許 root 帳號遠端登入?

{% asset_img 4.png %}

</br>


移除測試用資料庫?

{% asset_img 5.png %}

</br>


是否重新載入設定?

{% asset_img 6.png %}

</br>


照著設定完 MariaDB 就會有基本的安全性在。  
