---
title: Redis - Redis cluster with docker and create-cluster script
date: 2020-02-01 16:04:53
tags: [Redis, Docker]
---

透過 Docker 去起 Redis cluster，多半網路上的做法都是用多個容器去做，這邊筆者因為測試與開發上的便利性，試著用一個容器搭配 create-cluster 腳本去起 Redis cluster。  

<!-- More -->

</br>


這邊為了整合 Docker，create-cluster 腳本筆者做了些調整。只留下本來腳本中的 create 與 start 兩個步驟，將兩個步驟合併，並支援透過環境變數帶入 Host 與 Port，另外因為 Redis 不支援 Domain，所以 Host 帶入後會在容器內解析為 IP 後使用。  

```
#!/bin/bash


# Settings
HOSTNAME=${HOSTNAME}
PORT=${PORT}
TIMEOUT=2000
NODES=6
REPLICAS=1
CLUSTER_HOST=$(getent hosts $HOSTNAME | awk '{ print $1 }')


# Create & start
HOSTS=""
ENDPORT=$((PORT+NODES))
CURRENTPORT=$PORT


while [ $((CURRENTPORT < ENDPORT)) != "0" ]; do
    echo "Starting $CURRENTPORT"


    redis-server --port $CURRENTPORT --cluster-enabled yes --cluster-config-file nodes-${CURRENTPORT}.conf --logfile ${CURRENTPORT}.log --daemonize yes


    HOSTS="$HOSTS $CLUSTER_HOST:$CURRENTPORT"
    CURRENTPORT=$((CURRENTPORT+1))
done
echo "yes"| redis-cli --cluster create $HOSTS --cluster-replicas $REPLICAS
```

{% asset_img 1.png %}

</br>


Docker-Compose 檔這邊記得將 create-cluster 掛入，透過環境變數指定 Host 與 Port，開通容器的 Port，並設定容器啟動時運行 create-cluster 腳本。  

```
version: '3'


services:
  redis-cluster:
    image: redis:5.0.7
    volumes:
      - "./create-cluster.sh:/usr/local/bin/redis/create-cluster.sh"
    environment:
      - HOSTNAME=127.0.0.1
      - PORT=6379
    ports:
      - "6379-6384:6379-6384"
    command: bash -c "sh /usr/local/bin/redis/create-cluster.sh && tail -f /dev/null"
```

{% asset_img 2.png %}

</br>


將容器啟動，Redis cluster 沒意外的話會正常運作。  

    docker-compose up

{% asset_img 3.png %}

</br>


運行 Redis cluster info 命令查驗 Redis cluster 的狀態資訊，可看到 cluster_state 是 ok。  

    docker exec $container redis-cli cluster info

{% asset_img 4.png %}

</br>


運行 Redis cluster nodes 命令查驗 Redis cluster 的節點資訊，可看到 Redis cluster 內的節點識別碼、Host、Port、Master or slave、連線狀態、及服務的 Slot 區間。  

    docker exec $container redis-cli cluster nodes

{% asset_img 5.png %}
