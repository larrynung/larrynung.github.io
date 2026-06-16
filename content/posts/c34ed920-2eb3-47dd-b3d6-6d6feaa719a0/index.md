---
title: "土豆視頻開發系列-影片播放"
date: "2013-11-06 12:00:00"
tags: [土豆視頻]
description: "土豆視頻提供的影片播放API其格式如下： http://www.tudou.com/v/【影片對應的CODE】/&【配置參數】/v.swf 影片對應的CODE土豆視頻開發系列-依影集分類查詢這篇所抓到的影片ItemCode，用來指定所要播放的影片，而配置參數則是用來設定撥放器的行為，"
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

![image_thumb_6.png](/images/posts/c34ed920-2eb3-47dd-b3d6-6d6feaa719a0/image_thumb_6.png)

http://www.tudou.com/v/49eeAQ2V6Cs/&videoClickNavigate=false/v.swf

withSearchBar參數則是指是否要在播放器上方顯示搜尋框，為非必要性參數，可接受true跟false這兩個值，預設為true。

http://www.tudou.com/v/49eeAQ2V6Cs/&withSearchBar=true/v.swf

![image_thumb_3.png](/images/posts/c34ed920-2eb3-47dd-b3d6-6d6feaa719a0/image_thumb_3.png)

http://www.tudou.com/v/49eeAQ2V6Cs/&withSearchBar=false/v.swf

![image_thumb_5.png](/images/posts/c34ed920-2eb3-47dd-b3d6-6d6feaa719a0/image_thumb_5.png)

withFirstFrame參數則是指是否要顯示影片的預覽圖片，為非必要性參數，可接受true跟false這兩個值，預設為true。

http://www.tudou.com/v/49eeAQ2V6Cs/&withFirstFrame=true/v.swf

![image4_thumb.png](/images/posts/c34ed920-2eb3-47dd-b3d6-6d6feaa719a0/image4_thumb.png)

http://www.tudou.com/v/49eeAQ2V6Cs/&withFirstFrame=false/v.swf

![image1_thumb.png](/images/posts/c34ed920-2eb3-47dd-b3d6-6d6feaa719a0/image1_thumb.png)

withRecommendList參數則是指播放器播放完畢後，是否要顯示推薦的影片，為非必要性參數，可接受true跟false這兩個值，預設為true。

http://www.tudou.com/v/49eeAQ2V6Cs/&withRecommendList=false/v.swf

![image_thumb.png](/images/posts/c34ed920-2eb3-47dd-b3d6-6d6feaa719a0/image_thumb.png)
