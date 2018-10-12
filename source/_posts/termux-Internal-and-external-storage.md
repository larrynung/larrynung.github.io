---
title: termux - Internal and external storage
date: 2018-10-12 08:55:58
tags: [termux]
---

termux 裝完後預設只能看到 termux 空間內的資料，若要讓 termux 能使用到 Android 的內外部空間，需要自行呼叫命令開啟。  

<!-- more -->

</br>


開啟只要呼叫下列命令:  

    termux-setup-storage

{% asset_img 1.jpg %}

</br>


開啟時會確認是否授權，點選允許完成授權動作。  

{% asset_img 2.jpg %}

</br>


命令跑完 termux 下會多個 ~/storage 目錄。

{% asset_img 3.jpg %}

</br>


透過該目錄就可以存取到 Android 的內外部空間了。

</br>


Link
----
* [Internal and external storage](https://wiki.termux.com/wiki/Internal_and_external_storage)
* [Termux-setup-storage](https://wiki.termux.com/wiki/Termux-setup-storage)
