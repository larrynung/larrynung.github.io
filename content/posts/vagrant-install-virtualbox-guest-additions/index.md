---
title: "Vagrant - Install VirtualBox Guest Additions"
date: "2018-02-27 14:28:14"
tags: [Vagrant]
---

OS Kernal 更新，可能會造成 Vagrant 無法正常使用，像是筆者切換了不同 Domain 的 AD帳號後，嘗試使用 Vagrant 就會出錯。

![1.png](1.png)

這時我們可以嘗試重新安裝 VirtualBox Guest Additions。

vagrant plugin install vagrant-vbguest

![2.png](2.png)

![3.png](3.png)

![4.png](4.png)

重新安裝完 Vagrant 就可以正常使用了。

![5.png](5.png)