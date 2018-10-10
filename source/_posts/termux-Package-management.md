---
title: termux - Package management
date: 2018-10-09 19:44:34
tags: [termux]
---

termux 除了可以使用 apt & apt-get 來做套件管理外，也提供 pkg 來做套件管理。  

<!--More-->

</br>


使用方式可直接帶入 help 命令查閱。  

    pkg help

{% asset_img 1.jpg %}

</br>


像是可用 search 命令搜尋是否有指定套件可供安裝。  

    pkg search <query>

{% asset_img 2.jpg %}

</br>


找到指定套件後可用 show 命令進一步查看套件資訊。  

    pkg show <packages>

{% asset_img 3.jpg %}

</br>


套件安裝可用 install 命令，並帶入要安裝的套件。
 
     pkg install <packages>

{% asset_img 4.jpg %}

</br>


安裝完後可用 list-installed 命令做個檢查。  

    pkg list-installed

{% asset_img 5.jpg %}

</br>


Link
----
* [Package Management](https://wiki.termux.com/wiki/Package_Management)
