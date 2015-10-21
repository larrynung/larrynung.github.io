---
layout: post
title: "Vagrant - Vagrantfile inheritance"
date: 2015-10-21 05:26
comments: true
categories: [Vagrant]
keywords: "Vagrant, Vagrantfile"
description: "Vagrant - Vagrantfile inheritance"
---

Vagrantfile 的設定跟很多軟體一樣是有繼承關係的。  

<!-- More -->

<br/>


首先他會去看 Vagrant Box 的 Vagrantfile。通常會是在 `%HOMEPATH%\.vagrant.d\boxs` 下，若有設定 VAGRANT_HOME 則是在  `%VAGRANT_HOME%\.vagrant.d\boxs` 下。   

{% img /images/posts/VagrantfileInheritance/1.png %}

<br/>


接著會看 `%HOMEPATH%\.vagrant.d` 或是 `%VAGRANT_HOME%\.vagrant.d\` 下的 Vagrantfile。  

{% img /images/posts/VagrantfileInheritance/2.png %}

<br/>


最後才會看專案目錄下的 Vagrantfile。  

<br/>


通常我們跟著專案跑的設定會設在專案下的 Vagrantfile，若是一些通用的設定或是跟主機環境比較相關的設定，我們會在 `.vagrant.d` 下的 Vagrantfile 設定，像是 Proxy 的設定等。  




Link
----
* [Vagrantfile inheritance | Michael Maclean](http://mgdm.net/weblog/vagrantfile-inheritance/)
