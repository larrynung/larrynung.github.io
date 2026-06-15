---
title: "Grunt - Using Grunt in Visual Studio 2015"
date: "2016-01-28 01:25:00"
description: "Grunt - Using Grunt in Visual Studio 2015"
tags: [Grunt]
---

Visual Studio 2015 開始支援 Grunt，使用時需先為專案加入 NPM Configuration File。

![1.png](/images/posts/GruntInVS2015/1.png)

還有 Grunt Configuration File。

![2.png](/images/posts/GruntInVS2015/2.png)

接著在 package.json 中加入要使用的 Grunt plugin。

![3.png](/images/posts/GruntInVS2015/3.png)

![4.png](/images/posts/GruntInVS2015/4.png)

設定完按下編譯或是滑鼠右鍵快顯選單中的 Restore Packages 選單選項，即可透過 NPM 下載 Grunt plugin。

![5.png](/images/posts/GruntInVS2015/5.png)

我們可以透過 Visual Studio 的狀態列觀察到套件下載的狀態。

![6.png](/images/posts/GruntInVS2015/6.png)

![7.png](/images/posts/GruntInVS2015/7.png)

若有需要也可以透過 Output 視窗查看細部處理資訊。

![8.png](/images/posts/GruntInVS2015/8.png)

下載完畢，設定完 gruntfile.js，我們就可以在 Task Runner Explorer 點選對應的 Task 進行運行。

![9.png](/images/posts/GruntInVS2015/9.png)