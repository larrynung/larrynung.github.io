---
title: SonarQube - Setup MySQL database
date: 2017-02-15 23:05:24
tags: [SonarQube]
---

要讓 SonarQube 使用 MySQL 資料庫，需先在伺服器中安裝 MySQL 資料庫。  

<!-- More -->

<br/>


接著要設定 MySQL 資料庫，可先將下列 SQL 語法存放至副檔名為 SQL 的檔案 (這邊筆者選用 create_database.sql)。  

```sql
CREATE DATABASE sonar CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER sonar@localhost IDENTIFIED BY 'password';
CREATE USER sonar@'%' IDENTIFIED BY 'password';
GRANT ALL ON sonar.* TO sonar@localhost;
GRANT ALL ON sonar.* TO sonar@'%';
```

{% asset_img 1.png %}

<br/>


接著使用 `mysql -u -root -p < create_database.sql` 將 SQL 送到 MySQL 運行。  

{% asset_img 2.png %}

<br/>


然後要設定 SonarQube 的設定檔 sonar.properties，sonar.jdbc.username 與 sonar.jdbc.password 這邊要設定 MySQL 的帳密，sonar.jdbc.url 設定這邊要將註解拿掉。   

{% asset_img 3.png %}

<br/>


最後將 SonarQube 服務重啟就可以了。  

{% asset_img 4.png %}

<br/>


Link
----
* [Installing the Server - SonarQube Documentation - SonarQube](https://docs.sonarqube.org/display/SONAR/Installing+the+Server)
* [Solaris 10: how to install SonarQube and perform a basic configuration | Luca Merello's blog](https://lucamerello.wordpress.com/2014/08/06/solaris-10-how-to-install-sonarqube-and-perform-a-basic-configuration/)
