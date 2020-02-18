---
title: Redis - Setup redis cluster
date: 2020-02-07 08:27:09
tags: [Redis]
---

這邊紀錄一下如何不透過 create-cluster 腳本一步一步建立 Redis cluster。  

<!-- More -->

<br>


首先安裝 Redis，這邊為了方便筆者是直接使用 Docker 去起 Redis 容器。  

    docker run -it redis bash

{% asset_img 1.png %}

<br>


這邊為了測試方便，會讓六個 Redis instance 放在同一個容器。所以這邊筆者建立一個目錄便於後續操作。

    mkdir cluster-test

{% asset_img 2.png %}

<br>


    cd cluster-test

{% asset_img 3.png %}

<br>


接著為每個 Redis instance 建立目錄。

    mkdir 7000 7001 7002 7003 7004 7005

{% asset_img 4.png %}

<br>


每個 Redis instance 放置對應的 Redis 設定。  

    cd 7000

{% asset_img 5.png %}

<br>


    apt-get update && apt-get install vim

{% asset_img 6.png %}

<br>


    vim redis.conf

{% asset_img 7.png %}

<br>


設定檔內記得設定 Redis instance 的 port 號與 cluster。  

```
port 7000
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
```

{% asset_img 8.png %}

<br>


調用 redis-server 命令，指定設定檔，啟動 Redis instance。  

    redis-server redis.conf --daemonize yes

{% asset_img 9.png %}

<br>


再透過 redis-cli 帶入 --cluster 參數與 Redis instance 的位置，指定要串成 cluster 的 Redis instance，並透過 --cluster-replicate 指定 slave 份數。  

    redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 --cluster-replicas 1

{% asset_img 10.png %}

<br>


指定的 Redis instance 就會串成 Redis cluster。

{% asset_img 11.png %}

<br>


運行 Redis cluster info 命令查驗 Redis cluster 的狀態資訊，可看到 cluster_state 是 ok。    

    redis-cli -p 7000 cluster info

{% asset_img 12.png %}

<br>


運行 Redis cluster nodes 命令查驗 Redis cluster 的節點資訊，可看到 Redis cluster 內的節點識別碼、Host、Port、Master or slave、連線狀態、及服務的 Slot 區間。  

    redis-cli -p 7000 cluster nodes

{% asset_img 13.png %}

<br>


Link
=====
* [Redis cluster tutorial – Redis](https://redis.io/topics/cluster-tutorial)
