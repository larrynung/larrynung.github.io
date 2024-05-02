---
title: "Logstash - Install Logstash via apt"
date: "2017-05-29 23:40:35"
tags: [Logstash]
---


安裝 Logstash 前，需先確認已有安裝 Java 8。  

<!-- More -->

<br/>


可輸入指令查看 Java 版本。  

    java -version

<br/>


若版本不對，可先進行 Java 8 的安裝。  

    apt-get install python-software-properties

![1.png](1.png)

<br/>


加入 PPA。  

    add-apt-repository -y ppa:webupd8team/java

![2.png](2.png)

<br/>


進行 apt-get 的更新。  

    apt-get update

![3.png](3.png)

<br/>


透過 APT 安裝 Java 8。  

    apt-get -y install oracle-java8-installer

![4.png](4.png)

<br/>


![5.png](5.png)

<br/>


![6.png](6.png)

<br/>


Java 環境準備好後，開始進行 Logstash 的安裝。  

<br/>


設定 repository definition。  

    echo "deb http://packages.elastic.co/logstash/2.1/debian stable main" | sudo tee -a /etc/apt/sources.list.d/logstash-2.x.list

![7.png](7.png)

<br/>


透過 APT 安裝 Logstash。 

    apt-get install logstash

![8.png](8.png)

<br/>


Link
----
* [Installing Logstash | Logstash Reference [5.4] | Elastic](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)
