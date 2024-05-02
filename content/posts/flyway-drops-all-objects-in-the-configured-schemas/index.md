---
title: "Flyway - Drops all objects in the configured schemas"
date: "2019-08-01 20:09:20"
tags: [Flyway]
---


Flyway 的 Clean 功能能將資料庫內所有東西都清除，不論是 Table、View、還是 Procedure。  

<!-- More -->

![1.png](1.png)

</br>


通常用在測試 Migration 時。  

</br>


像是這邊有一個已經 Migration 過的資料庫。

![2.png](2.png)

</br>


Clean 以後...

    flyway clean

![3.png](3.png)

</br>


資料庫內的資料都會被清掉。  

![4.png](4.png)

</br>


我們就可以調整 Migration，重新將 Migration migrate 到資料庫，反覆操作，藉此將 Migration 調到我們預期的效果。  
