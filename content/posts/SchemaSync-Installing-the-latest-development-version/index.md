---
title: "SchemaSync - Installing the latest development version"
date: "2019-08-10 12:46:19"
tags: [SchemaSync]
---


要安裝 SchemaSync 最新的開發版，先將 SchemaSync 用 git clone 下來。

<!-- More -->

    git clone git://github.com/mmatuson/SchemaSync.git


![1.png](1.png)

</br>


然後切到 clone 下來的目錄。 

    cd SchemaSync


![2.png](2.png)

</br>


透過 Python 調用 setup.py 進行安裝。  

    sudo python setup.py install


![3.png](3.png)

</br>


安裝完可調用命令查驗版本，確認安裝無誤。  

    schemasync -V


![4.png](4.png)

</br>


Link
=====
* [Schema Sync a MySQL Schema Versioning and Migration Utility](http://mmatuson.github.io/SchemaSync/)
