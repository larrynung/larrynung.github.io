---
title: "安裝stlinux23-sh4-python套件，讓網樂通具備運行Python的能力"
date: "2013-11-06 12:00:00"
description: "安裝stlinux23-sh4-python套件，讓網樂通具備運行Python的能力"
tags: [Python]
---

<p>
	網樂通改機成功後，若想要讓網樂通可以支援運行Python的能力，我們可以為網樂通加掛stlinux23-sh4-python套件。這篇稍微紀錄一下要怎樣才能透過sh4twbox為網樂通加掛stlinux23-sh4-python套件。</p>
<p>
	 </p>
<p>
	首先我們必須連進網樂通，並參閱[網樂通改機][sh4twbox]如何使用shpkg去做套件的安裝與管理這篇，或是直接呼叫命令"shpkg -S stlinux23-sh4-python"，將Python套件安裝起來。</p>
<p>
	<img alt="image" border="0" height="222" src="\images\posts\84095ada-078b-4b9e-87e5-fe33600df5f6\image_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="592" /></p>
<p>
	 </p>
<p>
	安裝完成後記得要呼叫命令shpkg -E檢查是否有相依的套件需要安裝。</p>
<p>
	<img alt="image" border="0" height="295" src="\images\posts\84095ada-078b-4b9e-87e5-fe33600df5f6\image_thumb_1.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="592" /></p>
<p>
	 </p>
<p>
	這邊應該會找到需要安裝的相依套件，會提示我們要按下Enter安裝相依的套件，直接按下Enter繼續即可。</p>
<p>
	<img alt="image" border="0" height="372" src="\images\posts\84095ada-078b-4b9e-87e5-fe33600df5f6\image_thumb_2.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="593" /></p>
<p>
	 </p>
<p>
	相依的套件也安裝完後，若是整個流程都沒有什麼意外的話，套件就算正常的安裝上去了。</p>
<p>
	<img alt="image" border="0" height="373" src="\images\posts\84095ada-078b-4b9e-87e5-fe33600df5f6\image_thumb_3.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="593" /></p>
<p>
	 </p>
<p>
	實際呼叫命令python進入指令互動環境測試看看，沒意外的話應該可像下圖一般運作良好。</p>
<p>
	<img alt="image" border="0" height="210" src="\images\posts\84095ada-078b-4b9e-87e5-fe33600df5f6\image_thumb_4.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="592" /></p>
