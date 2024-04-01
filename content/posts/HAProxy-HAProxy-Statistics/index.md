---
title: "HAProxy - HAProxy Statistics"
date: "2019-02-19 00:23:32"
tags: [HAProxy]
---


要啟動 HAProxy Statistics，需將 HAProxy 設定檔開啟進行設定。  

<!-- More -->

    sudo vim /etc/haproxy/haproxy.cfg

![1.png](1.png)

<br/>


將設定檔加上如下設定：  

```
# HAProxy Statistics
listen  stats
        bind :9000
        mode http
        stats enable  # Enable stats page
        stats hide-version  # Hide HAProxy version
        stats realm Haproxy\ Statistics  # Title text for popup window
        stats uri /haproxy_stats  # Stats URI
        stats auth Username:Password  # Authentication credentials
```

![2.png](2.png)

<br/>


設定檔的 bind、uri 與 auth 資訊需視需要調動。  

<br/>


接著調用命令啟動 HAProxy。  

    sudo service haproxy start

![3.png](3.png)

<br/>


訪問設定的 HAProxy Statistics 網址。  

![4.png](4.png)

<br/>


帶入設定檔 auth 那邊設定的帳密。  

<br/>


就可以看到 HAProxy Statistics 的報表頁面。  

![5.png](5.png)
