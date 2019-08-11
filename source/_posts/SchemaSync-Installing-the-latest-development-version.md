---
title: SchemaSync - Installing the latest development version
date: 2019-08-10 12:46:19
tags: [SchemaSync]
---

要安裝 SchemaSync 最新的開發版，先將 SchemaSync 用 git clone 下來。  

<!-- More -->

    git clone git://github.com/mmatuson/SchemaSync.git

{% asset_img 1.png %}

</br>


然後切到 clone 下來的目錄。

    cd SchemaSync

{% asset_img 2.png %}

</br>


透過 Python 調用 setup.py 進行安裝。  

    sudo python setup.py install

{% asset_img 3.png %}

</br>


安裝完可調用命令查驗版本，確認安裝無誤。  

    schemasync -V

{% asset_img 4.png %}

</br>


Link
=====
* [Schema Sync a MySQL Schema Versioning and Migration Utility](http://mmatuson.github.io/SchemaSync/)
