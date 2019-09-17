---
title: MongoDB - Enable and configure database pofiling
date: 2019-09-16 07:52:49
tags: [MongoDB]
---

要設定或啟用 MongoDB Profiler 功能去能監控較慢的運行，可先進入 MongoDB。  

<!-- More -->

    mongo

{% asset_img 1.png %}

</br>


切到指定資料庫。  

    use $db

</br>


透過 db.setProfilingLevel 設定 Profiling 的層級與定義耗費多少毫秒是慢的處理。  

    db.setProfilingLevel($level, $slowms)

{% asset_img 2.png %}

</br>


設定完可用 db.getProfilingLevel 查驗設定的 Profiling 層級。

    db.getProfilingLevel()

{% asset_img 3.png %}

</br>


或是用 db.getProfilingStatus 查驗整個 Profiling 設定。

    db.getProfilingStatus()

{% asset_img 4.png %}

</br>


設定無誤，實際運行程式，MongoDB Profiler 就會依 Profiling 的設定幫我們抓出慢的操作。  

</br>


Profiler 抓出的資料會被放置在 db.system.profile，可對此操作查閱。  

    db.system.profile.find().pretty()

{% asset_img 5.png %}
