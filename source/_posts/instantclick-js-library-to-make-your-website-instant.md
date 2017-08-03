---
title: "InstantClick - JS library to make your website instant"
date: 2017-08-02 13:29:44
tags: [InstantClick]
---

InstantClick 是一 JS 套件，能讓在 MouseHover 時就預先進行站台的載入，這樣在 MouseDown 後切換頁面就會只需要較少的載入時間，加速網站的載入速度。  

<!-- More -->

<br/>


InstantClick 這邊也提供了個簡易的[測試站台](http://instantclick.io/click-test)，可用來測試 MouseHover 與 MouseDown 之間的時間間隔，也就是 InstantClick 會拿來預載網頁的時間間隔。

{% asset_img 1.png %}

<br/>


測試上只要先把滑鼠從連結上移開，然後將滑鼠移上連結，按下滑鼠按鈕即可。通常測試下來大概可以看到可用來預載的時間間隔約為 200 ~ 300 ms。    

{% asset_img 2.png %}

<br/>


想要看一下 InstantClick 的運作的話，可以在 InstantClick 網站開啟開發人員工具，切換到 Network 頁籤，然後將滑鼠移至連結，就可以看到當滑鼠移至連結時就已經在進行預載的動作了。  

{% asset_img 3.png %}

<br/>


InstantClick 支援的瀏覽器版本如下：  

{% asset_img 4.png %}

<br/>


若是要使用可在下載頁面將要使用的 js 檔下載。  

{% asset_img 5.png %}

<br/>


或是透過 bower 之類的套件管理工具下載。  

    bower install instantclick

<br/>


下載下來後放置專案中像下面這樣調用即可。  	
	
```js
<script type="text/javascript" src= "js/instantclick.js" data-no-instant></script>
<script data-no-instant>InstantClick.init();</script>
```

<br/>


最後提醒一下，InstantClick 的預載行為可能會造成其它套件的異常，可能要自行視情況修正將問題排除。  

<br/>


Link
----
* [InstantClick — JS library to make your website instant](http://instantclick.io/)