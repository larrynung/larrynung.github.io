---
title: "Bower - Using Bower in Visual Studio 2015"
date: "2016-01-29 05:47:00"
description: "Bower - Using Bower in Visual Studio 2015"
tags: [Bower]
---

Visual Studio 2015 開始支援 Bower，使用時需先為專案加入 Bower Configuration File。

![1.png](/images/posts/BowerInVS2015/1.png)

Bower Configuration File 加入後，也會順帶加入 .bowerrc 檔，這邊會指定 Bower 套件放置的位置。

![2.png](/images/posts/BowerInVS2015/2.png)

這邊我們可以開啟 bower.json 檔案設定所要使用的 Bower 套件。

![3.png](/images/posts/BowerInVS2015/3.png)

或是使用 `Manage Bower Packages...` 加入 Bower 套件。

![4.png](/images/posts/BowerInVS2015/4.png)

![5.png](/images/posts/BowerInVS2015/5.png)

在設定 Bower 套件時，我們可能會需要調用 Bower 指令查閱一些資訊，像是  Bower 套件的版本等，這邊可透過 Package Manager Console 視窗調用。

![6.png](/images/posts/BowerInVS2015/6.png)

設定完按下編譯或是滑鼠右鍵快顯選單中的 Restore Packages 選單選項，即可透過 Bower 下載 Bower 套件。

![7.png](/images/posts/BowerInVS2015/7.png)

我們可以透過 Visual Studio 的狀態列觀察到套件下載的狀態。

![8.png](/images/posts/BowerInVS2015/8.png)

![9.png](/images/posts/BowerInVS2015/9.png)