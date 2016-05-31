---
layout: post
title: "SlowCheetah - XML Transforms extension"
date: 2014-09-03 22:22:00
comments: true
tags:  
keywords: "SlowCheetah"
description: "SlowCheetah - XML Transforms extension"
---

Web.Config Transformation 功能在我們有多個環境需要部署時很方便，但預設只支援 Web.config 的轉換，且發佈時才會做轉換的動作，開發上總是有些不便。  

<!-- More -->

<br/>

要對 Web.config 以外的設定檔案做轉換，或是要在建置時做轉換，可以參考 [Web.Config Transformation - Transform on build](http://larrynung.github.io/2014/07/07/web-dot-config-transformation-transform-on-build/) 這篇，修改專案檔讓 Microsoft.WebApplication.targets 幫我們做設定檔的轉換。但這樣的處理方式轉換檔需要自行手動加上去，設定起來是有點費工。  

</br>

若是使用 SlowCheetah 這個 Visual Studio 擴充套件相較起來就簡單了許多，可以很輕易的為設定檔加上建置時轉換。  

{% img /images/posts/SlowCheetah/1.png %}

<br/>


SlowCheetah 可直接透過 Extension Manager 進行安裝。  

{% img /images/posts/SlowCheetah/2.png %}

<br/>

{% img /images/posts/SlowCheetah/3.png %}

<br/>

{% img /images/posts/SlowCheetah/4.png %}

<br/>

{% img /images/posts/SlowCheetah/5.png %}

<br/>


使用時只要在方案總管中找到欲加入建置轉換的設定檔，按下滑鼠右鍵，在彈出的滑鼠右鍵選單中選取 `Add Transform` 滑鼠右鍵選單選項。  

{% img /images/posts/SlowCheetah/6.png %}

<br/>


在彈出的確認視窗中按下 `Yes` 按鈕繼續。  

{% img /images/posts/SlowCheetah/7.png %}

<br/>


對應的轉換檔即會幫我們產生。  

{% img /images/posts/SlowCheetah/8.png %}

<br/>


專案檔中也會做對應的修改，會加入 SlowCheetah 自己的 Targets 去做轉換，而非使用現成的 Microsoft.WebApplication.targets。  

{% img /images/posts/SlowCheetah/9.png %}

<br/>


Link
----
* [SlowCheetah - XML Transforms extension](http://visualstudiogallery.msdn.microsoft.com/69023d00-a4f9-4a34-a6cd-7e854ba318b5)
* [Huan-Lin 學習筆記: 使用 SlowCheetah 轉換組態檔](http://huan-lin.blogspot.com/2013/10/slowcheetah.html)
