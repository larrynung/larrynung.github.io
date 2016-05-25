---
layout: post
title: "Bower - Using Bower in Visual Studio 2015"
date: 2016-01-29 05:47:00
comments: true
categories: [Bower]
keywords: "Bower"
description: "Bower - Using Bower in Visual Studio 2015"
---

Visual Studio 2015 開始支援 Bower，使用時需先為專案加入 Bower Configuration File。  

<!-- More -->

{% img /images/posts/BowerInVS2015/1.png %}

<br/>


Bower Configuration File 加入後，也會順帶加入 .bowerrc 檔，這邊會指定 Bower 套件放置的位置。  

{% img /images/posts/BowerInVS2015/2.png %}

<br/>


這邊我們可以開啟 bower.json 檔案設定所要使用的 Bower 套件。  

{% img /images/posts/BowerInVS2015/3.png %}

<br/>


或是使用 `Manage Bower Packages...` 加入 Bower 套件。   

{% img /images/posts/BowerInVS2015/4.png %}

<br/>


{% img /images/posts/BowerInVS2015/5.png %}

<br/>


在設定 Bower 套件時，我們可能會需要調用 Bower 指令查閱一些資訊，像是  Bower 套件的版本等，這邊可透過 Package Manager Console 視窗調用。  

{% img /images/posts/BowerInVS2015/6.png %}

<br/>


設定完按下編譯或是滑鼠右鍵快顯選單中的 Restore Packages 選單選項，即可透過 Bower 下載 Bower 套件。  

{% img /images/posts/BowerInVS2015/7.png %}

<br/>


我們可以透過 Visual Studio 的狀態列觀察到套件下載的狀態。  

{% img /images/posts/BowerInVS2015/8.png %}

<br/>


{% img /images/posts/BowerInVS2015/9.png %}

