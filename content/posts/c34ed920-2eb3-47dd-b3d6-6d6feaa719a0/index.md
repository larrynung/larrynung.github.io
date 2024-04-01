---
title: "土豆視頻開發系列-影片播放"
date: "2013-11-06 12:00:00"
description: "土豆視頻開發系列-影片播放"
---

<p>
	土豆視頻提供的影片播放API其格式如下：</p>
<p>
	http://www.tudou.com/v/【影片對應的CODE】/&amp;【配置參數】/v.swf</p>
<p>
	 </p>
<p>
	影片對應的CODE土豆視頻開發系列-依影集分類查詢這篇所抓到的影片ItemCode，用來指定所要播放的影片，而配置參數則是用來設定撥放器的行為，有autoPlay、videoClickNavigate、withSearchBar、withFirstFrame、withRecommendList這幾個參數。</p>
<p>
	 </p>
<p>
	autoPlay參數是用來指定當瀏覽到撥放器時要自動開始撥放，為非必要性參數，可接受true跟false這兩個值，預設為false，也就是不自動撥放。</p>
<p>
	 </p>
<p>
	使用上會像下面這樣，可自行點選連結瀏覽效果：</p>
<p>
	http://www.tudou.com/v/49eeAQ2V6Cs/&amp;autoPlay=false/v.swf</p>
<p>
	http://www.tudou.com/v/49eeAQ2V6Cs/&amp;autoPlay=true/v.swf</p>
<p>
	 </p>
<p>
	videoClickNavigate參數則是指定點選到播放器時是否要帶到土豆網頁，為非必要性參數，可接受true跟false這兩個值，預設為true。</p>
<p>
	http://www.tudou.com/v/49eeAQ2V6Cs/&amp;videoClickNavigate=true/v.swf</p>
<p>
	<img alt="image" border="0" height="487" src="\images\posts