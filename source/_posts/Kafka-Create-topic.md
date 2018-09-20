---
title: Kafka - Create topic
date: 2018-09-20 23:29:20
tags: [Kafka]
---

要建立 Kafka 的 Topic，可以調用 kafka-topics.sh，帶入 --create 參數指定創建 topic、--zookeeper 參數指定 zookeeper 位置、--topic 參數指定要創建的 topic。  

<!-- More -->

    bin/kafka-topics.sh --create --zookeeper [ZooKeeper] --replication-factor [ReplicationFactor] --partitions [Partitions] --topic [Topic]

{% asset_img 1.png %}
 
<br/>


Link
----
* [Apache Kafka](https://kafka.apache.org/quickstart)
