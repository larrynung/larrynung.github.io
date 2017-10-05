---
title: Gitea - Install from binary
date: 2017-10-05 23:07:06
tags: [Gitea]
---

要透過二進制黨進行 Gitea 的安裝，可將 Gitea 二進制黨拉下來。  

<!-- More -->

    wget -O gitea https://dl.gitea.io/gitea/1.0.0/gitea-1.0.0-linux-amd64

{% asset_img 1.png %}

<br/>


調整權限。  

    chmod +x gitea

{% asset_img 2.png %}

<br/>


啟用 Gitea 服務即可。  

    ./gitea web

{% asset_img 3.png %}

<br/>


{% asset_img 4.png %}

<br/>


Link
----
* [從二進制安裝- Docs](https://docs.gitea.io/zh-cn/install-from-binary/)
