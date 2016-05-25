---
layout: post
title: "Mozjpeg - Improved JPEG encoder"
date: 2014-09-20 16:21:00
comments: true
categories: 
keywords: "Mozjpeg"
description: "Mozjpeg - Improved JPEG encoder"
---

Mozjpeg 是 Mozilla 在維持相容性的前提下，為了改善 JPEG 壓縮能力，以減少檔案大小並加速網頁傳輸所開的專案。  

<!-- More -->

<br/>

目前現階段已發行到了 2.1 版，以數據來說平均約可減少 5% 的檔案大小。  

<br/>

有興趣的可至 [mozilla/mozjpeg · GitHub](https://github.com/mozilla/mozjpeg) 這邊下載編譯來使用，編譯方式可參閱 [BUILDING.txt](https://github.com/mozilla/mozjpeg/blob/master/BUILDING.txt) 文件。  

<br/>

如果不會編譯的也沒關係，可到 [mozjpeg | binaries](http://mozjpeg.codelove.de/binaries.html) 這邊直接下載別人編譯好的檔案來用。  

{% img /images/posts/Mozjpeg/1.png %}

<br/>

檔案取得後，我們會看到裡面有四個執行檔，一個Dll。四個執行檔各自有不同的功用，像是壓縮、解壓縮、轉換...之類的，使用上可參閱 [usage.txt](https://github.com/mozilla/mozjpeg/blob/master/usage.txt)。  

<br/>

不過基本上我們多半只會需要做些圖檔壓縮或無失真的減肥處理動作，因此我們通常只需要熟悉 cjpeg 以及 jpegtran 的使用。  

<br/>

使用方式我們可直接呼叫 cjpeg 命令，並帶入參數 -? 查詢。  

    cjpeg -?

{% img /images/posts/Mozjpeg/2.png %}

<br/>

使用上大概是遵循下面這樣的方式去叫用：
    cjpeg [switches] -outfile jpegfile  imagefile	' Support all systems
    cjpeg [switches] [imagefile] >jpegfile		' Support Unix-like systems
    cjpeg [switches] imagefile jpegfile		' Support non-Unix systems

<br/>

指令參數部分很多都是一般我們不會需要用到的，若有需要到時再回過來查也就好了。基本使用我們只要知道 -quality 與 -baseline 這兩個參數應該就可以了。

<br/>

-quality 參數是用來指定壓縮圖檔的品質的，一般是建議將其值設在 60 - 90 之間，若不設定預設是用 75。

    cjpeg -quality 80 -outfile Desert_Compressed.jpg Desert.jpg


-baseline 參數是用來指定產生 Baseline 的圖檔，預設產生的是 Progressive 的圖檔，若有需要變更就要特別指定。  

    cjpeg -baseline -quality 80 -outfile Desert_Compressed.jpg Desert.jpg


cjpegtran 的使用上，我們主要是拿來做無失真的減肥處理，只要像下面這樣帶入 -copy none 參數即可。  

    jpegtran -copy none -outfile Desert_Compressed.jpg Desert.jpg


Link
----
* [mozilla/mozjpeg · GitHub](https://github.com/mozilla/mozjpeg)
* [mozjpeg/BUILDING.txt at master · mozilla/mozjpeg · GitHub](https://github.com/mozilla/mozjpeg/blob/master/BUILDING.txt)
* [mozjpeg/usage.txt at master · mozilla/mozjpeg · GitHub](https://github.com/mozilla/mozjpeg/blob/master/usage.txt)
* [mozjpeg | binaries](http://mozjpeg.codelove.de/binaries.html)
* [Mozilla釋出檔案更小的Mozjpeg 2.0圖檔，FB採用並贊助發展下一代 | iThome](http://www.ithome.com.tw/news/89459)
* [用 mozjpeg 產生高效率的 JPEG | 部落格 | Mozilla Taiwan](http://blog.mozilla.com.tw/posts/6084/using-mozjpeg-to-create-efficient-jpegs)
* [mozjpeg：JPEG图片压缩5%，获Facebook支持 - 开源中国社区](http://www.oschina.net/news/54087/mozjpeg-2-0-released)
