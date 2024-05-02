---
title: "[IADP]IADP Advertising - 為應用程式添加廣告"
date: "2011-06-15 11:12:01"
description: "[IADP]IADP Advertising - 為應用程式添加廣告"
tags: [CSharp]
---

<p>
	經過上一篇[IADP]IADP Advertising - 開發前的準備的介紹，相信對廣告服務已經有了初步的了解，也已經可以取得開發所需的SiteID與ZoneID。接著就是要將廣告放置到應用程式中了。此時我們必須要到Intel AppUp Developer Program網站，點選[Develop]→[Component Catalog]選單選項。</p>
<p>
	<img alt="image" border="0" height="273" src="\images\posts\28613\image3_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	找到並下載In-App Advertising and Monetization (C#)這個元件。</p>
<p>
	<img alt="image" border="0" height="384" src="\images\posts\28613\image6_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	<img alt="image" border="0" height="420" src="\images\posts\28613\image9_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	下載下來後安裝起來，安裝的檔案會被放置C:\Program Files\mOcean\mOcean Intel CS SDK。安裝目錄中會含有程式範例、說明文件、參考用的組件、與範例檔。</p>
<p>
	 </p>
<p>
	接著我們將廣告控制項加入工具箱，在工具箱上按下滑鼠右鍵，在彈出的右鍵快顯選單中選取[Choose items...]選單選項，在彈出的Choose Toolbox Items對話框中，按下[Browse...]按鈕，選取"C:\Program Files\mOcean\mOcean Intel CS SDK\Lib\Release\mOceanWindows.dll"。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\28613\image_thumb_5.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	再按一下[OK]按鈕。</p>
<p>
	<img alt="image" border="0" height="463" src="\images\posts\28613\image_thumb_8.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	AdViewControl控制項就會放置在工具箱中。</p>
<p>
	<img alt="image" border="0" height="244" src="\images\posts\28613\image_thumb_4.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="207" /></p>
<p>
	 </p>
<p>
	將AdViewControl控制項拖曳放置應用程式，調整放置想要顯示廣告的位置。</p>
<p>
	<img alt="image" border="0" height="552" src="\images\posts\28613\image_thumb_6.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="587" /></p>
<p>
	 </p>
<p>
	設定AdViewControl控制項的屬性，最重要的是要將申請的SiteID與ZoneID帶入屬性值中，其它還有很多有用的屬性可依自己需求下去設定，像是InternalBrowser可以設定瀏覽廣告時是以內建的瀏覽視窗來瀏覽。</p>
<p>
	<img alt="image" border="0" height="503" src="\images\posts\28613\image_thumb_7.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="581" /></p>
<p>
	 </p>
<p>
	還是以預設的瀏覽器來開啟 、DefaultImage設定廣告載入前所要顯示的預設圖片、UpdateTime設定幾秒自動重讀廣告...等。</p>
<p>
	 </p>
<p>
	設定好屬性後，必須在適當的時間點呼叫AdViewControl.Update來顯示廣告。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:b76fcbc5-d375-4c18-87a4-683def7d7290" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
public MainForm()
{
	...
	InitializeComponent();            

	adViewControl1.Update();
	...
}</pre>
</div>
<p>
	 </p>
<p>
	在運行時，若是要做測試的動作，必須將參考的"C:\Program Files\mOcean\mOcean Intel CS SDK\Lib\Release\mOceanWindows.dll"組件，替換為"C:\Program Files\mOcean\mOcean Intel CS SDK\Lib\Debug\mOceanWindows.dll"組件，因為該廣告元件也是Intel AppUp的程式，也必須經過Intel AppUp的認證，而Debug版的組件用的Application ID是除錯用的，模擬器才能認證通過。</p>
<p>
	 </p>
<p>
	另外除了控制項外，該廣告元件還提供了一個簡單的廣告視窗，簡單的說其實就是一個表單內含剛剛介紹的廣告控制項(AdinterstitialForm.Control)，並附加一些屬性方便我們做些細部的控制而以，像是可以帶入關閉按鈕、可以指定多久後才彈出關閉按鈕...等。使用上也十分簡單，比較要注意的是在建立完表單後，必須透過AdinterstitialForm.Control.Site與AdinterstitialForm.Control.Zone帶入我們申請的SiteID與ZoneID。簡單的程式範例如下：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:1454f555-3a27-447b-b7fa-088161f0bf0f" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
...
var dlg = new AdInterstitialForm();
dlg.Control.Site = "8061";
dlg.Control.Zone = "16112";
using (Button btn = new Button())
{
    btn.Size = new Size(50, 20);
    btn.Text = "Close";
    btn.Location = new Point(10, 10);
    btn.Visible = false;
    dlg.CloseButton = btn;
    dlg.CloseButtonShowTime = 2;
    dlg.ShowDialog();
}
...</pre>
</div>
<p>
	 </p>
<p>
	若有意進一步了解的，這邊強烈建議參閱SDK附的說明文件，位置在"C:\Program Files\mOcean\mOcean Intel CS SDK\mOcean_Intel_CS_SDK_Documentation.pdf"，該說明文件對於控制項的屬性、方法，與廣告視窗都較為詳細的介紹。</p>
<p>
	<img alt="image" border="0" height="433" src="\images\posts\28613\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="565" /></p>
