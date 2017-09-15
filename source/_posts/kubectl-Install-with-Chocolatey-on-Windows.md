---
title: kubectl - Install with Chocolatey on Windows
date: 2017-09-15 23:52:13
tags: [kubectl]
---

要在 Windows 使用 kubectl，透過 Chocolatey 進行安裝即可。  

<!-- More -->

    choco install kubernetes-cli

{% asset_img 1.png %}

<br/>


安裝完可運行 kubectl 命令查閱 kubectl 版本，確認命令可以正確運行。  

    kubectl version

{% asset_img 2.png %}

<br/>


Link
----
* [Install and Set Up kubectl - Kubernetes](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
