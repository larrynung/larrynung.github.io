---
title: "Deploy Google App Engine's Application to cloud with appcfg.py"
date: "2013-11-06 12:00:00"
description: "Deploy Google App Engine's Application to cloud with appcfg.py"
---

<p>
	參閱筆者Registering Google App Engine's Application這篇，當你跟Google App Engine註冊完一個Application後，用對應的網址連上去應該會像下面這張圖一樣回應Server Error。這是因為我們還未將Application佈署到Cloud上所導致。</p>
<p>
	<img alt="image" border="0" height="128" src="\images\posts\26e8ea9a-dad3-4ad5-941e-0fc146d1d50a\image_thumb_1.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	若是在本地撰寫好了Application，經過測試無誤，我們就可以準備將Application佈署到Cloud上了。</p>
<p>
	 </p>
<p>
	在佈署前我們必須要開啟Application內的app.yaml檔案，確定application這邊的設定跟我們當時註冊的Application ID是一致的，像是筆者當初註冊的Application ID是levelupapp1，app.yaml這邊的application設定就必須要是levelupapp1，這樣佈署時Google App Engine才能做個對應，才知道是要佈署到哪邊。</p>
<p>
	<img alt="image" border="0" height="470" src="\images\posts\26e8ea9a-dad3-4ad5-941e-0fc146d1d50a\image_thumb_3.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	app.yaml的設定確定無誤後，我們可以開啟命令提示字元，呼叫命令appcfg updeate [Application Folder] (或是python appcfg updeate [Application Folder])，開始進行佈署動作，佈署的同時會要求輸入Google的帳號密碼，輸入完後等它運行結束，佈署的動作就完成了。</p>
<p>
	<img alt="image" border="0" height="349" src="\images\posts\26e8ea9a-dad3-4ad5-941e-0fc146d1d50a\image_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="581" /></p>
<p>
	 </p>
<p>
	佈署到Cloud後我們可以再次用當初註冊的Application網址來測試看看，沒意外的話應該會看到我們的Application確實的運行在Cloud上面。</p>
<p>
	<img alt="image" border="0" height="114" src="\images\posts\26e8ea9a-dad3-4ad5-941e-0fc146d1d50a\image_thumb_2.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="304" /></p>
