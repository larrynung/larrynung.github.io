---
title: "Prepare android development environment with ADT(Android Developer Tools) Bundle for Windows"
date: "2013-11-06 12:00:00"
description: "Prepare android development environment with ADT(Android Developer Tools) Bundle for Windows"
---

Android開發環境有幾種建立方式，這邊紀錄一下怎樣透過ADT Bundle去建立Andorid的開發環境。

ADT Bundle算是比較簡單的安裝方式，它將開發需要用的工具都幫我們包裝了起來，像是：

* Eclipse + ADT plugin
* Android SDK Tools
* Android Platform-tools
* The latest Android platform
* The latest Android system image for the emulator

可至Get the Android SDK這邊，點擊右側的Download the SDK ADT Bundle for Windows按鈕。

![image_thumb.png](/images/posts/6742cf00-7d5a-4daa-b4c5-aac79a8749a2/image_thumb.png)

接著網頁會被導到授權頁面，勾選授權的選取框，決定要下載的是32還是64 bit版本，再點選Download the SDK ADT Bundle for Windows按鈕開始進行下載。

![image3_thumb.png](/images/posts/6742cf00-7d5a-4daa-b4c5-aac79a8749a2/image3_thumb.png)

下載的同時，我們可以開啟命令提示字元，輸入命令java -version，確認當前電腦是否有安裝Java。

![image10_thumb.png](/images/posts/6742cf00-7d5a-4daa-b4c5-aac79a8749a2/image10_thumb.png)

電腦環境必須要裝有JDK 6以上的版本，不然eclipse可能會跑不起來。若有需要可至Java SE Downloads這邊下載安裝。

![image4_thumb.png](/images/posts/6742cf00-7d5a-4daa-b4c5-aac79a8749a2/image4_thumb.png)

JDK環境OK，ADT Bundle也下載完了的話。我們可以將下載下來的ADT Bundle壓縮包解壓縮，進到eclipse目錄。

![image1_thumb.png](/images/posts/6742cf00-7d5a-4daa-b4c5-aac79a8749a2/image1_thumb.png)

滑鼠連點開啟eclipse.exe。

![image13_thumb.png](/images/posts/6742cf00-7d5a-4daa-b4c5-aac79a8749a2/image13_thumb.png)

eclipse就會開始運行...

![image16_thumb.png](/images/posts/6742cf00-7d5a-4daa-b4c5-aac79a8749a2/image16_thumb.png)

第一次啟用會問一下工作目錄...

![image19_thumb.png](/images/posts/6742cf00-7d5a-4daa-b4c5-aac79a8749a2/image19_thumb.png)

以及是否將使用資訊回報給Google...

![image22_thumb.png](/images/posts/6742cf00-7d5a-4daa-b4c5-aac79a8749a2/image22_thumb.png)

進到eclipse主頁面就可以開始進行Android的開發了。

![image28_thumb.png](/images/posts/6742cf00-7d5a-4daa-b4c5-aac79a8749a2/image28_thumb.png)

## Link

* Get the Android SDK
* Java SE Downloads
