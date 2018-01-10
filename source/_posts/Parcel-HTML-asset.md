---
title: Parcel - HTML asset
date: 2018-01-11 06:26:20
tags: [Parcel]
---

除了 JavaScript 文件外，Parcel 也支援 HTML 文件的處理。  

<!-- More -->

<br/>


像是下面這邊筆者創建了個簡單的範例，建立了個 index.html，裡面載入了 profile.jpg 且連結了 hello.html 頁面。  

```html
<html>
    <body>
      <img src="./images/profile.jpg">
      <a href="./hello.html">Say Hello</a>
    </body>
</html>
```

{% asset_img 1.png %}
 
<br/>


profile.jpg 是很單純的大頭照。  

{% asset_img 2.png %}
 
<br/>


hello.html 內引用了 hello.js 並輸出 Hello World 字樣。  

```html
<html>
    <body>
      <script src="./scripts/hello.js"></script>
      Hello World
    </body>
</html>
```

{% asset_img 3.png %}
 
<br/>


hello.js 內則是很簡單的利用 Console 輸出 hello world 字樣。  

```js
console.log("hello world");
```

{% asset_img 4.png %}
 
<br/>


調用 Parcel 命令建置並啟用服務。  

{% asset_img 5.png %}
 
<br/>


Parcel 解析網站後會將需要的檔案處理後移至輸出目錄。  

{% asset_img 6.png %}
 
<br/>


連至啟動的服務網址，可看到網站正確的被運行。

{% asset_img 7.png %}
 
<br/>


{% asset_img 8.png %}
 
<br/>


Link
----
* [📦 資源(Assets)](https://parceljs.org/assets.html)
