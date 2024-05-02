---
title: "Docker - Stop/remove all containers"
date: "2020-03-05 08:37:45"
tags: [Docker， Linux]
---


Docker 容器開多了沒關，要一次停掉可以用 docker ps 命令查閱所有容器，將容器資訊帶給 docker stop，一次停掉。  

<!-- More -->

    docker stop $(docker ps -a -q)

![1.png](1.png)

<br>


    docker ps

![2.png](2.png)

<br>


要一次殺掉可以用 docker ps 命令查閱所有容器，將容器資訊帶給 docker rm，一次殺掉。

    docker rm -f $(docker ps -a -q)

![3.png](3.png)

<br>


    docker ps -a

![4.png](4.png)

<br>


Link
=====
* [Stop / remove all Docker containers (Example)](https://coderwall.com/p/ewk0mq/stop-remove-all-docker-containers)
