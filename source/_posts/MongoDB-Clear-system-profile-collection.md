---
title: MongoDB - Clear system.profile collection
date: 2019-09-21 22:24:15
tags: [MongoDB]
---

在做 MongoDB 的 Profiling 時，有時我們會需要清除 system.profile collection 內的資料。  

<!-- More -->

</br>


像是這邊筆者已經有資料在 system.profile collection 內。

    db.system.profile.count()

{% asset_img 1.png %}

</br>


要將 system.profile collection 清除，先要將 Profiler 關閉，也就是透過 db.setProfilingLevel 將 Profiling 等級設為 0。  

    db.setProfilingLevel(0)

{% asset_img 2.png %}

</br>


然後 drop system.profile collection。  

    db.system.profile.drop()

{% asset_img 3.png %}

</br>


{% asset_img 4.png %}

</br>


Link
=====
* [profiling - How to delete system.profile collection from a MongoDB? - Stack Overflow](https://stackoverflow.com/questions/24908047/how-to-delete-system-profile-collection-from-a-mongodb)
