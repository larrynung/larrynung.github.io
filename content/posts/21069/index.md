---
title: "[Software]CodeFusion Wizard"
date: "2011-01-27 12:01:54"
description: "最近看到補丁工具codefusion wizard v3.0這篇，名稱跟界面看起來滿炫的，所以稍微抓下來玩了一下，還算是滿方便的一個工具，可很輕鬆的製作出補丁程式，將自己要更新的檔案透過該程式包裝起來，許多網路流傳的破解或補丁都是用這個軟體製作，這邊隨手記錄一下使用方式。"
tags: [Software]
---

最近看到補丁工具codefusion wizard v3.0這篇，名稱跟界面看起來滿炫的，所以稍微抓下來玩了一下，還算是滿方便的一個工具，可很輕鬆的製作出補丁程式，將自己要更新的檔案透過該程式包裝起來，許多網路流傳的破解或補丁都是用這個軟體製作，這邊隨手記錄一下使用方式。

程式開啟後會看到如下畫面，可設定一些基本的資訊，右邊太極符號那邊可以設定產生出來的補丁程式的ICON，中間為設定補丁的視窗標題、標題或程式名稱、與附加的資訊。

![image_thumb.png](/images/posts/21069/image_thumb.png)

上方兩個鉛筆的按鈕，一個是清除輸入的內容，一個是帶入預設的文字，而下方前兩個按鈕，前面第一個是用來將當前的設定設為預設的輸入，第二個是還原為本來系統內建的預設輸入。

![image_thumb_24.png](/images/posts/21069/image_thumb_24.png)

最後一個按鈕是用來設定關於對話框的資訊。

![image_thumb_3.png](/images/posts/21069/image_thumb_3.png)

設定完後可透過上方的眼睛工具按鈕檢視設定後的畫面。

![image_thumb_23.png](/images/posts/21069/image_thumb_23.png)

基本資訊設定完後，按下[Next >]按鈕設定要更新的內容，更新的內容分為兩大塊，上半部為要更新的檔案，下半部為要更新的動作。首先我們按下上半部的加號設定要更新的檔案。

![image_thumb_4.png](/images/posts/21069/image_thumb_4.png)

系統會彈出[Add File to Project]設定對話框。

![image_thumb_5.png](/images/posts/21069/image_thumb_5.png)

透過File to patch後方的按鈕選取要更新的檔案。

![image_thumb_7.png](/images/posts/21069/image_thumb_7.png)

檔案資訊會被載入到 [Add File to Project]設定對話框，按下[OK]按鈕確定設定。

![image_thumb_8.png](/images/posts/21069/image_thumb_8.png)

會在更新內容頁面的上半部看到剛加入的檔案。

![image_thumb_9.png](/images/posts/21069/image_thumb_9.png)

接著按下下半部的加號按鈕，會看到CodeFusion提供的四種設定方式。

![image_thumb_10.png](/images/posts/21069/image_thumb_10.png)

Byte-Patch Offset可以設定檔案某一偏移位置開始要寫入的資料內容。

![image_thumb_15.png](/images/posts/21069/image_thumb_15.png)

Find & Replace可設定從某一偏移位置開始所要找尋的資料，與找到後所要變更的資料內容。

![image_thumb_16.png](/images/posts/21069/image_thumb_16.png)

Truncate Offset可以將檔案截短，指定的偏移位置即為檔案的結尾。

![image_thumb_17.png](/images/posts/21069/image_thumb_17.png)

File Compare是用來比對檔案內容的，也是我們最常使用的選項，他會依照指定的兩個檔案去比對其差異，進而找出對應的變更動作。

![image_thumb_11.png](/images/posts/21069/image_thumb_11.png)

使用上需將Original File與Patched File設定，接著按下左下方的[Compare]按鈕。

![image_thumb_12.png](/images/posts/21069/image_thumb_12.png)

兩個檔案間的差異就找出來了，按下[OK]按鈕確定。

![image_thumb_13.png](/images/posts/21069/image_thumb_13.png)

Code Fusion會自動將兩個檔案的差異與所需要做的變更給加入到下半部表格。都設定完後，按下[Next >]按鈕繼續。

![image_thumb_14.png](/images/posts/21069/image_thumb_14.png)

再按下中間的[Make Win32 Executable!]按鈕，指定要產生補丁執行檔的位置後，會自動產生出對應的補丁執行檔。

![image_thumb_18.png](/images/posts/21069/image_thumb_18.png)

![image_thumb_19.png](/images/posts/21069/image_thumb_19.png)

此時可以直接按下Win32 Executable Output File後面的運行按鈕，產生的補丁執行檔就會被運行。

![image_thumb_20.png](/images/posts/21069/image_thumb_20.png)

運行後我們可以看到如下的補丁介面。

![image_thumb_21.png](/images/posts/21069/image_thumb_21.png)

依這邊的範例，補丁運行後會將本來熊的圖片替換為氣球的圖片。

![image_thumb_22.png](/images/posts/21069/image_thumb_22.png)

## Link

* [CodeFusion 3.0: Free Download](http://www.softpedia.com/progDownload/CodeFusion-Download-1433.html)
* [補丁工具codefusion wizard v3.0](http://www.dotblogs.com.tw/hung-chin/archive/2011/01/24/20974.aspx)
