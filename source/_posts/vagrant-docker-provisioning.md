---
layout: post
title: "Vagrant - Docker Provisioning"
date: 2015-11-01 23:33:00
comments: true
tags: [Vagrant]
keywords: "Vagrant"
description: "Vagrant - Docker Provisioning"
---

Docker Provisioning 可以自動在 Vagrant 啟動時幫我們進行 Docker 的安裝，容器的下載，與容器的設定。

<!-- More -->

<br/>


使用上主要是透過 Vagrantfile 將 config.vm.provision 設為 docker，並利用支援的參數與方法做些對應的設定。  	

<br/>


支援的參數有 images、version。images 用以指定所要拉下來的 Docker 映像檔，跟 pull_images 方法類似。version 則是指定要裝的 docker 版本，若未指定預設是使用最新版本。  

<br/>


支援的方法有 build_image、pull_images、run。build_images 方法可以讓我們把 dockerfile 建立成映像檔。pull_images 方法可以將指定容器下載下來。run 方法可以啟動指定容器。  

<br/>


像是下面這個例子，筆者使用 boot2docker 的 vagrant box，結合 docker provision 拉下 oracle-xe-11g 容器，以守護容器方式啟動，將 1521 port 導出，並掛上 data volume。  

```rb
Vagrant.configure(2) do |config|
  config.vm.box = "blinkreaction/boot2docker"

  config.vm.box_check_update = false

  config.vm.synced_folder "Data", "/home/docker/data", create: true
  config.vm.network "forwarded_port", guest: 1521, host: 1521

  config.vm.provision "docker",
    images:["wnameless/oracle-xe-11g:latest"] do |d|

     d.run "oracle",
     image: "wnameless/oracle-xe-11g",
     args: "-p 1521:1521 -v /home/docker/data:/data",
     daemonize: true
  end
end
```

<br/>

Link
----
* [Docker - Provisioning - Vagrant Documentation](https://docs.vagrantup.com/v2/provisioning/docker.html)
