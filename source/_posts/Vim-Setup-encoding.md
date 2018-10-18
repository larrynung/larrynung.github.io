---
title: Vim - Setup encoding
date: 2018-10-18 00:14:58
tags: [Vim]
---

使用 Vim 時若因編碼導致文字無法正常顯示。  

<!-- more -->

{% asset_img 1.jpg %}

</br>


可開啟編輯 Vim 的設定檔。  

    vi ~/.vimrc

{% asset_img 2.jpg %}

</br>


加上 encoding 設定後存檔。  

    set encoding = <Encoding>

{% asset_img 3.jpg %}

</br>


Vim 就可以用正確的編碼顯示文字。  

{% asset_img 4.jpg %}
