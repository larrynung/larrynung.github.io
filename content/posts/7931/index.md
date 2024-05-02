---
title: "[WPF]WPF初體驗"
date: "2009-04-09 12:39:43"
description: "[WPF]WPF初體驗"
tags: [WPF]
---

<p>
	 </p>
<h2>
	建立專案</h2>
<p>
	檔案=&gt;新增專案=&gt;依需求選取WPF專案範本。</p>
<p>
	<img alt="image" border="0" height="318" src="\images\posts\7931\image_thumb_16.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="554" /></p>
<p>
	 </p>
<h2>
	專案架構</h2>
<p>
	建立完WPF專案後，以WPF應用程式為例，我們可以在方案總管視窗看到方案中已有Application.Xaml、Window1.Xaml、與其Code Behind檔共四個檔案。</p>
<p>
	<img alt="image" border="0" height="180" src="\images\posts\7931\image_thumb_18.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="217" /></a> <a href="http://files.dotblogs.com.tw/larrynung/0904/0f43544950ad_14995/image_36.png"><img alt="image" border="0" height="281" src="\images\posts\7931\image_thumb_17.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="404" /></p>
<p>
	 </p>
<p>
	其中Application.Xaml就有點像是C#應用程式專案中的Program.cs，主要是用來指定一開始要執行的XAML檔。</p>
<p>
	<img alt="image" border="0" height="136" src="\images\posts\7931\image_thumb_19.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="448" /></p>
<p>
	 </p>
<p>
	而Window1.Xaml檔則是主界面檔，主要的畫面是設計在這個檔上面。</p>
<p>
	 </p>
<h2>
	介面操作</h2>
<p>
	開啟WPF專案後，我們可以看到如下畫面。</p>
<p>
	<img alt="image" border="0" height="555" src="\images\posts\7931\image_thumb_1.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="557" /></p>
<p>
	 </p>
<p>
	在編寫WPF程式上，我們可以在『視覺編輯區』放置控制項，並到屬性視窗設定屬性。也可以直接在XAML編輯區使用宣告式的設計方式來設計介面。不論採用哪種設計方式，在編寫時都會影響另一個編輯區。</p>
<p>
	若在編寫時覺得不習慣『視覺編輯區』與『XAML編輯區』的位置，我們可按下兩個編輯區中間的<img alt="image" border="0" height="20" src="\images\posts\7931\image_thumb_5.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="21" />按鈕，把『視覺編輯區』與『XAML編輯區』的位置互換。</p>
<p>
	<img alt="image" border="0" height="23" src="\images\posts\7931\image_thumb_4.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="296" /></p>
<p>
	 </p>
<p>
	互換位置後畫面會變得如下：</p>
<p>
	<img alt="image" border="0" height="300" src="\images\posts\7931\image_thumb_6.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="306" /></p>
<p>
	 </p>
<p>
	也可以透過<img alt="image" border="0" height="20" src="\images\posts\7931\image_thumb_8.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="19" /> 按鈕把編輯區設為垂直分隔。</p>
<p>
	<img alt="image" border="0" height="300" src="\images\posts\7931\image_thumb_7.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="306" /></p>
<p>
	 </p>
<p>
	透過<img alt="image" border="0" height="17" src="\images\posts\7931\image_thumb_9.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="18" /> 按鈕把編輯區設為水平分隔。</p>
<p>
	<img alt="image" border="0" height="300" src="\images\posts\7931\image_thumb_10.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="306" /></p>
<p>
	 </p>
<p>
	或是透過<img alt="image" border="0" height="17" src="\images\posts\7931\image_thumb_11.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="18" /> 按鈕摺疊編輯區。摺完後編輯區將不會分割顯示，而變成可用頁籤來切換的型式。</p>
<p>
	<img alt="image" border="0" height="300" src="\images\posts\7931\image_thumb_12.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="306" /></p>
<p>
	 </p>
<p>
	在用『視覺編輯區』設計介面時，若覺得畫面太大或是太小的話。可透過『視覺編輯區』左上方的縮放條調整畫面大小。</p>
<p>
	 <img alt="image" border="0" height="223" src="\images\posts\7931\image_thumb_15.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="244" /></a> <a href="http://files.dotblogs.com.tw/larrynung/0904/0f43544950ad_14995/image_30.png"><img alt="image" border="0" height="223" src="\images\posts\7931\image_thumb_14.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="244" /></p>
