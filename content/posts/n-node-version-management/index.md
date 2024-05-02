---
title: "n - Node version management"
date: "2017-04-23 10:06:14"
tags: [Node.js]
---


n 是一 Node version management，可以管理 Node.js 的版本。安裝時可先將 npm 的快取清掉。  

<!-- More -->

    sudo npm cache clean -f


![1.png](1.png)

<br/>



然後用 npm 安裝 n 即可。  

    sudo npm install -g n

![2.png](2.png)

<br/>


安裝好後就可以用 n 來進行 Node.js 版本的管理。  

<br/>


像是要使用最新版本的 Node.js。  

    n stable

![3.png](3.png)

<br/>


![4.png](4.png)

<br/>


要使用指定版本的 Node.js。  

    n <version>

![5.png](5.png)

<br/>


要使用最新版本的 Node.js。  

    n latest

![6.png](6.png)

<br/>


要切換已經安裝的 Node.js。  

    n

![7.png](7.png)

<br/>


![8.png](8.png)

<br/>


![9.png](9.png)

<br/>


要移除指定版本的 Node.js。  

    n rm <version>

![10.png](10.png)

<br/>


要移除當前位使用的 Node.js 版本。  

    n prune

![11.png](11.png)

<br/>


Link
----
* [tj/n: Node version management](https://github.com/tj/n)
* [Node.js各作業系統更新方式 - eddychang.me](http://eddychang.me/blog/javascript/58-nodes-update.html)
