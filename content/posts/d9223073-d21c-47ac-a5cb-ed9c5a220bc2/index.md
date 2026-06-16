---
title: "[Web]使用BrowserStack測試網頁的相容性"
date: "2013-11-06 12:00:00"
tags: [Web]
description: "筆者前幾天看到Cross Browser Debugging integrated into Visual Studio with BrowserStack這篇文章，因為覺得有趣就試玩了一下。"
---

筆者前幾天看到Cross Browser Debugging integrated into Visual Studio with BrowserStack這篇文章，因為覺得有趣就試玩了一下。

可以直接連到BrowserStack的[Dashboard](http://www.browserstack.com/start)，由使用界面我們可以看到BrowserStack可以讓我們在不同的OS、瀏覽器、與解析度之下測試自己的網頁。

![image_thumb_6.png](/images/posts/d9223073-d21c-47ac-a5cb-ed9c5a220bc2/image_thumb_6.png)

在做測試時BrowserStack會需要一小段時間去做初始化的動作。

![image_thumb_7.png](/images/posts/d9223073-d21c-47ac-a5cb-ed9c5a220bc2/image_thumb_7.png)

初始化完成就會看到像下面這樣的畫面，開發人員可以直接在右測看到跑起來的效果。若有需要隨時可以透過左邊的Bar下去調整OS與瀏覽器之類的設定。

![image_thumb_8.png](/images/posts/d9223073-d21c-47ac-a5cb-ed9c5a220bc2/image_thumb_8.png)

若是比較常需要測試IE的相容性，[modern.IE](http://www.modern.ie/)也提供了Chrome與FireFox的Add-in，可讓測試上更為便利。使用時只需要導到要測試的網頁，然後按下Add-In，指定需要運行的IE版本就可以了。

![image_thumb_1.png](/images/posts/d9223073-d21c-47ac-a5cb-ed9c5a220bc2/image_thumb_1.png)

它一樣會幫我們導到BrowserStack進行測試。

![image_thumb_3.png](/images/posts/d9223073-d21c-47ac-a5cb-ed9c5a220bc2/image_thumb_3.png)

順帶一提，BrowserStack也已開始針對Visual Studio進行整合，正確安裝後瀏覽器設定那邊會多個瀏覽器選項可供測試，但目前看來能支援的只有Visual Studio 2012 Express，雖然Visual Studio 2012其它版本也是可以安裝，但不會有任何的效果。

![image_thumb_5.png](/images/posts/d9223073-d21c-47ac-a5cb-ed9c5a220bc2/image_thumb_5.png)

## Link

* [modern.IE](http://www.modern.ie/)
* [Cross Browser Debugging integrated into Visual Studio with BrowserStack](http://www.hanselman.com/blog/CrossBrowserDebuggingIntegratedIntoVisualStudioWithBrowserStack.aspx)
* [BrowserStack](http://visualstudiogallery.msdn.microsoft.com/2dfa32b1-3c47-439d-b1c5-9e28be18b81c)
* [How do I use the BrowserStack Visual Studio extension?](http://www.browserstack.com/question/537)
