---
title: >-
  Vagrant - The VirtualBox VM was created with a user that doesn't match the
  current user running Vagrant
date: 2017-05-01 17:39:22
tags: [Vagrant]
---

在使用 Vagrant 時如果出現'The VirtualBox VM was created with a user that doesn't match the current user running Vagrant' 的錯誤。  

<!-- More -->

{% asset_img 1.png %}

<br/>


可以開啟 '.vagrant\machines\default\virtualbox\creator_uid'。  

{% asset_img 2.png %}

<br/>


將數值設為錯誤訊息中告知當初用來建立 VM 的 UID 後存檔。  

{% asset_img 3.png %}

<br/>


再次運行 Vagrant，沒意外的話應該就可以正常使用了。  

{% asset_img 4.png %}

<br/>


Link
----
* [Vagrant – User doesn’t match | My snippets](https://mysnippets443.wordpress.com/2015/09/25/vagrant-user-doesnt-match/)
