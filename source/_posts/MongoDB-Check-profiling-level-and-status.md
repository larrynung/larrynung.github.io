---
title: MongoDB - Check profiling level and status
date: 2019-09-17 23:35:33
tags: [MongoDB]
---

MongoDB 在設定好 Profiler 後，可用 db.getProfilingLevel 查驗設定的 Profiling 層級。      
<!-- More -->

    db.getProfilingLevel()                 

{% asset_img 1.png %}                       

</br>                                      


或是用 db.getProfilingStatus 查驗整個 Profiling 設定。                                  

    db.getProfilingStatus()                 

{% asset_img 2.png %}
