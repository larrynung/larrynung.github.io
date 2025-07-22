---
title: "土豆視頻開發系列-影片播放"
date: "2013-11-06 12:00:00"
description: "土豆視頻開發系列-影片播放"
---

土豆視頻提供的影片播放API其格式如下：

http://www.tudou.com/v/【影片對應的CODE】/&【配置參數】/v.swf

影片對應的CODE土豆視頻開發系列-依影集分類查詢這篇所抓到的影片ItemCode，用來指定所要播放的影片，而配置參數則是用來設定撥放器的行為，有autoPlay、videoClickNavigate、withSearchBar、withFirstFrame、withRecommendList這幾個參數。

autoPlay參數是用來指定當瀏覽到撥放器時要自動開始撥放，為非必要性參數，可接受true跟false這兩個值，預設為false，也就是不自動撥放。

使用上會像下面這樣，可自行點選連結瀏覽效果：

http://www.tudou.com/v/49eeAQ2V6Cs/&autoPlay=false/v.swf

http://www.tudou.com/v/49eeAQ2V6Cs/&autoPlay=true/v.swf

videoClickNavigate參數則是指定點選到播放器時是否要帶到土豆網頁，為非必要性參數，可接受true跟false這兩個值，預設為true。

http://www.tudou.com/v/49eeAQ2V6Cs/&videoClickNavigate=true/v.swf

<img alt="image" border="0" height="487" src="\images\posts