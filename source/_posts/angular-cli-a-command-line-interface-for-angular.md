---
title: "Angular CLI - A command line interface for Angular"
date: 2017-04-23 18:25:08
tags: [Angular]
---

使用 Angular CLI 前，需先確認 Node.js 版本有到 6.9.0 以上，npm 有到 3 以上。  

<!-- More -->

<br/>


安裝用 npm 將 Angular CLI 安裝到全域。  

    npm install -g @angular/cli

{% asset_img 1.png %}

<br/>


安裝完可調用 ng 並帶入參數 -v 去查驗版本。  

    ng -v

{% asset_img 2.png %}

<br/>


用 help 命令去查閱使用語法。  

    ng help

{% asset_img 3.png %}

<br/>


用 new 命令帶入專案名稱去建立指定名稱的 Angular 專案。  

    ng new <ProjectName>

{% asset_img 4.png %}

<br/>


專案建立後會幫我們準備好基本的程式。  

{% asset_img 5.png %}

<br/>


進入專案目錄，用 serve 命令啟動服務器。  

{% asset_img 6.png %}

<br/>


開啟瀏覽器輸入服務器網址即可看到專案運行起來的樣子。  

{% asset_img 7.png %}

<br/>


Link
----
* [CLI tool for Angular](https://cli.angular.io/)
