---
title: "[Software]使用GooCalSync同步Google與Notes日曆"
date: "2010-08-09 12:25:24"
description: "[Software]使用GooCalSync同步Google與Notes日曆"
tags: [Software]
---

最近剛換了個Android作業系統的新手機，剛好自己又是Google重度使用者，就想說把公司內部用的Notes日曆與Google的日曆同步，如此在手機上就能隨時掌握已排定的工作，也能利用手機本身的通知功能來提醒自己。上網找到GooCalSync這套Java開發的軟體能達到需求，只是要手動結合Notes，設定就變得有點複雜難懂，這邊簡單的記錄一下。

  首先需先確定Java Run Time為1.5以後的版本，若太舊的可至Sun網站下載更新。Java Run Time確認完後，到GooCalSync網站下載GooCalSync軟體。解壓縮後打開GooCalSync.bat，將其用到的路徑位置改為您電腦中正確的對應位置(像是JDK/JRE、 Lotus Notes 、GooCalSync等路徑位置)，改完後存檔關閉。  

接著我們必須手動設定以結合Notes。首先把剛下載的壓縮檔中的GooCalSync.ntf複製到Notes設定的資料庫資料夾。該位置可透過點選[檔案]→[細項設定]→[使用者細項設定]開啟使用者細項設定對話框，查閱基本頁籤中的本區資料庫資料夾設定。

接著透過Ctrl+N快速鍵，或是透過點選[檔案]→[資料庫]→[新增]開啟新資料庫對話框，設定標題與檔案位置後按下確定。

完成後工作區中應該會看到GoogleCalSync的圖示。

點選開啟設定細部設定，主要要設定的有GOOGLE帳密、Notes Domino Server、Mail DB檔案、同步的類型、Proxy...等。

這邊比較有問題的設定應該是Notes Domino Server與Mail DB檔案，可在Notes郵件圖示上方按下滑鼠右鍵，在彈出的快顯選單中點選[資料庫]→[屬性]，查看資料庫屬性對話框中的伺服器與檔名設定。

到此，同步Google與Notes日曆的設定已經完成，可直接用滑鼠點擊開啟剛下載的壓縮檔中的GooCalSync.bat檔，就可以進行同步的動作。

除此之外，您也可以在Notes的工具列上建立一個自訂按鈕方便來做同步的動作，只要在Notes工具列上按下滑鼠右鍵，在彈出的快顯選單中點選[工具列細項設定...]。

在工具列細項設定對話框中的工具列頁籤，選取自訂按鈕要襬放的工具列。

接著切到自訂頁籤，按下[新增]→[按鈕]。

再填入自訂按鈕的內文、說明文字、與要運行的公式即可。公式請依下面格式輸入：
  
@Command([Execute];"[GooCalSync.bat完整路徑]")

完成後在工具列上就可看到自己加入的同步按鈕。

## Link
     GooCalSync    與谷歌同步吧-谷歌日曆同步程式(Google Calendar Sync)