---
title: "Bower - Bower install"
date: "2016-01-14 09:57:00"
description: "Bower install 可用來安裝 bower 的 package 以及其依類的套件。 使用方式如下： bower install bower install bower install # bower install 會依據 bower.json 的設定下去安裝 bower 套件。"
tags: [Bower]
---

Bower install 可用來安裝 bower 的 package 以及其依類的套件。

使用方式如下：

bower install
bower install
bower install #

bower install 會依據 bower.json 的設定下去安裝 bower 套件。

如果指定安裝 bower 套件，可以直接在 bower install 後接上 bower 套件的名稱。像是要安裝 jQuery，我們就可以下 bower install jquery。

![1.png](/images/posts/BowerInstall/1.png)

![2.png](/images/posts/BowerInstall/2.png)

如果要安裝特定版本的 bower 套件，就是在 bower install 後接上 bower 套件名稱，再用 # 串接 bower 套件的版本。像是 bower install jquery#2.2.0。

如果想在安裝時一併寫入 bower.json 檔，可加帶 --save。