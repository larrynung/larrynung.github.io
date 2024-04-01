---
title: "MaxToCode"
date: "2010-12-29 03:13:32"
description: "MaxToCode"
tags: [.NET Resource]
---

<p>
	MaxToCode為一.NET程式碼核級保護軟體，能為程式加上混淆或加密，保護程式碼不被有心人事惡意破解。取得授權後會拿到一個硬體鎖與金鑰，透過金鑰可到指定位置下載正式版本的MaxToCode，安裝完即可開始使用MaxToCode，需特別注意在使用上要先插入MaxToCode硬體鎖，再將MaxToCode正式版本軟體開啟，MaxToCode軟體才會變為正式版本。</p>
<p>
	 </p>
<p>
	開啟MaxToCode後，我們可以看到如下頁面，介面設計的十分簡潔好用，主要功能分為幾個頁面，像是常規選項、強命名選項、Web應用選項、與授權管理等，主要要做加密的組件可透過常規選項頁面下方的【增加...】按鈕加入至頁面下半部的程序集列表，也可透過拖曳的方式加入。頁面上半部有些細部資訊可供設定，像是保存目錄可用以指式保護完的檔案要放置的位置，運行庫名可用以設定用以保護用的類別庫檔案名稱，是否要將用以保護用的類別庫與檔案合併，是否支援64位元...等等，若想細部微調混淆的部份，可在頁面下方的程序集列表中的項目上，用滑鼠左鍵連點兩次，在彈出的編輯對話框下去修改即可。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\20449\image1_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="588" /></p>
<p>
	 </p>
<p>
	這邊提到的用以保護用的類別庫檔案，若不特別處理，其組件資訊會以其保護程式預設的為主，因為預設的資料是固定的資訊，有心人士可從中判斷你的保護機制為何，造成被惡意破解的風險。在MaxToCode中，我們可以透過頁面下半部的【隱藏保護者】的按鈕，修改保護用的類別庫檔案資訊，藉此增加破解上的難度。</p>
<p>
	<img alt="image" border="0" height="272" src="\images\posts\20449\image18_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="523" /></p>
<p>
	 </p>
<p>
	在強命名頁面中，主要是用以設定要簽署的強命名，若要保護的組件本身有做強命名的簽署動作，可在此處設定強命名金鑰的位置，讓MaxToCode可以在做完保護後重新為組件簽署強命名。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\20449\image9_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="588" /></p>
<p>
	 </p>
<p>
	Web應用選項頁面則是做些Web方面的設定...</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\20449\image12_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="588" /></p>
<p>
	 </p>
<p>
	授權管理頁面則用來為組件加入一些授權的機制，像是限制試用的日期，與限制使用的次數...等。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\20449\image15_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="588" /></p>
<p>
	 </p>
<p>
	都設定好後，我們可以按下頁面下方【執行加密】按鈕，MaxToCode就會開始幫我們依照設定下去做加密的動作，加密後的檔案會產生在所設定的保存目錄。</p>
<p>
	 </p>
<p>
	此外，MaxToCode也支援命令列的控制方式，其參數如下：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:0422f0f1-d4f1-4ad9-ab2a-49ee5b1d7e19" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="xml" name="code">
	-?  or -help        顯示幫助 

-project=&lt;projectfile&gt;    從 MaxtoCode 項目文件中的信息開始加密 (.mcproj) 

                -p 參數不可以與其它參數共同使用 

-out=&lt;out directory&gt;        加密后的程序集輸出目錄 

-runtime=&lt;Mruntime3.dll&gt;    運行庫名稱 

-bind                合并運行庫 

-string            加密用戶字符串 

-blob                加密用戶blob信息 

-resource            加密用戶資源 

-new                加密構造函數 

-support64            支持64位操作系統 

-autoconfusion        自動混淆當前程序集，如沒此選項都不混淆程序集 

-metaconfusion        混淆原數據 

-strongname=&lt;snk file&gt;    使用引命名簽此文件 

-weboptimize            如果是Web相關程序，請帶上此參數</pre>
</div>
<p>
	 </p>
<p>
	使用上我們可依自身的需求下去撰寫保護用的命令，像是：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:5f9c6f56-5034-4b9e-a925-ae39b2b76f1b" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="xml" name="code">
	MaxToCode.Exe -project="MaxToCodeProject.mcproj"</pre>
</div>
<p>
	 </p>
<p>
	MaxToCode的使用上就是那麼簡單，但是需注意的是，透過MaxToCode保護後的組件會被MaxToCode限制住所能支援的OS與.NET Framework版本，也就是說程式給客戶後可能會因客戶的自行升級，造成程式無法正常運作，感覺上會有點失去跨平台的優勢。至於要怎樣確認電腦可否正常運行保護後的程式，或是判斷是否為環境造成的問題，我們可以開啟MaxToCode附的小工具去檢查，像下方就可明顯看到Windows Version與Framework Version顯示著Passed。</p>
<p>
	<img alt="image" border="0" height="400" src="\images\posts\20449\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<p>
	另外一提MaxToCode也附帶了一個String To Byte的小工具，可用以輔助開發人員將程式中一些敏感字串做些保護。</p>
<p>
	<img alt="image" border="0" height="423" src="\images\posts\20449\image3_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
