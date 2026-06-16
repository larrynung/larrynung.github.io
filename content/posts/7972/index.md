---
title: "[WLW]First Experience with Windows Live Writer Plugins"
slug: "wlw-first-experience-with-windows-live-writer-plugins"
aliases: ["/posts/7972/"]
date: "2009-04-11 01:53:22"
description: "日前參考了水瓶大的『我的 Live Writer Plugin - 插入可愛貓咪表情符號 (已釋出原始碼專案)』教學文章，學習如何做Windows Live Writter Plugin。本篇做個初略的整理，詳細教學煩請移駕水瓶大的Blog。"
tags: [WLW]
---

日前參考了水瓶大的『我的 Live Writer Plugin - 插入可愛貓咪表情符號 (已釋出原始碼專案)』教學文章，學習如何做Windows Live Writter Plugin。本篇做個初略的整理，詳細教學煩請移駕水瓶大的Blog。

## Live Writter Plugin型態

Live Writter Plugin可分為兩種型態：

1. Simple:單向的插入HTML
2. Smart:雙向的HTML

## 寫作步驟

寫作步驟大概如下：

1. 新建類別庫專案
2. 加入參考WindowsLive.Writer.Api.dll (檔案在Windows Live Writter目錄下)
3. 建立個繼承ContentSource的Plugin類別
4. 為類別設定WriterPlugin與InsertableContentSource屬性 (屬性中的圖片大小約為18X16)
5. 覆寫CreateContent函式並設定HTML到Content函式參數

## 程式架構

以水瓶大那篇的範例為例，一個簡單的Windows Live Plugin架構大概如下。

![image_thumb_4.png](/images/posts/7972/image_thumb_4.png)

## 注意事項

在撰寫時須注意主要的Plugin類別需在根命名空間內。

![image_thumb_1.png](/images/posts/7972/image_thumb_1.png)

若不在根命名空間內的話

![image_thumb_3.png](/images/posts/7972/image_thumb_3.png)

![image_thumb_2.png](/images/posts/7972/image_thumb_2.png)

執行Windows Live Writter時則會彈出怪怪的錯誤訊息，這錯誤訊息應該看半天也猜不到問題所在吧。

![image_thumb.png](/images/posts/7972/image_thumb.png)
