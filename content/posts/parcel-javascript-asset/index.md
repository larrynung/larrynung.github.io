---
title: "Parcel - JavaScript asset"
date: "2018-01-09 00:27:17"
description: "要使用 Parcel 在 JavaScript 中載入 JavaScript 模塊可用 CommonJS 的寫法。 const module = require(modulePath); 或是 ES6 的寫法。"
tags: [Parcel]
---

要使用 Parcel 在 JavaScript 中載入 JavaScript 模塊可用 CommonJS 的寫法。

const module = require(modulePath);

或是 ES6 的寫法。

import module from modulePath;

除了 JavaScript 的模塊外，也能引用 CSS 文件。

import cssPath;

以及引用圖片。

import imageUrl from imagePath;

像是下面這邊筆者創建了個簡單的範例，建立了個 index.html，裡面引用了 index.js。
```html
<html>
    <body>
      <script src="./scripts/index.js"></script>
    </body>
</html>
```
![1.png](1.png)

index.js 內引用了不同類型的檔案。
```js
//const hello = require('./hello');
import hello from './hello';
import '../style/index.css';
import profileImageUrl from '../images/profile.jpg';
console.log(profileImageUrl);
```
![2.png](2.png)

像是 js 檔(hello.js)。
```js
console.log("hello world");
```
![3.png](3.png)

CSS 檔(index.css)。
```css
body {background-color: coral;}
```
![4.png](4.png)

以及圖檔。

範例準備好後調用 Parcel 命令建置並啟用服務。

![5.png](5.png)

Parcel 解析網站後會將需要的檔案處理後移至輸出目錄。

![6.png](6.png)

連至啟動的服務網址，可看到網站正確的被運行。

![7.png](7.png)

Link
----
* [📦 资源(Assets)](https://parceljs.org/assets.html)