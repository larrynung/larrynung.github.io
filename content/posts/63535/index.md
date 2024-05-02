---
title: "[C++]使用Visual Leak Detector for Visual C++ 2008/2010輔助偵測程式中記憶體洩漏的問題"
date: "2011-12-27 12:52:07"
description: "[C++]使用Visual Leak Detector for Visual C++ 2008/2010輔助偵測程式中記憶體洩漏的問題"
tags: [C++]
---

<p>
	Visual Leak Detector for Visual C++ 2008/2010</a>是一免費的開放源碼工具，能輔助開發人員偵測C++程式中記憶體洩漏的問題，使用上也算十分簡單，至<a href="http://vld.codeplex.com/" target="_blank">Visual Leak Detector for Visual C++ 2008/2010下載主程式後。</p>
<p>
	<img alt="image" border="0" height="580" src="\images\posts\63535\image_thumb_4.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="602" /></p>
<p>
	 </p>
<p>
	安裝後會在Program Files(x86)下找到安裝的程式，裡面比較重要的就是bin、lib跟include幾個目錄，bin目錄存放dll組件，lib存放靜態函式庫，include則是存放著標頭擋。</p>
<p>
	<img alt="image" border="0" height="468" src="\images\posts\63535\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="598" /></p>
<p>
	 </p>
<p>
	這邊以靜態函式庫為例，先開啟專案的屬性，在Additional Dependencies這邊設定lib檔的位置。</p>
<p>
	<img alt="image" border="0" height="436" src="\images\posts\63535\image_thumb_1.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	Additional Include Directories這邊設定include目錄位置。</p>
<p>
	<img alt="image" border="0" height="436" src="\images\posts\63535\image_thumb_2.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	都設定好後在程式中加入vld.h檔的引用，建置後執行程式，當關閉時偵測的結果就會顯現在輸出視窗中。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:c60da7b3-feb7-45ba-84f3-d029685be41f" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
#include "vld.h"</pre>
</div>
<p>
	 </p>
<p>
	這邊筆者示範個簡潔的範例，程式碼如下：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e4291b58-f836-4256-9202-08ba1f2efa10" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
// Test_VisualLeakDetector.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "vld.h"

int _tmain(int argc, _TCHAR* argv[])
{
	char* buffer = new char[512];
	return 0;
}</pre>
</div>
<p>
	 </p>
<p>
	運行後關閉，在輸出視窗就會顯現像下面這樣的偵測結果，不僅僅每個偵測到的Leak都會有當下的呼叫堆疊與記憶體資訊，也會列出簡單的統計資訊，像是總共發現的leak數、最大記憶體用量、與總共花費的記憶體。若要修正偵測到的Memory leak，可點擊感興趣的call stack，程式碼會自動跳至對應的位置。</p>
<p>
	<img alt="image" border="0" height="685" src="\images\posts\63535\image_thumb_3.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="618" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		Visual Leak Detector for Visual C++ 2008/2010</li>
</ul>
