---
title: gollum - Install on Ubuntu
date: 2019-07-03 08:34:42
tags: [gollum]
---

要在 Ubuntu 安裝 gollum，可先透過 apt-get 安裝必要套件。  

<!-- More -->

    apt-get install ruby ruby-dev make zlib1g-dev libicu-dev build-essential git cmake

{% asset_img 1.png %}

</br>


然後透過 RubyGems 安裝 gollum 即可。  

    gem install gollum

{% asset_img 2.png %}

</br>


Link
===
* [Installation - gollum / gollum](https://github.com/gollum/gollum/wiki/Installation)
