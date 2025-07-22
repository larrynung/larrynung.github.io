---
title: "Google Plus One API"
date: "2013-11-06 12:00:00"
description: "Google Plus One API"
tags: [
  {lang: 'zh-TW', parsetags: 'explicit'}]
---Google近期推出了Plus One功能，類似於Facebook上的讚，你可以透過Plus One功能對你覺得喜歡的內容做個標記。詳細介紹可參閱Google的介紹影片：

若將這樣的功能加入到自己的網站，可透過Google Plus One API來完成。只要簡簡單單的在網站上加入JavaScript標記。

再加入Plus One標記就可以了。

所以最簡單的方法就是在網頁上加入以下的程式碼片段， 就能為網站加入Plus One的功能。

若基本的功能不足以符合網站的需求，我們就必須要為其做些細部的調整，像是在JavaScript那邊的設定可透過lang參數去指定顯示的語系，這邊設定的語系主要會影響點選Plus One按鈕後彈出的對話框語系。而parsetags屬性則是設定Plus One按鈕是要在載入網頁時載入，還是要明確的用JavaScript去控制載入的動作。

像是下面這樣：

{lang: 'zh-TW', parsetags: 'explicit'}

而在Plus One按鈕那邊也有些參數可供細部設定，像是是否要顯示Plus One被按下的總數、所要Plus One的網址、與Plus One按鈕的大小等。

像是：

若不熟悉這邊的參數設定，Google也有提供輔助用的設定器，只要做些選項設定就可以產生對應的程式碼片段，開發人員只要將這些程式碼片段依指示放置在該放置的位置即可。

這邊實際來為網站加入個Google Plus One功能，以點部落為例，進入設定頁面，切換至選項頁面，在簽名檔中加入Plus One的功能程式碼。

加完後存檔，隨便開啟個文章就會看到Plus One的按鈕。

點選後會彈出個視窗要求建立Plus One時所會顯示的個人資料，視窗的語系由JavaScript設定的lang參數所決定，該視窗會帶入預設的顯示名稱，若要自行設定可點選後方的自訂個人資料進行進一步的設定。

## Link

+1 button API

在網頁上加入 + 1 按鈕，讓您的網站脫穎而出