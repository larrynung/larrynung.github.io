---
title: Kafka - Download and start kafka server
date: 2018-09-19 23:26:42
tags: [Kafka]
---

要使用 Kafka  首先須確定環境中有安裝 Java。   

<!-- More -->

<br/>


若沒有的話需先進行安裝。  

{% asset_img 1.png %}
 
<br/>


{% asset_img 2.png %}
 
<br/>


接著下載 Kafka 程式。  

    wget http://ftp.mirror.tw/pub/apache/kafka/2.0.0/kafka_2.11-2.0.0.tgz 

{% asset_img 3.png %}
 
<br/>


將下載下來的 Kafka 程式解壓縮。  

    tar -xzf kafka_2.11-2.0.0.tgz

{% asset_img 4.png %}
 
<br/>


進入解壓縮後的 Kafka 目錄。  

    cd kafka_2.11-2.0.0

{% asset_img 5.png %}
 
<br/>


啟動 ZooKeeper。  

    bin/zookeeper-server-start.sh config/zookeeper.properties

{% asset_img 6.png %}
 
<br/>


啟動 Kafka。  

    bin/kafka-server-start.sh config/server.properties

{% asset_img 7.png %}
 
<br/>


Link
----
* [Apache Kafka](https://kafka.apache.org/quickstart)
