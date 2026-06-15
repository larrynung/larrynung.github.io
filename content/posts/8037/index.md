---
title: "[WLW]插入精靈開發隨筆"
date: "2009-04-17 08:29:20"
description: "[WLW]插入精靈開發隨筆"
tags: [WLW]
---

## Introduction

看了水瓶大的WLW (Windows Live Writer)外掛教學後，如獲一甲子功力，雖功力還不夠使用天外飛仙，但也已足夠撰寫WLW Simple類型外掛。不過想了半天，卻想不到我要寫啥外掛。既然想不到要寫啥外掛，索性乾脆寫個更彈性、功能可隨意調整、可很快編寫的外掛。

## 概觀

外掛目前暫命名為插入精靈，介面目前暫定如下：

**主介面-顯示所有可用的插入項目，在項目上連點兩下即可插入內容**

![image_thumb_2.png](/images/posts/8037/image_thumb_2.png)

**編輯畫面-可供編輯插入項目，編完存檔後的插入項目會顯示在主畫面，供使用者插入使用**

![image_thumb_3.png](/images/posts/8037/image_thumb_3.png)

## Hello World範例

欲使用該外掛編寫Hello World可直接切到Result頁面，並設定Result變數。

![image_thumb_4.png](/images/posts/8037/image_thumb_4.png)

接著把該檔存起來

![image_thumb_5.png](/images/posts/8037/image_thumb_5.png)

存完檔後會在插入項目列表區看到剛存的檔案

![image_thumb_6.png](/images/posts/8037/image_thumb_6.png)

點選兩下即會插入所編寫的內容

![image_thumb_8.png](/images/posts/8037/image_thumb_8.png)

從上面可以知道，目前設定最後插入到WLW的HTML，其實就是上面所設的Result變數值。換句話說，假設要編寫的是像水瓶大外掛一樣的可愛圖片，也只要在把HTML設到Result變數並存檔就完成了。

## Hello World進階範例

接著看一下如何運用Command來編寫。這邊我要把本來不會動的Hello World，利用Command去把它變為動態的Hello World。

**Step1.編寫變數值**

這邊設定了靜態與動態Hello World的HTML

![image_thumb_9.png](/images/posts/8037/image_thumb_9.png)

**Step2.插入命令**

在左側命令列表區點選兩下，加入要使用的命令。

![image_thumb_14.png](/images/posts/8037/image_thumb_14.png)

**Step3.插入參數**

在Params欄位上點選兩下，並在彈出的視窗設定參數。

![image_thumb_15.png](/images/posts/8037/image_thumb_15.png)

![image_thumb_12.png](/images/posts/8037/image_thumb_12.png)

![image_thumb_13.png](/images/posts/8037/image_thumb_13.png)

執行後可看到HTML被正確的插入

![image_thumb_16.png](/images/posts/8037/image_thumb_16.png)

## Conclusion

目前外掛已具基本雛型與功能，但是仍有許多的問題存在，Command也只有寫兩個，也許在一段時間，我就會..................半途放棄![Cat_17.gif](/images/posts/8037/Cat_17.gif)。(其實這篇是湊篇幅的)
