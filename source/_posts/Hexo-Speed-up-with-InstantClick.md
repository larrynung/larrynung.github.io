---
title: Hexo - Speed up with InstantClick
date: 2017-08-03 13:07:08
tags: [InstantClick, Hexo]
---

要用 InstantClick 加速 Hexo 部落格，可先下載 InstantClick 放至 source\js 下。  

<!-- More -->

{% asset_img 1.png %}

<br/>


然後開啟 _config.yml 設定檔，加入 skip_render 設定，將 js 檔排除 render。  

{% asset_img 2.png %}

<br/>


接著修改 Hexo 的 theme 讓 InstantClick 得以啟動。以 next theme 為例，可開啟 next theme 的 layout\_layout.swig，將 InstantClick 啟動的程式插入即可。  

```js
<script type="text/javascript" src= "js/instantclick.js" data-no-instant></script>
<script data-no-instant>InstantClick.init();</script>
```

{% asset_img 3.png %}

<br/>


設定完可開啟部落格網站，打開開發人員工具，切換到 Network 頁籤，然後將滑鼠移至連結，就可以看到當滑鼠移至連結時就已經在進行預載的動作了。  

{% asset_img 4.png %}

<br/>


最後提醒一下，InstantClick 的預載行為可能會造成其它套件的異常，可能要自行視情況修正將問題排除。  

<br/>


Link
----
* [InstantClick — JS library to make your website instant](http://instantclick.io/)