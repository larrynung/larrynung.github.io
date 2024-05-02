---
title: "安裝並啟動transmission server，讓網樂通變身BT下載機"
date: "2013-11-06 12:00:00"
description: "安裝並啟動transmission server，讓網樂通變身BT下載機"
---

<p>
	網樂通改機成功後，若想要讓網樂通變身BT下載機，我們可以為網樂通加掛transmission server。這篇稍微紀錄一下要怎樣才能透過sh4twbox為網樂通加掛transmission。</p>
<p>
	 </p>
<p>
	首先我們必須連進網樂通，並參閱[網樂通改機][sh4twbox]如何使用shpkg去做套件的安裝與管理這篇，或是直接呼叫命令"shpkg -S transmission-cli"，將transmission套件安裝起來。</p>
<p>
	<img alt="image" border="0" height="225" src="\images\posts\db492636-a756-4e18-829e-fa47008d137f\image_thumb_3.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="582" /></p>
<p>
	 </p>
<p>
	安裝完成後記得要呼叫命令shpkg -E檢查是否有相依的套件需要安裝。</p>
<p>
	<img alt="image" border="0" height="284" src="\images\posts\db492636-a756-4e18-829e-fa47008d137f\image_thumb_4.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="581" /></p>
<p>
	 </p>
<p>
	這邊應該會找到需要安裝的相依套件，會提示我們要按下Enter安裝相依的套件，直接按下Enter繼續即可。</p>
<p>
	<img alt="image" border="0" height="350" src="\images\posts\db492636-a756-4e18-829e-fa47008d137f\image_thumb_5.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="582" /></p>
<p>
	 </p>
<p>
	相依的套件也安裝完後，若是整個流程都沒有什麼意外的話，套件就算正常的安裝上去了。</p>
<p>
	<img alt="image" border="0" height="351" src="\images\posts\db492636-a756-4e18-829e-fa47008d137f\image_thumb_6.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="580" /></p>
<p>
	 </p>
<p>
	接著呼叫"/etc/init.d/transmission-daemon start"將服務啟動，讓transmission幫我們產生設定檔到/root/Downloads/transmission/settings.json這個位置。然後呼叫命令"vi /root/Downloads/transmission/settings.json"做些設定，像是連線進去控制是要走哪個Port、檔案要下載到哪個目錄等等。這邊要特別注意到rpc-whitelist跟rpc-whitelist-enabled這兩個設定，rpc-whitelist是設定允許連進去控制的IP，而rpc-whitelist-enabled則是是否啟動白名單功能。要記得把IP改成要使用瀏覽器連進去網樂通的那台電腦IP，或是將白名單功能關閉，不然在用瀏覽器連進去時會被拒絕。</p>
<p>
	<img alt="image" border="0" height="349" src="\images\posts\db492636-a756-4e18-829e-fa47008d137f\image_thumb_13.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="579" /></p>
<p>
	<img alt="image" border="0" height="349" src="\images\posts\db492636-a756-4e18-829e-fa47008d137f\image_thumb_14.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="580" /></p>
<p>
	 </p>
<p>
	設定完後我們可以呼叫"/etc/init.d/transmission-daemon stop"將服務停止，並再次叫用"/etc/init.d/transmission-daemon start"命令將服務啟動，讓transmission重新載入設定。</p>
<p>
	 </p>
<p>
	啟動後我們實際用瀏覽器連接看看，輸入網樂通的網址，並指定Port為9091(假設上面的設定沒改過的話)，像是筆者的網樂通IP為192.168.0.104，就要帶入http://192.168.0.104:9091這串網址到瀏覽器的網址列。理論上我們會看到類似下面這樣的管理畫面，透過這個簡易的管理頁面，我們可以將BT的種子指定給網樂通進行下載。</p>
<p>
	<img alt="image" border="0" height="567" src="\images\posts\db492636-a756-4e18-829e-fa47008d137f\image_thumb_12.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="667" /></p>
<p>
	<img alt="image" border="0" height="567" src="\images\posts\db492636-a756-4e18-829e-fa47008d137f\image_thumb_10.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="666" /></p>
<p>
	 </p>
<p>
	最後這邊要再提醒一下，像上面這樣啟動沒問題後，若是希望每次網樂通通電就可以使用這樣的功能，我們必須要參閱[網樂通改機]網樂通運行時自動啟動指定的服務這篇，將要啟動的命令寫在/etc/rc.local裡面。</p>
<p>
	<img alt="image" border="0" height="386" src="\images\posts\db492636-a756-4e18-829e-fa47008d137f\image_thumb_9.png" width="611" /></p>
