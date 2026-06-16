---
title: "Vagrant - Global Status"
date: "2015-11-11 00:41:00"
description: "Vagrant box 一多，常常會 Vagrant up 後就忘 Vagrant halt，虛擬機就在背後持續運行。 這時我們可以呼叫 global-status 命令查詢當前使用者所有 Vagrant 虛擬機的使用狀況。"
tags: [Vagrant]
---

Vagrant box 一多，常常會 Vagrant up 後就忘 Vagrant halt，虛擬機就在背後持續運行。

這時我們可以呼叫 global-status 命令查詢當前使用者所有 Vagrant 虛擬機的使用狀況。

Vagrant globl-status

![1.png](/images/posts/VagrantGlobalStatus/1.png)

會顯示 id、name、provider、status、directory 這些資訊，藉此我們可以找到正在運行的 Vagrant box 所在目錄，切換過去將之關閉.

Link
----
* [vagrant global-status - Command-Line Interface - Vagrant Documentation](https://docs.vagrantup.com/v2/cli/global-status.html)