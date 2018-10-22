---
title: Vim - Display line numbers
date: 2018-10-20 23:56:45
tags: [Vim]
---

Vim 預設 Line number 是關閉的。  

<!-- more -->

{% asset_img 1.jpg %}

</br>


如有需要將開啟 Vim 的設定檔。  

    vi ~/.vimrc

{% asset_img 2.jpg %}

</br>


在設定檔內加上設定開啟 Line number。  

    set number

{% asset_img 3.jpg %}

</br>


再次進入 Vim 就會看到 Line number 已被開啟。  

{% asset_img 4.jpg %}

</br>


如果只是暫時要開關 Line number，可以不用修改到設定檔。    

</br>


可以直接輸入命令暫時開啟。  

    set number

{% asset_img 5.jpg %}

</br>


    set nu

{% asset_img 6.jpg %}

</br>


或是直接輸入命令暫時關閉。  

    set nonumber

{% asset_img 7.jpg %}

</br>


    set nonu

{% asset_img 8.jpg %}

</br>


Link
----
* [Display line numbers](http://vim.wikia.com/wiki/Display_line_numbers)
