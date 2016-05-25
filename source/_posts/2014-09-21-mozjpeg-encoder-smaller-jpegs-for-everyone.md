---
layout: post
title: "mozjpeg encoder - smaller jpegs for everyone"
date: 2014-09-21 16:23:00
comments: true
categories: 
keywords: "Mozjpeg, Jpeg, Encoder, Online"
description: "mozjpeg encoder - smaller jpegs for everyone"
---

筆者在 [Mozjpeg - Improved JPEG encoder - Level Up](http://larrynung.github.io/2014/09/20/mozjpeg-improved-jpeg-encoder/) 這篇稍稍的介紹了一下 Mozilla 的 Mozjpeg 專案及其用法。但需要進行檔案的編譯或是下載，取得檔案後要再下命令才能轉換。對於只是想要做個體驗，或是臨時要做處理的，我們應該不會想這麼做。  

<!-- More -->

<br/>

因此這篇要稍稍的介紹一下 [mozjpeg encoder](http://mozjpeg.codelove.de/) 這個線上服務。它能讓我們直接將圖片上傳，上傳後該服務會用 Mozjpeg 進行壓縮後讓我們下載回來。  

<br/>

使用上只要先設定所要使用的圖片品質，或是選取無失真的處理方式...  

{% img /images/posts/MozjpegEncoder/1.png %}

<br/>

然後將要處理的檔案用拖曳的方式放至網站上...  

{% img /images/posts/MozjpegEncoder/2.png %}

<br/>

拖曳完成，圖片會進行上傳的動作，並做壓縮的處理。處理完後網站會有處理前後的比對，可以清楚知道圖片壓縮為我們省下了多少。若要將壓縮後的圖檔下載下來使用，這邊也可直接點擊 `download image` 按鈕進行下載...  

{% img /images/posts/MozjpegEncoder/3.png %}

<br/>

最後一提，該網站上方的 binaries 頁面有提供 Mozjpeg 的 Binary 檔，有需要的可直接從該頁面下載使用，就不需要自行將 Mozjpeg 編譯。  

Link
----
* [mozjpeg encoder](http://mozjpeg.codelove.de/)
