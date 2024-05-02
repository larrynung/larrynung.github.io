---
title: "Parcel - Getting started"
date: "2017-12-23 07:15:47"
tags: [Parcel]
---


Parcel 使用前需先安裝套件。  

<!-- More -->

<br/>


可以透過 yarn。   

    yarn global add parcel-bundler

<br/>


或是透過 npm 安裝。  

    npm install -g parcel-bundler
    
<br/>


 ![1.png](1.png)
 
 <br/>


安裝完準備要進行打包的程式。  

 ![2.png](2.png)
 
 <br/>


Index.html 檔案內容為：  

```html
<html>
<body>
  <script src="./index.js"></script>
</body>
</html>
```

<br/>


Index.js 檔案內容為：  

```js
console.log("hello world");
```

<br/>


調用 Parcel 命令進行編譯並運行網站服務。  

    parcel [WebFile]

 ![3.png](3.png)
 
 <br/>


編譯後的檔案會產生在 dist 目錄下。  

 ![4.png](4.png)
 
 <br/>


連至網站可看到打包後運行起來的樣子。  

 ![5.png](5.png)
 
 <br/>


要退出網站服務的話，按下熱鍵 Ctrl + C，鍵入 Y 後 Enter 即可。  

 ![6.png](6.png)
 
 <br/>
