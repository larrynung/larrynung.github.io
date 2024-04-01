---
title: "Puppet - Install puppet server via apt"
date: "2017-07-19 23:49:47"
tags: [Puppet]
---


要透過 apt 安裝 Pupper server，需要開啟 package repository。  

<!-- More -->

<br/>


首先要先依作業系統的版本下載 puppetlabs-release。  

<br/>


Ubuntu 12.04  

    curl -O https://apt.puppetlabs.com/puppetlabs-release-precise.deb

<br/>


Ubuntu 14.04  

    curl -O https://apt.puppetlabs.com/puppetlabs-release-trusty.deb


![1.png](1.png)

<br/>


下載完用 dpkg 安裝下載的套件。  

    dpkg -i <PACKAGE NAME>

![2.png](2.png)

<br/>


安裝完更新 apt 套件的清單。  

    sudo apt-get update

![3.png](3.png)

<br/>


最後用 apt 安裝 puppetserver 即可。  

    sudo apt-get install puppetserver

![4.png](4.png)

<br/>


Link
----
* [Installing Puppet: Debian and Ubuntu — Documentation — Puppet](https://docs.puppet.com/puppet/3.8/install_debian_ubuntu.html#step-2-install-puppet-on-the-puppet-master-server)
