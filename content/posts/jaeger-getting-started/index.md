---
title: "Jaeger - Getting started"
date: "2020-02-19 07:37:46"
description: "要使用 Jaeger，最簡便的做法是直接使用 Docker 去起 jaegertracing/all-in-one 容器。 docker run -d --name jaeger \\ -e COLLECTOR_ZIPKIN_HTTP_PORT=9411 \\ -p 5775:5775/udp \\…"
tags: [Jaeger]
---

要使用 Jaeger，最簡便的做法是直接使用 Docker 去起 jaegertracing/all-in-one 容器。

docker run -d --name jaeger \
-e COLLECTOR_ZIPKIN_HTTP_PORT=9411 \
-p 5775:5775/udp \
-p 6831:6831/udp \
-p 6832:6832/udp \
-p 5778:5778 \
-p 16686:16686 \
-p 14268:14268 \
-p 9411:9411 \
jaegertracing/all-in-one

![1.png](1.png)

或是從下載頁下載 Jaeger。

![2.png](2.png)

wget https://github.com/jaegertracing/jaeger/releases/download/v1.16.0/jaeger-1.16.0-darwin-amd64.tar.gz

![3.png](3.png)

解壓縮。

tar xf jaeger-1.16.0-darwin-amd64.tar.gz

![4.png](4.png)

![5.png](5.png)

運行 jaeger-all-in-one 啟動 Jaeger 服務。

jaeger-all-in-one --collector.zipkin.http-port=9411

![6.png](6.png)

透過瀏覽器訪問 http://localhost:16686 應該就可以看到 Jaeger 的操作界面。

![7.png](7.png)

Link
====
* [Getting Started — Jaeger documentation](https://www.jaegertracing.io/docs/1.16/getting-started/)