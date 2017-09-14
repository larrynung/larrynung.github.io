---
title: kubectl - Install kubectl binary via curl on Linux
date: 2017-09-14 22:38:14
tags: [kubectl]
---

要在 Linux 安裝 kubectl，可以透過 curl 下載 kubectl。  

<!-- More -->

<br/>


如果要使用最新的版本的可調用下列命令。  

    curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

<br/>


{% asset_img 1.png %}

<br/>


如果要使用指定版本，可像下面這樣調用。  

    curl -LO https://storage.googleapis.com/kubernetes-release/release/[Version]/bin/linux/amd64/kubectl

<br/>


像是要使用 1.7.0 版，可調用下列命令。  

    curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.7.0/bin/linux/amd64/kubectl

<br/>


下載下來後修改 kubectl 執行檔權限，設上執行權限。  

    chmod +x ./kubectl

{% asset_img 2.png %}

<br/>


然後搬移 kubectl 到 /usr/local/bin/kubectl 下。  

    sudo mv ./kubectl /usr/local/bin/kubectl

{% asset_img 3.png %}

<br/>


運行 kubectl 命令查閱 kubectl 版本，確認命令可以正確運行。  

    kubectl version

{% asset_img 4.png %}

<br/>


Link
----
* [Install and Set Up kubectl - Kubernetes](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
