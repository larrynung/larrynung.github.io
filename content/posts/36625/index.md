---
title: "[Visual Studio]Visual Studio 2011 Preview New Feature - Code Clone Analysis"
date: "2011-09-18 11:30:22"
description: "[Visual Studio]Visual Studio 2011 Preview New Feature - Code Clone Analysis"
tags: [Visual Studio]
---

<p>
	Visual Studio 2011 Preview新增了一個很有趣的功能，稱作Code Clone Analysis，能輔助開發人員搜尋方案中、或是針對特定程式碼片段找尋是否有相似的程式碼。可以用來檢查程式中是否有可提出成共用方法的可能。</p>
<p>
	 </p>
<p>
	使用上可透過Analyze→Analyze Solution for Code Clones觸發檢查動作，透過這邊觸發Code Clone檢查動作可檢查出方案中是否有任何相似的程式存在。</p>
<p>
	<img alt="image" border="0" height="382" src="\images\posts\36625\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="501" /></p>
<p>
	 </p>
<p>
	如果方案中存在有相似的程式碼，會在Code Clone Analysis Results視窗中看到類似下圖的畫面，裡面會顯示不同的Clone Group，Clone Group會依不同的相似等級顯示不同的Match名稱，大致上分為Exact、Strong、Medium、與Weak幾種等級。另外在Clone Group上還會顯示有相似的檔案有幾個，以及裡面找到的相似Cloned Snippets個數。</p>
<p>
	<img alt="image" border="0" height="237" src="\images\posts\36625\image_thumb_1.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="493" /></p>
<p>
	 </p>
<p>
	要進一步查看Cloned Snippets的話，可將Clone Groups展開，並用滑鼠在感興趣的Cloned Snippets上停留，透過彈出的ToolTip來查閱對應的程式碼。</p>
<p>
	<img alt="image" border="0" height="339" src="\images\posts\36625\image_thumb_2.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="651" /></p>
<p>
	 </p>
<p>
	或是直接透過滑鼠左鍵連點讓Visual Studio切至對應的程式碼也可以。</p>
<p>
	<img alt="image" border="0" height="310" src="\images\posts\36625\image_thumb_3.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	另外要提的是，若是想針對特定的程式碼片段查驗是否有相似的程式碼存在，可選取想要查驗的程式碼，透過滑鼠右鍵快顯選單中的Find Matching Clones in Solution快顯選單選項即可。</p>
<p>
	<img alt="image" border="0" height="425" src="\images\posts\36625\image_thumb_5.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="266" src="\images\posts\36625\image_thumb_6.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	這邊筆者試著了解了一下相似度等級的區分規則，因為目前找不到更為詳細的文件，這邊用一些簡單的實驗來試圖釐清。看起來大概是依照程式碼的行數、相似的行數、相異的行數等，套入公式後運算取得相似等級，可能還參雜一些權限的機制。下面附上筆者的測試範例，有興趣的可以稍微看一下。</p>
<p>
	<img alt="image" border="0" height="256" src="\images\posts\36625\image_thumb_7.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="260" src="\images\posts\36625\image_thumb_8.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="254" src="\images\posts\36625\image_thumb_9.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="256" src="\images\posts\36625\image_thumb_12.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="238" src="\images\posts\36625\image_thumb_10.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="224" src="\images\posts\36625\image_thumb_11.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="239" src="\images\posts\36625\image_thumb_13.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
