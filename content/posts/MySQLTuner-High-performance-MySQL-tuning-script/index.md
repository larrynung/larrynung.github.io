---
title: "MySQLTuner - High performance MySQL tuning script"
date: "2019-07-13 20:25:32"
tags: [MySQL]
---


MySQLTuner 是用 Perl 撰寫的腳本，可用來分析 MySQL 或是 MariaDB 的設定，給予效能上的建議。  

<!-- More -->

</br>


將 MySQLTuner 下載下來。  

    wget https://github.com/major/MySQLTuner-perl/tarball/master

![1.png](1.png)

</br>


解壓縮。  

    tar xf master

![2.png](2.png)

</br>


進到解完壓縮的目錄。  

    cd major-MySQLTuner-perl-037f720

![3.png](3.png)

</br>


輸入命令可分析資料庫的設定並給予建議，只要針對最下方的建議或是前面是 !! 的下去處理即可。  

    ./mysqltuner.pl 
    ./mysqltuner.pl --user $user --pass $password

![4.png](4.png)
