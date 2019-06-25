---
title: Termux - nginx
date: 2018-10-15 08:38:15
tags: [Termux, nginx]
---

要在 Termux 內使用 nginx，首先要透過套件管理工具安裝 nginx 套件。  

<!-- more -->

    nginx install nginx

{% asset_img 1.jpg %}

</br>


安裝完輸入命令啟動。  

    nginx

{% asset_img 2.jpg %}

</br>


啟動後服務會在背景運行，可以用查詢看看 process 是否有起來。  

    ps | grep nginx

{% asset_img 3.jpg %}

</br>


服務有正常起來到話訪問 http://127.0.0.1:8080 就可以看到 nginx 的歡迎頁面。  

{% asset_img 4.jpg %}

</br>


如果要關閉 nginx 服務，可調用...

    fuser -k 8080/tcp

{% asset_img 5.jpg %}
