---
title: "[IADP]IADP Advertising - 為應用程式添加廣告"
date: "2011-06-15 11:12:01"
description: "[IADP]IADP Advertising - 為應用程式添加廣告"
tags: [CSharp]
---

經過上一篇[IADP]IADP Advertising - 開發前的準備的介紹，相信對廣告服務已經有了初步的了解，也已經可以取得開發所需的SiteID與ZoneID。接著就是要將廣告放置到應用程式中了。此時我們必須要到Intel AppUp Developer Program網站，點選[Develop]→[Component Catalog]選單選項。

	找到並下載In-App Advertising and Monetization (C#)這個元件。

	下載下來後安裝起來，安裝的檔案會被放置C:\Program Files\mOcean\mOcean Intel CS SDK。安裝目錄中會含有程式範例、說明文件、參考用的組件、與範例檔。

	接著我們將廣告控制項加入工具箱，在工具箱上按下滑鼠右鍵，在彈出的右鍵快顯選單中選取[Choose items...]選單選項，在彈出的Choose Toolbox Items對話框中，按下[Browse...]按鈕，選取"C:\Program Files\mOcean\mOcean Intel CS SDK\Lib\Release\mOceanWindows.dll"。

	再按一下[OK]按鈕。

	AdViewControl控制項就會放置在工具箱中。

	將AdViewControl控制項拖曳放置應用程式，調整放置想要顯示廣告的位置。

	設定AdViewControl控制項的屬性，最重要的是要將申請的SiteID與ZoneID帶入屬性值中，其它還有很多有用的屬性可依自己需求下去設定，像是InternalBrowser可以設定瀏覽廣告時是以內建的瀏覽視窗來瀏覽。

	還是以預設的瀏覽器來開啟 、DefaultImage設定廣告載入前所要顯示的預設圖片、UpdateTime設定幾秒自動重讀廣告...等。

	設定好屬性後，必須在適當的時間點呼叫AdViewControl.Update來顯示廣告。

public MainForm()
{
	...
	InitializeComponent();            

	adViewControl1.Update();
	...
}

	在運行時，若是要做測試的動作，必須將參考的"C:\Program Files\mOcean\mOcean Intel CS SDK\Lib\Release\mOceanWindows.dll"組件，替換為"C:\Program Files\mOcean\mOcean Intel CS SDK\Lib\Debug\mOceanWindows.dll"組件，因為該廣告元件也是Intel AppUp的程式，也必須經過Intel AppUp的認證，而Debug版的組件用的Application ID是除錯用的，模擬器才能認證通過。

	另外除了控制項外，該廣告元件還提供了一個簡單的廣告視窗，簡單的說其實就是一個表單內含剛剛介紹的廣告控制項(AdinterstitialForm.Control)，並附加一些屬性方便我們做些細部的控制而以，像是可以帶入關閉按鈕、可以指定多久後才彈出關閉按鈕...等。使用上也十分簡單，比較要注意的是在建立完表單後，必須透過AdinterstitialForm.Control.Site與AdinterstitialForm.Control.Zone帶入我們申請的SiteID與ZoneID。簡單的程式範例如下：

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
...

	若有意進一步了解的，這邊強烈建議參閱SDK附的說明文件，位置在"C:\Program Files\mOcean\mOcean Intel CS SDK\mOcean_Intel_CS_SDK_Documentation.pdf"，該說明文件對於控制項的屬性、方法，與廣告視窗都較為詳細的介紹。