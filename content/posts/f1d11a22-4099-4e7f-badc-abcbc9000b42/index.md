---
title: "如何上傳Visual Studio Extension至Visual Studio Gallery"
date: "2013-11-06 12:00:00"
tags: [Visual Studio]
description: "有在用Visual Studio開發的都知道在Visual Studio中有好用的Extension Manager，可供開發人員直接在上面搜尋、下載、及安裝想要的擴充套件，而他搜尋的來源主要是來至於Visual Studio Gallery，所以當我們開發了一個擴充套件想要分享出去時，"
---

有在用Visual Studio開發的都知道在Visual Studio中有好用的Extension Manager，可供開發人員直接在上面搜尋、下載、及安裝想要的擴充套件，而他搜尋的來源主要是來至於Visual Studio Gallery，所以當我們開發了一個擴充套件想要分享出去時，我們也可以很直接的將它上到[Visual Studio Gallery，就可以很容易地將擴充套件散播出去。](http://visualstudiogallery.msdn.microsoft.com/)

那要如何才能將開發的擴充套件上傳至Visual Studio Gallery呢？首先我們必須連到Visual Studio Gallery這個網站，並登入自己的Live ID，然後像下圖這樣點選Upload的圖示。

![image_thumb.png](/images/posts/f1d11a22-4099-4e7f-badc-abcbc9000b42/image_thumb.png)

按下後會進到上傳擴充套件的處理流程，首先第一步我們要決定上船的擴充套件是屬於哪種型態的套件。以筆者的擴充套件來說是一個輔助性的工具，因此這邊筆者選取的是Tool這個類型。

![image_thumb_1.png](/images/posts/f1d11a22-4099-4e7f-badc-abcbc9000b42/image_thumb_1.png)

選取完類型後按下Next，會進到第二步，這步驟主要是要上傳擴充套件的檔案，選取編譯出來的vsix檔案將它上傳上去即可。

![image_thumb_2.png](/images/posts/f1d11a22-4099-4e7f-badc-abcbc9000b42/image_thumb_2.png)

第三步則是設定擴充套件的一些基本資訊，Visual Studio Gallery預設會從上傳的vsix中的manifest抽出一些資訊並將之帶出。

![image_thumb_4.png](/images/posts/f1d11a22-4099-4e7f-badc-abcbc9000b42/image_thumb_4.png)

若是manifest有設定好的話，這邊其實我們只需要將Category、Cost Category、以及Description這幾個部分的資料補齊就好。

![image_thumb_5.png](/images/posts/f1d11a22-4099-4e7f-badc-abcbc9000b42/image_thumb_5.png)

Description這邊的資料比較麻煩些，因為它有限制字數必須要多於180個字元。(若是不太會排版的可以善用右側所提供的樣板，將樣板套用上去後再下去修改會方便許多。)

![image_thumb_6.png](/images/posts/f1d11a22-4099-4e7f-badc-abcbc9000b42/image_thumb_6.png)

資料都補齊後，最後就是授權的部分，若是對條款沒什麼意見，勾選後按下[Create Contribution]就可以了。

![image_thumb_7.png](/images/posts/f1d11a22-4099-4e7f-badc-abcbc9000b42/image_thumb_7.png)

[Create Contribution]按下後，該擴充套件的頁面就會被建立，會出現類似下面這樣的頁面。需特別注意到此時你的擴充套件還沒有對外發佈，你可以在這頁面中確認擴充套件相對應的資料是否都正確，若是有誤可按下Edit再次進行編修，若是正確無誤可以按下Publish對外發佈，發佈後你的擴充套件就可以透過Extension Manager搜尋到了。

![image_thumb_8.png](/images/posts/f1d11a22-4099-4e7f-badc-abcbc9000b42/image_thumb_8.png)

## Link

* Visual Studio 元件庫
