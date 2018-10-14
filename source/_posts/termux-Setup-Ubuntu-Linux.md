---
title: termux - Setup Ubuntu Linux
date: 2018-10-14 21:37:10
tags: [termux]
---

要在 termux 安裝 Ubuntu Linux，首先要下載安裝用的 script。  

<!-- more -->

    curl https://raw.githubusercontent.com/Neo-Oli/termux-ubuntu/master/ubuntu.sh --output ubuntu.sh

{% asset_img 1.jpg %}

</br>


然後運行下載下來的 script 安裝，安裝完會直接進入到 Arch Linux。  

    bash ubuntu.sh

{% asset_img 2.jpg %}

</br>


如果要去 Ubuntu Linux 退出，可調用 exit 命令。

</br>


要再次進入 Ubuntu Linux 的話，只要運行 start-ubuntu.sh 即可。  

{% asset_img 3.jpg %}

</br>


Link
----
* [termux-ubuntu](https://github.com/Neo-Oli/termux-ubuntu)
* [Ubuntu - Termux Wiki](https://wiki.termux.com/wiki/Ubuntu)
