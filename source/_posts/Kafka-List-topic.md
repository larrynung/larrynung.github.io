---
title: Kafka - List topic
date: 2018-09-20 23:41:39
tags: [Kafka]
---

要列出 Kafka 的 Topic，可以調用 kafka-topics.sh，帶入參數 --list 指示要列出 topic、--zookeeper 參數指定 ZooKeeper 位置。  

<!-- More -->

    bin/kafka-topics.sh --list --zookeeper localhost:2181

{% asset_img 1.png %}
 
<br/>


Link
---
* [Apache Kafka](https://kafka.apache.org/quickstart)
