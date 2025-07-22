---
title: "Parcel - HTML asset"
date: "2018-01-11 06:26:20"
tags: [Parcel]
---

除了 JavaScript 文件外，Parcel 也支援 HTML 文件的處理。

像是下面這邊筆者創建了個簡單的範例，建立了個 index.html，裡面載入了 profile.jpg 且連結了 hello.html 頁面。
```html

![](./images/profile.jpg)
[Say Hello](./hello.html)
```
![1.png](1.png)

profile.jpg 是很單純的大頭照。

![2.png](2.png)

hello.html 內引用了 hello.js 並輸出 Hello World 字樣。
```html

Hello World
```
![3.png](3.png)

hello.js 內則是很簡單的利用 Console 輸出 hello world 字樣。
```js
console.log("hello world");
```
![4.png](4.png)

調用 Parcel 命令建置並啟用服務。

![5.png](5.png)

Parcel 解析網站後會將需要的檔案處理後移至輸出目錄。

![6.png](6.png)

連至啟動的服務網址，可看到網站正確的被運行。

![7.png](7.png)

![8.png](8.png)

Link
----
* [📦 資源(Assets)](https://parceljs.org/assets.html)