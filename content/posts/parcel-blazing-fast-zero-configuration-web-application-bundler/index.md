---
title: "Parcel - Blazing fast, zero configuration web application bundler"
date: "2017-12-22 06:46:39"
tags: [Parcel]
---


Parcel 是一極速零配置的 Web 應用打包工具，不需額外的配置設定就能快速的將 Web 應用程式進行打包。  

<!-- More -->

<br/>


![1.png](1.png)

<br/>


該工具具有以下幾個特點：  

- Blazing fast bundle times
- Bundle all your assets
- Automatic transforms
- Zero config code splitting
- Hot module replacement
- Friendly error logging

<br/>


也就是說 Parcel 的打包速度極快、支援 JS/CSS/HTML 文件、可以自動轉換程式、不用額外的配置、可以動態更新、錯誤訊息比較好看。  

<br/>


其中速度極快是因為 Parcel 使用多核進行編譯，且會將編譯過的文件進行快取，所以編譯速度極快。

<br/>


Parcel 的作者有在 4 CPU 的 2016 MacBook Pro 上將 1726 的模塊，6.5 M 大小的 Web 應用程式進行壓縮，可以看到 Parcel 在打包上的確花了較少的時間。    

| Tool | Time | 
|:-------------:|:-------------:|
| browserify | 22.98s |
| webpack | 20.71s |
| parcel | 9.98s |
| parcel - with cache | 2.64s | 

<br/>


Link
-----
* [📦 Parcel](https://en.parceljs.org/)
