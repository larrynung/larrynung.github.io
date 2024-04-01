---
title: "[Visual Studio]Visual Studio 2011 Preview Black Screen Issue"
date: "2013-11-06 12:00:00"
description: "[Visual Studio]Visual Studio 2011 Preview Black Screen Issue"
---

<p>
	筆者在使用Visual Studio 2011 Preview時有時會出現黑色畫面，這問題困擾筆者許久，今天終於將重現步驟抓出了，將其整理於這篇。</p>
<p>
	 </p>
<p>
	重現步驟如下：</p>
<p>
	Step1.開啟Visual Studio 2011 Preview</p>
<p>
	Step2.開啟Output Window</p>
<p>
	Step3.拖出Output Window將其最大化</p>
<p>
	<img alt="image" border="0" height="245" src="\images\posts\8fa5a9c9-4b67-4385-914a-784aea41035e\image_thumb_1.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	Step4.保持這樣的狀態直接關閉Visual Studio 2011 Preview(可以透過工作列將之關閉)</p>
<p>
	Step5.開啟Visual Studio 2011 Preview</p>
<p>
	Step6.按工作列圖示將它縮小再放大</p>
<p>
	 </p>
<p>
	然後會發現本來顯示好好的輸出視窗就會全部黑掉。</p>
<p>
	<img alt="image" border="0" height="245" src="\images\posts\8fa5a9c9-4b67-4385-914a-784aea41035e\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	在筆者的電腦，當黑掉後重新建置，黑掉的部分又會正常顯示。若你也為這問題苦惱，可以嚐試用這方法先頂一下，但是最好還是先避開上面的使用方式。</p>
<p>
	 </p>
<p>
	這邊筆者有請Bill叔幫忙確認一下這個Issue，在Win8的環境下好像黑掉後會Stop working ，有興趣的可以自行試驗看看。</p>
