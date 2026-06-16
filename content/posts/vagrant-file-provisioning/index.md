---
title: "Vagrant - File Provisioning"
date: "2015-11-03 00:06:00"
description: "File Provisioning 可以讓我們自動在 Vagrant 啟動時將檔案傳遞至虛擬機中。 使用上主要是透過 Vagrantfile 將 config.vm.provision 設為 file，並利用支援的參數與方法做些對應的設定。 支援的參數有 source、 destination。"
tags: [Vagrant]
---

File Provisioning 可以讓我們自動在 Vagrant 啟動時將檔案傳遞至虛擬機中。

使用上主要是透過 Vagrantfile 將 config.vm.provision 設為 file，並利用支援的參數與方法做些對應的設定。

支援的參數有 source、 destination。source 參數指定的是本機上的來源檔案位置，destination 參數指定的是虛擬機上的目標檔案位置。

像是這邊，若要將本地的 shell script 帶入到虛擬機中。

![1.png](/images/posts/VagrantFileProvisioning/1.png)

Provisioning 運行後虛擬機就會將指定的檔案帶到指定的位置。

![2.png](/images/posts/VagrantFileProvisioning/2.png)

Link
----
* [File Uploads - Provisioning - Vagrant Documentation](https://docs.vagrantup.com/v2/provisioning/file.html)