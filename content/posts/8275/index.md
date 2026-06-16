---
title: "[Software]MSBuild Shell Extension"
date: "2009-05-03 12:52:08"
description: "又從保哥Blog那邊挖到好東西^^，原來有工具可以幫助我們建置專案卻不用開啟Visual Studio。而且只需安裝MSBuild Shell Extension，在專案檔上按滑鼠右鍵就可以辦到。使用上就像它的網頁上秀的圖一樣簡單。"
tags: [Software]
---

又從保哥Blog那邊挖到好東西^^，原來有工具可以幫助我們建置專案卻不用開啟Visual Studio。而且只需安裝[MSBuild Shell Extension](http://www.codeplex.com/msbuildshellex)，在專案檔上按滑鼠右鍵就可以辦到。使用上就像它的網頁上秀的圖一樣簡單。

![image_thumb.png](/images/posts/8275/image_thumb.png)

## 設定畫面

安裝完軟體後，會在[開始/所有程式 ]內看到MSBuildShellExtension目錄。點開後可看到Configurator。

![image_thumb_1.png](/images/posts/8275/image_thumb_1.png)

點擊Configurator，即可叫出設定畫面。

![image_thumb_2.png](/images/posts/8275/image_thumb_2.png)

Targets設定畫面可設定滑鼠右鍵清單按下的功能，可設定是建置Debug還是Release檔。

![image_thumb_3.png](/images/posts/8275/image_thumb_3.png)

Extensions設定頁面可設定建置的.Net Framework版本。(個人覺得這設定頁跟Target設定整合的話，建置上會更具彈性)

![image_thumb_4.png](/images/posts/8275/image_thumb_4.png)

## 建置畫面

使用上只需在專案檔上按下滑鼠右鍵，並選擇建置。

![image_thumb_5.png](/images/posts/8275/image_thumb_5.png)

即會彈出MS-Dos建置視窗與錯誤視窗。

![image_thumb_6.png](/images/posts/8275/image_thumb_6.png)

建置完後到Bin目錄下找到建置完的檔案即可。

## Link

* [The Will Will Web-介紹好用工具：MSBuild Shell Extension](http://blog.miniasp.com/post/2009/04/Useful-tools-MSBuild-Shell-Extension.aspx)
* [CodePlex-MSBuildShellExtension](http://www.codeplex.com/msbuildshellex)
