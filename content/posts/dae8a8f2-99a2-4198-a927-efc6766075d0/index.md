---
title: "[CoffeeScript]Setting Up a CoffeeScript Development Environment on Windows"
slug: "coffeescript-setting-up-a-coffeescript-development-environment-on-windows"
aliases: ["/posts/dae8a8f2-99a2-4198-a927-efc6766075d0/"]
date: "2013-11-06 12:00:00"
tags: [CoffeeScript]
description: "要在Windows上建立CoffeeScript的開發環境，首先須要安裝可在Windows上運行的node.js，可至node.js首頁下載安裝。 安裝後會程式集內會多兩個Icon，這邊直接點擊Node.js command prompt，開啟命令提示字元。"
---

要在Windows上建立CoffeeScript的開發環境，首先須要安裝可在Windows上運行的node.js，可至[node.js首頁下載安裝。](http://nodejs.org/)

![image_thumb_7.png](/images/posts/dae8a8f2-99a2-4198-a927-efc6766075d0/image_thumb_7.png)

安裝後會程式集內會多兩個Icon，這邊直接點擊Node.js command prompt，開啟命令提示字元。

![image_thumb_1.png](/images/posts/dae8a8f2-99a2-4198-a927-efc6766075d0/image_thumb_1.png)

在命令提示字元中鍵入"npm install -g coffee-script"進行CoffeeScript的安裝。

![image_thumb_2.png](/images/posts/dae8a8f2-99a2-4198-a927-efc6766075d0/image_thumb_2.png)

安裝好後我們可用"coffee -v"查驗CoffeeScript的版本，或是用"coffee -h"查看CoffeeScript的命令列參數，以確定CoffeeScript有正確的安裝進去。CoffeeScript的命令列參數大概如下圖所示，比較重要的大概就是-c、-i、-w這幾個命令列參數，有興趣的可從這幾個命令列參數下手了解起。

![image_thumb_5.png](/images/posts/dae8a8f2-99a2-4198-a927-efc6766075d0/image_thumb_5.png)

若是直接呼叫CoffeeScript不帶入命令列參數，視同於帶入-i這個命令列參數。會切換到互動模式，可直接在裡面測試CoffeeScript的語法。![image_thumb_6.png](/images/posts/dae8a8f2-99a2-4198-a927-efc6766075d0/image_thumb_6.png)

除了互動模式外，我們也可以先撰寫好CoffeeScript再將之進行編譯轉成JavaScript，這也是一般比較常見的使用方式。像是筆者這邊就建立了一個helloword.coffee的CoffeeScript程式，裡面有一個很簡單的方法，預設執行會秀出"hello!!"，如果有帶入指定的字串則改秀帶入的字串。

![image_thumb_3.png](/images/posts/dae8a8f2-99a2-4198-a927-efc6766075d0/image_thumb_3.png)

CoffeeScript的程式碼編寫好後帶入命令列參數-c以及程式檔，CoffeeScript會進行編譯並產生對應的js檔。像是上面筆者編寫的CoffeeScript程式透過編譯就會產生像下圖這樣的js檔。

![image_thumb_4.png](/images/posts/dae8a8f2-99a2-4198-a927-efc6766075d0/image_thumb_4.png)

## Link

* node.js
