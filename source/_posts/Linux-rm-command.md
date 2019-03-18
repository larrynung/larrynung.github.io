---
title: Linux - rm command
date: 2019-03-18 08:30:58
tags: [Linux]
---

rm 命令提供 Linux 系統檔案刪除的功能。  

<!-- More -->

<br/>


可直接不帶參數調用命令查閱使用方式。  

    rm

{% asset_img 1.jpg %}

<br/>


要移除指定檔案可以直接在命令後帶入檔案位置調用。  

    rm [File]

{% asset_img 2.jpg %}

<br/>


加帶參數 -i 讓刪除前再做一次確認。  

    rm -i [File]

{% asset_img 3.jpg %}

<br/>


刪除的位置可帶入多組，也可以使用萬用字元的方式模糊指定。   

    rm [Filter]

{% asset_img 4.jpg %}

</br>


若是要刪除目錄，可加帶參數 -r。  

    rm -r [Folder]

{% asset_img 5.jpg %}
