---
title: "Consul - Run the Consul agent"
date: "2018-12-07 23:14:32"
tags: [Consul]
---

要簡單的將 Consul agent 跑起來玩玩，可以用 development 模式將 Consul agent 跑起來。

consul agent -dev

![1.png](1.png)

跑起來後可用 members 指令查閱節點。

consul members

![2.png](2.png)

或是用 HTTP API 查閱。

curl /v1/catalog/nodes

![3.png](3.png)

抑或是用 DNS 去查詢。

dig @ -p

![4.png](4.png)

要停止 Consul agent 的話用熱鍵 Ctrl + C 即可。

Link
----
* [Run the Consul Agent | Consul - HashiCorp Learn](https://learn.hashicorp.com/consul/getting-started/agent)