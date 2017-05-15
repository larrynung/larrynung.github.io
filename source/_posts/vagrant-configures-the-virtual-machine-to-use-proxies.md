---
layout: post
title: "Vagrant - Configures the virtual machine to use proxies"
date: 2015-10-20 04:26:00
comments: true
tags: [Vagrant]
keywords: "Vagrant, Proxy"
description: "Vagrant - Configures the virtual machine to use proxies"
---

要讓 Vagrant 走 Proxy，我們可以借助 vagrant-proxyconf 套件。  

<!-- More -->

<br/>

用  vagrant plugin install 帶入套件名稱 vagrant-proxyconf 進行套件的安裝。  

    vagrant plugin install vagrant-proxyconf

<br/>


{% img /images/posts/ConfigVagrantProxy/1.png %}

<br/>


套件安裝完畢後，我們可以修改 Vagrantfile 做 proxy 的設定。像是下面這樣：  

```rb
...
if Vagrant.has_plugin?("vagrant-proxyconf")
    config.proxy.http     = "http://proxy.xuenn.com:3128/"
    config.proxy.https    = "https://proxy.xuenn.com:3128/"
    config.proxy.no_proxy = "localhost,127.0.0.1"
end
...
```

<br/>


if Vagrant.has_plugin?("vagrant-proxyconf") 用以判斷 vagrant-proxyconf 套件是否有安裝，config.proxy.http 用以設定  http 的 proxy，config.proxy.https 用以設定 https 的 proxy，config.proxy.no_proxy 用以設定不走 proxy 的 domain。  

<br/>


若是 Proxy 需經過認證，設定時要將帳密一併帶入：  

```rb
...
if Vagrant.has_plugin?("vagrant-proxyconf")
deblock %}
    config.proxy.http     = "http://username:password@proxy.xuenn.com:3128/"
    config.proxy.https    = "https://username:password@proxy.xuenn.com:3128/"
    config.proxy.no_proxy = "localhost,127.0.0.1"
end
...
```

<br/>

Link
----
* [tmatilai/vagrant-proxyconf](https://github.com/tmatilai/vagrant-proxyconf/)
* [Setting up vagrant behind a corporate proxy | Failing fast to learn a lot](http://runefs.com/2014/11/28/setting-up-vagrant-behind-a-corporate-proxy/)
