---
title: "Run python with SublimeText"
date: "2013-11-06 12:00:00"
description: "Run python with SublimeText"
tags: [Python]
---

<p>
	要在Sublime Text中執行Python，首先我們要將要運行的程式撰寫好，並將程式存成副檔名為py的檔案。</p>
<p>
	 </p>
<p>
	接著開啟Tools/Build/Build System的子選單，我們應該可以看到SublimeText會自動選取到Python這個選項。表示SublimeText知道這段程式是Python的程式，需要用Python去運行。</p>
<p>
	<img alt="screenshot(61)" border="0" height="293" src="\images\posts\dafb0f4c-815a-4c77-84f4-8e05e34f14ff\screenshot(61)_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="428" /></p>
<p>
	 </p>
<p>
	再來可以按下熱鍵Ctrl + b (MAC下按command + b)，或是透過滑鼠點選Tools/Build/Build選單選項，Sublime Text會開始運行我們的Python程式並將結果輸出在下方。</p>
<p>
	<img alt="image" border="0" height="464" src="\images\posts\dafb0f4c-815a-4c77-84f4-8e05e34f14ff\image_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="613" /></p>
<p>
	 </p>
<p>
	這樣的建置功雖然讓我們在SublimeText下開發Python方便了許多，但有的時候我們不太能這樣直接透過SublimeText幫我們運行程式，像是如果我們的程式中用了raw_input這樣的語法，運行後輸出結果那邊就會出現EOF的錯誤，因為輸出結果這邊沒提供我們輸入的功能。</p>
<p>
	<img alt="image" border="0" height="464" src="\images\posts\dafb0f4c-815a-4c77-84f4-8e05e34f14ff\image_thumb_1.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="614" /></p>
<p>
	 </p>
<p>
	像這樣的情況我們就得自行使用Command Line下去叫用Python運行程式。</p>
<p>
	<img alt="image" border="0" height="372" src="\images\posts\dafb0f4c-815a-4c77-84f4-8e05e34f14ff\image_thumb_2.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="511" /></p>
<p>
	 </p>
<p>
	最後這邊要提醒一下，若是程式有確實存檔，副檔名也是.py，但卻無法正常運行Python，這邊我們可能會需要檢查一下設定。點選Preferences/Browse Packages...選單選項。</p>
<p>
	<img alt="screenshot(56)" border="0" height="249" src="\images\posts\dafb0f4c-815a-4c77-84f4-8e05e34f14ff\screenshot(56)_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="431" /></p>
<p>
	 </p>
<p>
	會帶出SublimeText存放套件的目錄，這邊我們要看一下是否可以找到Python的目錄。</p>
<p>
	<img alt="screenshot(58)" border="0" height="374" src="\images\posts\dafb0f4c-815a-4c77-84f4-8e05e34f14ff\screenshot(58)_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	若有找到Python的目錄，我們進一步將Python.sublime-build這個設定檔給開啟。</p>
<p>
	<img alt="screenshot(59)" border="0" height="373" src="\images\posts\dafb0f4c-815a-4c77-84f4-8e05e34f14ff\screenshot(59)_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	該設定檔內會有Python運行時的命令設定，通常我們是不需要特別變動，稍稍檢查一下就好。</p>
<p>
	<img alt="screenshot(60)" border="0" height="150" src="\images\posts\dafb0f4c-815a-4c77-84f4-8e05e34f14ff\screenshot(60)_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="413" /></p>
<p>
	 </p>
<p>
	沒什麼問題的話，應該就是運行Python所需要的直譯器沒有安裝，或是沒有將所在位置寫到環境變數，導致找不到Python命令運行。</p>
