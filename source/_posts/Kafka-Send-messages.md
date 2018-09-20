---
title: Kafka - Send messages
date: 2018-09-21 00:04:48
tags: [Kafka]
---

要使用 Kafka 發送訊息到指定的 Topic，可以調用 kafka-console-producer.sh，帶入參數 --broker-list 指定 broker 的位置、--topic 參數指定 topic。  

<!-- More -->

    bin/kafka-console-producer.sh --broker-list [Broker] --topic [Topic]

{% asset_img 1.png %}
 
<br/>


Link
----
* [Apache Kafka](https://kafka.apache.org/quickstart)
