---
title: "Redis - Redis cluster with create-cluster script"
date: "2019-12-13 08:42:43"
tags: [Redis]
---


Redis 安裝完後 utils/create-cluster 目錄下有提供現成的腳本可以用來起 Redis cluster 做些測試。  

<!-- More -->

</br>


使用方式可參閱目錄下的 README。  

![1.png](1.png)

</br>


![2.png](2.png)

</br>


或是直接調用命令參考命令的說明。  

    ./create-cluster

![3.png](3.png)

</br>


簡單來說，可以用 start 將要組成 Redis cluster 的節點都先運行起來。  

    ./create-cluster start

![4.png](4.png)

</br>


再用 create 將運行起來的 Redis 連結組成 Cluster。  

    ./create-cluster create

![5.png](5.png)

</br>


![6.png](6.png)

</br>


若有需要，可用 watch 監看 Redis 的輸出。  

    ./create-cluster watch

![7.png](7.png)

</br>


如 Redis log 過多，可用 clean-logs 清除 Redis log。

    ./create-cluster clean-logs

</br>


不使用時可用 stop 停止 Redis 服務。  

    ./create-cluster stop

![8.png](8.png)

</br>


再用 clean 將 Redis 的 資料、設定、Log 都清除。

    ./create-cluster clean

![9.png](9.png)

</br>


![10.png](10.png)
